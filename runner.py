import tagger as tag

myTagger = tag.Tagger()
tokenList = myTagger.load_corpus('brown_corpus_modified')

print(tokenList)