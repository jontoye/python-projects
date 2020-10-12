import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        suggest = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        while True:
            ans = input("Did you mean %s? [y,n]  " % suggest)
            if ans.lower() == 'y' or ans == '':
                return data[suggest]
            if ans.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no")
    return "Word not found. Please check your input."


while True:
    word = input("Enter a word or type '\end' to exit: ")
    if word == '\end':
        break
    response = lookup(word)
    if type(response) == list:
        for line in response:
            print("  -->", line)
    else:
        print(response)
