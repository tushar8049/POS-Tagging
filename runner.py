import tagger as tag


"""
Loading Corpus
"""
corpus_path = 'brown_corpus_modified'
myTagger = tag.Tagger()
tokenList = myTagger.load_corpus(corpus_path)


"""
Initializing Frequencies and then the Probabilities for:
Initial Tagging, Transition, Emission
"""
for sentence in tokenList:
    myTagger.initialize_frequencies(sentence)
myTagger.initialize_probabilities()
# print("Initial Tag Probability: \n", myTagger.get_initial_tag_probability())
#
# print("Transition Probability: \n", myTagger.get_transition_probability())
#
# print("Emission Probability: \n", myTagger.get_emission_probability())


"""
Testing the Tagging using Viterbi Decode for two sentences:
1. The Secretariat is expected to race tomorrow .
2. People continue to enquire the reason for the race for outer space .
"""
sentence1 = "The Secretariat is expected to race tomorrow ."
sentence2 = "People continue to enquire the reason for the race for outer space ."
print("Tagging of Sentence 1: ", myTagger.viterbi_decode(sentence1))
print("Tagging of Sentence 2: ", myTagger.viterbi_decode(sentence2))
