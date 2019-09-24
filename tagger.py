import os
import io
import sys


class Tagger:

    def __init__(self):
        self.initial_tag_probability = {}
        self.transition_probability = {}
        self.emission_probability = {}
        self.initial_tag_frequency = {}
        self.transition_frequency = {}
        self.emission_frequency = {}
        self.word_frequency = {}
        self.token_frequency = {}

    def load_corpus(self, path):
        if not os.path.isdir(path):
            sys.exit("Input path is not a directory")
        list_of_list = []
        for filename in os.listdir(path):
            filename = os.path.join(path, filename)
            try:
                reader = io.open(filename)
                line = reader.readline()
                while line:
                    line_tuple_list = []
                    token_POS = line.split(' ')
                    for t in token_POS:
                        if len(t.split('/')) == 2:
                            temp_tuple = (t.split('/')[0], t.split('/')[1])
                            line_tuple_list.append(temp_tuple)
                    if len(line_tuple_list) > 0:
                        list_of_list.append(line_tuple_list)
                    line = reader.readline()
            except IOError:
                sys.exit("Cannot read file")
        print("Total Sentences: ", len(list_of_list))
        return list_of_list

    def initialize_frequencies(self, sentence):
        if type(sentence) != list:
            sys.exit("Incorrect input to method")
        if len(sentence) <= 0:
            sys.exit("Incorrect input to method")

        """
            Calculating the Frequency for Emission, transition and Initial Tag
        """
        self.initial_tag_frequency[sentence[0][1]] = (self.initial_tag_frequency.pop(sentence[0][1]) + 1) if (
                sentence[0][1] in self.initial_tag_frequency.keys()) else 1

        for word_token in sentence:
            self.emission_frequency[word_token] = (self.emission_frequency.pop(word_token) + 1) if (
                    word_token in self.emission_frequency.keys()) else 1
            self.word_frequency[word_token[0]] = (self.word_frequency.pop(word_token[0]) + 1) if (
                    word_token[0] in self.word_frequency.keys()) else 1
            self.token_frequency[word_token[1]] = (self.token_frequency.pop(word_token[1]) + 1) if (
                    word_token[1] in self.token_frequency.keys()) else 1

        for i in range(0, len(sentence) - 1):
            self.transition_frequency[(sentence[i][1], sentence[i + 1][1])] = (
                    self.transition_frequency.pop((sentence[i][1], sentence[i + 1][1])) + 1) if (
                    (sentence[i][1], sentence[i + 1][1]) in self.transition_frequency.keys()) else 1

    def initialize_probabilities(self):
        """
            Calculating the Frequency for Emission, transition and Initial Tag
        """
        for key in self.initial_tag_frequency.keys():
            self.initial_tag_probability[key] = float(self.initial_tag_frequency[key]) / self.get_initial_tag_total()
        for key in self.transition_frequency.keys():
            self.transition_probability[key] = float(self.transition_frequency[key] / self.token_frequency[key[0]])
        for key in self.emission_frequency.keys():
            self.emission_probability[key] = float(self.emission_frequency[key] / self.word_frequency[key[0]])

    def viterbi_decode(self, sentence):
        if type(sentence) != str:
            sys.exit("Incorrect input to method")
        probability = 1.0
        tagging = []
        words = sentence.split(' ')
        print("Words of Sentence: ", words)
        tokens = []
        for token in self.token_frequency.keys():
            tokens.append(token)
        for i in range(0, len(words)):
            max_probability = []
            if i == 0:
                for token in tokens:
                    if (words[i], token) in self.emission_probability.keys():
                        max_probability.append(self.initial_tag_probability[token] * self.emission_probability[(words[i], token)])
                    else:
                        max_probability.append(self.initial_tag_probability[token] * (1 / self.token_frequency[token]))
            else:
                for token in tokens:
                    if (words[i], token) in self.emission_probability.keys():
                        max_probability.append(self.transition_probability[(tagging[i-1], token)] * self.emission_probability[(words[i], token)])
                    else:
                        max_probability.append(self.transition_probability[(tagging[i-1], token)] * (1 / self.token_frequency[token]))

            index = max_probability.index(max(max_probability))
            tagging.append(tokens[index])

        return tagging

    def get_transition_frequency(self):
        return self.transition_frequency

    def get_emission_frequency(self):
        return self.emission_frequency

    def get_word_frequency(self):
        return self.word_frequency

    def get_initial_tag_frequency(self):
        return self.initial_tag_frequency

    def get_initial_tag_probability(self):
        return self.initial_tag_probability

    def get_emission_probability(self):
        return self.emission_probability

    def get_transition_probability(self):
        return self.transition_probability

    def get_transition_probability_total(self):
        count = 0
        for word in self.transition_frequency.keys():
            count += self.transition_frequency.get(word)
        return count

    def get_emission_total(self):
        count = 0
        for word in self.emission_frequency.keys():
            count += self.emission_frequency.get(word)
        return count

    def get_word_total(self):
        count = 0
        for word in self.word_frequency.keys():
            count += self.word_frequency.get(word)
        return count

    def get_transition_total(self):
        count = 0
        for word in self.transition_frequency.keys():
            count += self.transition_frequency.get(word)
        return count

    def get_initial_tag_total(self) -> float:
        count = 0
        for word in self.initial_tag_frequency.keys():
            count += self.initial_tag_frequency.get(word)
        return count

    def get_initial_tag_probability_total(self) -> float:
        count = 0.0
        for word in self.initial_tag_probability.keys():
            count += self.initial_tag_probability.get(word)
        return count
