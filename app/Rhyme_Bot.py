import json
import requests
from pprint import pprint as pp


apiAddress = "https://api.datamuse.com/words?"


# This returns a list of dicts
def get_rhyme_words(word):
    final_words = []
    tail_request = "rel_rhy=" + word
    final_request = apiAddress + tail_request
    rhyme_words = json.loads(requests.get(final_request).text)
    for wordDict in rhyme_words:
        final_words.append([wordDict['word'], wordDict['score'], wordDict['numSyllables']])

    return final_words


# this is my rating algorithm, which really prefers high syllable words
def word_rating(rating, num_syllables):
    return (rating / 10000) * (num_syllables / 5)


# Returns the 'coolest' word
def get_best_word(word_list):
    cur_best_score = word_rating(word_list[0][1], word_list[0][2])
    cur_best_word_index = 0
    for i in range(0, len(word_list)):
        score = word_list[i][1]
        syllables = word_list[i][2]
        cur_score = word_rating(score, syllables)
        if cur_score > cur_best_score:
            cur_best_score = cur_score
            cur_best_word_index = i

    return word_list[cur_best_word_index][0]
