from app.Rhyme_Bot import get_best_word, get_rhyme_words
import json


def get_last_word(json_dict):
    full_bar = json_dict['queryResult']['queryText']
    word_list = full_bar.split()
    print('last word is:' + word_list[-1])
    return word_list[-1]


def respond(json_dict):
    last_word = get_last_word(json_dict)
    print('responding...')
    return make_fulfillment(get_best_word(get_rhyme_words(last_word)))


def make_fulfillment(word):
    """ returns a json str containing the repsonse text for dialogflow"""
    response_dict = {'fulfillmentText': word}
    print('making fulfillment...')
    return json.dumps(response_dict)
