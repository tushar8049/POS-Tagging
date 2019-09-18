import os
import io
import sys


class Tagger:

    def __init__(self):
        self.initial_tag_probability = None
        self.transition_probability = None
        self.emission_probability = None

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

    def initialize_probabilities(self, sentences):
        if type(sentences) != list:
            sys.exit("Incorrect input to method")
        """
		YOUR CODE GOES HERE: Complete the rest of the method so that it computes the probability matrices as described in the question
		"""

    def viterbi_decode(self, sentence):
        if type(sentence) != str:
            sys.exit("Incorrect input to method")
        """
		YOUR CODE GOES HERE: Complete the rest of the method so that it computes the most likely sequence of tags as described in the question
		"""
