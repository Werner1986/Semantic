import spacy

# Load the language model
nlp = spacy.load('en_core_web_md')

# Compare word similarities
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Compare word similarities in a loop
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Compare sentence similarities
sentence_to_compare = "Why is my cat on the car"
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
    

            ## The interesting observations: ##
'''
--> The similarity between "cat" and "monkey" is relatively low,
indicating that they are dissimilar words.

--> The similarity between "banana" and "monkey" is higher than the similarity between "banana" and "cat."
This suggests that the model recognizes a closer semantic relationship between "banana" and "monkey" than
between "banana" and "cat."

--> It is interesting to note that the model seems to capture the association between monkeys and bananas,
likely due to the common context of monkeys eating bananas.

'''
# My own example #

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("coffee")
word2 = nlp("tea")
word3 = nlp("juice")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Compare word similarities in a loop
tokens = nlp('coffee water tea juice')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Compare sentence similarities
sentence_to_compare = "Where is the coffee machine for coffee"
sentences = [
    "where did my cup go",
    "Hi, there is my cup",
    "I've lost my cup in my cup",
    "I'd like my glass back",
    "I will name my glass Mine"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
    
            ## The interesting observations: ##
'''    
--> The similarity between "coffee" and "tea" is relatively high
indicating that they are similar words likely due to their,
association as popular hot beverages.

--> The similarity between "juice" and "tea" is higher than the similarity between,"juice" and "coffee."
This suggests that the model recognizes a closer semantic relationship between "juice" and "tea" than,
between "juice" and "coffee," possibly due to both being commonly consumed beverages.

--> It is interesting to note that the model recognizes some level of similarity between "juice" and "coffee,"
even though they are different types of beverages.

'''
