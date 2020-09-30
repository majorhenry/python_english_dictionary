import json
from difflib import get_close_matches

data = json.load(open("data.json")) #if file gets too big its better to use a query.

#print(file)
#print(data['rain'])

def dictionary(word):
    word = word.lower()
    if word in data:
        return  data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys())[0])
        if yn == 'Y' or 'y':
            #rerurn get_close_matches(word, data.keys())[0]
            return dictionary(get_close_matches(word, data.keys())[0])
        elif yn == 'N' or 'n':
            return "The word does not exist. Please double check and try again!"
       else:
           return "We did not understand your entry"
    else:
        return "The word does not exist. Please double check and try again!"

word = input('Enter word: ')

output = dictionary(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
#print(dictionary(word))
