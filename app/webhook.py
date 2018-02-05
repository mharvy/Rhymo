from app.Rhyme_Bot import get_best_word, get_rhyme_words
import json


def get_last_word(json_dict):
    full_bar = json_dict['queryResult']['queryText']
    word_list = full_bar.split()
    return word_list[-1]


def respond(json_dict):
    last_word = get_last_word(json_dict)
    return make_fulfillment(get_best_word(get_rhyme_words(last_word)))


def make_fulfillment(word):
    """ returns a json str containing the repsonse text for dialogflow"""
    response_dict = {'fulfillmentText': word}
    return json.dumps(response_dict)


print(make_fulfillment(get_best_word(get_rhyme_words('hello'))))
