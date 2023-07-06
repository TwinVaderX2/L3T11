"""
Task: SE L3T11

Author: Phillip van Staden

Date: 06-07-2023

Description: 

    Compulsory Task
    Follow these steps:
    ●   Read the introduction about garden path sentences and study a few of
        the examples on Wikipedia.
    ●   Create a new Python file called garden.py.
    ●   Find at least 2 garden path sentences from the web or think up your own.
    ●   Store the sentences you have identified or created in a list called
        gardenpathSentences
    ●   Add the following sentences to your list:
        ○   Mary gave the child a Band-Aid.
        ○   That Jill is never here hurts.
        ○   The cotton clothing is made of grows in Mississippi.
    ●   Tokenise each sentence in the list and perform named entity recognition.
    ●   Tokenise each sentence in the list and perform entity recognition.
    ●   Examine how spaCy has categorised each sentence. Then, use
        spacy.explain to look up and print the meaning of entities that you don’t
        understand. For example: print(spacy.explain("FAC"))
    ●   At the bottom of your file, write a comment about two entities that you
        looked up. For each entity answer the following questions:
        ○   What was the entity and its explanation that you looked up?
        ○   Did the entity make sense in terms of the word associated with it?

"""

# import modules
import spacy

# load English model
nlp = spacy.load('en_core_web_sm')

# create list of garden path sentences
garden_list = [
    'The old man the boat.',
    'The complex houses married and single soldiers and their families.',
    'Mary gave the child a Band-Aid.',
    'That Jill is never here hurts.',
    'The cotton clothing is made of grows in Mississippi.',
]

# Tokenization of list
nlp_list = []

for idx in garden_list:
    doc = nlp(idx)
    nlp_list.append(doc)

# print token text for each doc in list
for doc in nlp_list:
    for token in doc:
        print(token.text)

# perform named entity recognition
for doc in nlp_list:
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Note to mentors: Instruction to perform entity recognition is duplication of previous instruction. 

# Define/ explain unknown entity type
entity_GPE = spacy.explain('GPE')
print(f"GPE: {entity_GPE}")

# Answer question/instruction:
"""
    ORG: Companies, agencies, institutions
    MONEY: Monetary values, including unit

    ORG is an abrivation for organizations which includes, but may not be limited to companies, agencies and institutions
    MONEY is discriptive for a range of monetary values which is comonly depicted by symbols such as $ for USD (United States Dollar)
"""