
from collections import defaultdict, deque
import sys


'''
Computes all transformations from a word word_1 to a word word_2, consisting of
sequences of words of minimal length, starting with word_1, ending in word_2,
and such that two consecutive words in the sequence differ by at most one letter.
All words have to occur in a dictionary with name dictionary.txt, stored in the
working directory.
'''


dictionary_file = 'dictionary.txt'
with open(dictionary_file) as file:
	words = readlines()
	lexicon = word.split('\n')
	print(lexicon)

def get_words_and_word_relationships():
    with open(dictionary_file) as file:
		words = readlines()
		lexicon = word.split('\n')
	# Replace pass above with your code

def word_ladder(word_1, word_2):
    lexicon, closest_words = get_words_and_word_relationships()
    # Complete this function

