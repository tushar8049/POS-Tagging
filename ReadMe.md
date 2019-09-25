<h1> Part Of Speech - Tagging (POS-Tagging)</h1>
Develop a hidden Markov Model for part-of-speech
(POS) tagging, using a modified Brown corpus as training data. To simplify
the problem, we will use a tag-set which is composed of 11 tags. i.e. Noun, Pronoun, Verb, Adjective, Adverb, Conjunction, Preposition, Determiner, Number,
Punctuation and Other.

<h3>Description</h3>

The corpus for this can be downloaded from this link:

https://github.com/tushar8049/POS-Tagging/tree/master/brown_corpus_modified

Your goal is to design and implement a class ‘Tagger’ that is able to tag the
following sentences:

1. The Secretariat is expected to race tomorrow .
2. People continue to enquire the reason for the race for outer space .


<h3>Execution</h3>
<p>
To execute POS - Tagging use the below line of code:
</p>
<code>
    > python runner.py
</code>
<p>
</p>

<h3>Output</h3>
<p>
Output for the test Sentences is as below:
</p>
<code>
Tagging of Sentence 1:  ['DETERMINER', 'NOUN', 'VERB', 'VERB', 'PREPOSITION', 'NOUN', 'NOUN', 'PUNCT']
</code>
<p></p>
<code>
Tagging of Sentence 2:  ['NOUN', 'VERB', 'PREPOSITION', 'DETERMINER', 'DETERMINER', 'NOUN', 'PREPOSITION', 'DETERMINER', 'NOUN', 'PREPOSITION', 'ADJECTIVE', 'NOUN', 'PUNCT']
</code>
