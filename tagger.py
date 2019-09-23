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

    def initialize_probabilities(self, sentence):
        if type(sentence) != list:
            sys.exit("Incorrect input to method")
        if len(sentence) <= 0:
            sys.exit("Incorrect input to method")

        first_token = sentence[0][1]
        if first_token in self.initial_tag_frequency.keys():
            self.initial_tag_frequency[first_token] = self.initial_tag_frequency.pop(first_token) + 1
        else:
            self.initial_tag_frequency[first_token] = 1

        for word_token in sentence:
            self.emission_frequency[word_token] = (self.emission_frequency.pop(word_token) + 1) if (
                    word_token in self.emission_frequency.keys()) else 1
            self.transition_frequency[word_token[1]] = (self.transition_frequency.pop(word_token[1]) + 1) if (
                    word_token[1] in self.transition_frequency.keys()) else 1

    def viterbi_decode(self, sentence):
        if type(sentence) != str:
            sys.exit("Incorrect input to method")
        """
		YOUR CODE GOES HERE: Complete the rest of the method so that it computes the most likely sequence of tags as described in the question
		"""

    def get_initial_tag_frequency(self):
        return self.initial_tag_frequency

    def get_initial_tag_total(self):
        count = 0
        for word in self.initial_tag_frequency.keys():
            count += self.initial_tag_frequency.get(word)
        return count

    def get_transition_frequency(self):
        return self.transition_frequency

    def get_transition_total(self):
        count = 0
        for word in self.transition_frequency.keys():
            count += self.transition_frequency.get(word)
        return count

    def get_emission_frequency(self):
        return self.transition_frequency

    def get_emission_total(self):
        count = 0
        for word in self.transition_frequency.keys():
            count += self.transition_frequency.get(word)
        return count
