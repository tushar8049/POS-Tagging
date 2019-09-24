import tagger as tag

corpus_path = 'brown_corpus_modified'

myTagger = tag.Tagger()
tokenList = myTagger.load_corpus(corpus_path)

# print(tokenList)

for sentence in tokenList:
    myTagger.initialize_frequencies(sentence)

myTagger.initialize_probabilities()
print(myTagger.get_initial_tag_frequency())
print(myTagger.get_transition_total())

print(myTagger.get_emission_total())
print(myTagger.get_word_total())
print("Initial Tag Probability: \n", myTagger.get_initial_tag_probability())

print("Transition Probability: \n", myTagger.get_transition_probability())

print("Emission Probability: \n", myTagger.get_emission_probability())

