import json
from difflib import get_close_matches as gcm

data = json.load(open('data.json', "r"))

# print(type(data))


def translate(word):

    word = word.lower()
    if (word in data) or (word.title() in data) or (word.upper() in data):
        return data[word]
    elif len(gcm(word, data.keys(), cutoff=0.8)) > 0:
        print("Did you mean to ask {}?".format(
            gcm(word, data.keys(), cutoff=0.8)[0]))

        fl = True
        while(fl):
            x = input("Enter Y for yes and N for no.")
            if x == 'Y':
                fl = False
                return data[word]
            elif x == 'N':
                fl = False
                return "No such word doesn't exist in dictionary yet"
            else:
                return "You haven't answered correctly"
    else:
        return "This word doesn't exist in dictionary yet"


inp = input("Enter Input:")

if (type(translate(inp)) == list):

    y = translate(inp)
    for i in range(len(y)):
        print(y[i])
else:
    print(translate(inp))
