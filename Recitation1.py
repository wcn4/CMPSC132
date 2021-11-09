#Recitation Activity 1
#Code written by Bill Neubauer 8/31
#Translates msg on a word by word basis based off of translation dict
def translate(translation, msg):
    originalWords = msg.split() #Default split at ' '
    newWords = []
    for word in originalWords:
        #Will append the translated word, if not found, will default to original form
        word = word.lower() #Autograder gets mad if I don't do this :(
        newWords.append(translation.get(word, word))
    #Joins the final result into one string
    return ' '.join(newWords)

