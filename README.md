# Hyperiondev Software Engineering Bootcamp L3T11 
This project is part of course offered by Hyperiondev
The purpose is to train students on the use of spacy in NLP.

## Task
Read the introduction about garden path sentences and study a few of
the examples on Wikipedia.
* Create a new Python file called garden.py.
* Find at least 2 garden path sentences from the web or think up your own.
* Store the sentences you have identified or created in a list called gardenpathSentences
* Add the following sentences to your list:
    * Mary gave the child a Band-Aid.
    * That Jill is never here hurts.
    * The cotton clothing is made of grows in Mississippi.
* Tokenise each sentence in the list and perform named entity recognition.
* Tokenise each sentence in the list and perform entity recognition.
* Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t understand. For example: print(spacy.explain("FAC"))
* At the bottom of your file, write a comment about two entities that you looked up. For each entity answer the following questions:
    * What was the entity and its explanation that you looked up?
    * Did the entity make sense in terms of the word associated with it?

# Run program locally
## Requirements
* Python

## Installation
1. Clone repository
2. Create virtual environment (command: python -m venv [name of virtual environment])
3. Activate virtual environment (command: [name of virtual environment]\scripts\activate)
4. Install requirements from requirements.txt (command: python -m pip install -r requirements.txt)

## User guide
1. cd into src folder
2. run program (command: python garden.py)

# Run program via Docker
## Requirements
* Docker desktop
* Docker hub account

## Installation
1. Clone repository
2. Run Docker desktop and login
3. cd into directory using commandline
4. Create docker image (command: docker build -t [image name] .)
5. Run image (command: docker run [image name])

## User guide
1. refer to instruction above to run image