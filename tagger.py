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
        for filename in os.listdir(path):
            filename = os.path.join(path, filename)
            try:
                reader = io.open(filename)
                """
				YOUR CODE GOES HERE: Complete the rest of the method so that it outputs a list of lists as described in the question
				"""
            except IOError:
                sys.exit("Cannot read file")

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
