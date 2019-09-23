import tagger as tag

corpus_path = 'brown_corpus_modified'

myTagger = tag.Tagger()
tokenList = myTagger.load_corpus(corpus_path)

# print(tokenList)

for sentence in tokenList:
    myTagger.initialize_probabilities(sentence)

print(myTagger.get_initial_tag_frequency())
print(myTagger.get_initial_tag_total())
print(myTagger.get_transition_total())
