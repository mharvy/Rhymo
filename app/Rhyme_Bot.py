import json
import requests


apiAddress = "https://api.datamuse.com/words?"


# This returns a list of dicts
def get_rhyme_words(word):
    final_words = []
    tail_request = "rel_rhy=" + word
    final_request = apiAddress + tail_request
    rhyme_words = json.loads(requests.get(final_request).text)
    print(rhyme_words)
    for wordDict in rhyme_words:
        final_words.append([wordDict['word'], wordDict.get('score', 0), wordDict['numSyllables']])

    return final_words


# this is my rating algorithm, which really prefers high syllable words
def word_rating(rating, num_syllables):
    return (rating / 10000) * (num_syllables / 5)


# Returns the 'coolest' word
def get_best_word(word_list):
    if len(word_list) == 0:
        return 'No rhyming words :('
    cur_best_score = word_rating(word_list[0][1], word_list[0][2])
    cur_best_word_index = 0
    for i in range(0, len(word_list)):
        score = word_list[i][1]
        syllables = word_list[i][2]
        cur_score = word_rating(score, syllables)
        if cur_score > cur_best_score:
            cur_best_score = cur_score
            cur_best_word_index = i

    coolWord = word_list[cur_best_word_index][0]
    print('the word being chosen is "' + coolWord + '", with a score of ' + str(cur_best_score))
    return coolWord


print(get_best_word(get_rhyme_words('father')))
