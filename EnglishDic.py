
""" This script is implementing an offline English to English Dictionary. 
    With the help to this dictionary, we can find definition or meaning of any english word.
    This script also suggests you a word if are giving a wrong spelling for a word .
"""
import json
import difflib
from difflib import get_close_matches

# data for finding meaning of a given word .
data = json.load(open('data.json'))

def getDefinition(word):
    """
    :param word : Word whose whose meaning we are searching.
    :return: Definition of word if it exists else return error message.
    """

    if word in data:
        return data[word]
    else :
        # list of keys in data that are 80% close to word.
        matches = get_close_matches(word,data.keys(),cutoff=0.8)
        if len(matches)!=0:
            print('Did u mean '+matches[0]+'? Enter y if yes else n')
            if input() =='y':
                return data[matches[0]]
            else:
                return 'The word you entered does not exist. Please double check it.'
        else:
            return 'The word you entered does not exist. Please double check it.'


if __name__ == '__main__':

    word = input('Enter word\n')
    word = word.lower()
    meaning = getDefinition(word)
    if type(meaning)!=str:
        for i in range(len(meaning)):
            print(str(i+1)+".) "+meaning[i])
    else :
        print(meaning)


