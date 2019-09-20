import tagger as tag

corpus_path = 'brown_corpus_modified'

myTagger = tag.Tagger()
tokenList = myTagger.load_corpus(corpus_path)

print(tokenList)
