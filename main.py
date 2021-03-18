import pandas as pd
import joblib
import re
from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

words_frequency = []
char_frequency = []
capital_data = []
number_words = 0
number_chars = 0
message = ''

# Things: We assume message does not have line breaks 
@app.route("/checkEmail", methods=['POST'])
@cross_origin()
def checkEmail():

    model = joblib.load("model/model.pkl")

    global message
    message = request.json['message']
        
    if len(message) < 5:
        return Response(status=400)

    # Count capitals related things
    countCapitalLettersSequences()

    message = message.lower()

    # Count number of words and chars
    message_words = message.split(" ")

    global number_words, number_chars
    number_words = len(message_words)
    number_chars = len(message)

    # Count Amount of each word and chars defined in the dataset
    countDatasetWords(message_words)
    countDatasetChars()

    # Until here we have the absolute frquency of words and chars, we need to get this data in percentages
    data = toModelDataFormat()
    
    # Add columns names as np array, as in the last section of model.ipynb
    # Get columns names by reading the dataset
    df = pd.read_csv("./data/dataset_44_spambase.csv")
    df = df.drop(['class'], axis = 1)
    
    final_data = mergeLabels(df.columns, data)
    frame = model.predict(final_data)

    print(final_data)

    if (frame.max() == 1):
        e = True
    else:
        e = False

    return {'class': e}

def countDatasetWords(message_words):

    global words_frequency

    for mword in message_words:
        for index, word in enumerate(words_frequency):
            if (word[0] == mword):
                words_frequency[index][1] += 1

def countDatasetChars():

    global char_frequency
    
    for mchar in message:
        for index, char in enumerate(char_frequency):
            if (mchar[0] == char):
                char_frequency[index][1] += 1

def countCapitalLettersSequences():

    capital_sequences = []

    for index, char in enumerate(message):
        if (char.isupper()):
            if (message[index - 1].isupper() and index > 0):
                capital_sequences[-1] = capital_sequences[-1] + char
            else:
                capital_sequences.append(char)

    # Get the data we want

    # Average length of uninterrupted sequences of capital letters
    global capital_data
    len_sum = 0

    for sequence in capital_sequences:
        len_sum += len(sequence)

    try:
        len_avg = len_sum / len(capital_sequences)
    except ZeroDivisionError:
        len_avg = 0

    capital_data.append(len_avg)

    # Length of longest uninterrupted sequence of capital letters
    len_longest = 0

    for sequence in capital_sequences:
        if (len(sequence) > len_longest):
            len_longest = len(sequence)

    capital_data.append(len_longest)

    # total number of capital letters in the e-mail
    capital_data.append(len_sum)

def toModelDataFormat():

    email = []
    
    # To percentage frequency and add to email model
    for word_freq in words_frequency:
        email.append(word_freq[1] / number_words)

    for char_freq in char_frequency:
        email.append(char_freq[1] / number_chars)

    # We add the capital letters data
    for data in capital_data:
        email.append(data)

    return email

def mergeLabels(columns, data):

    d = {}

    for key in columns:
        for value in data:
            d[key] = [value]
            data.remove(value)
            break

    return pd.DataFrame.from_dict(d)
    
def main():

    global words_frequency, char_frequency
    
    # Define in an array the words used by the database
    words_frequency = [
        ['make'], ['address'], ['all'], ['3d'], ['our'], ['over'], ['remove'], ['internet'],
        ['order'], ['mail'], ['receive'], ['will'], ['people'], ['report'], ['addresses'],
        ['free'], ['business'], ['email'], ['you'], ['credit'], ['your'], ['font'], ['000'],
        ['money'], ['hp'], ['hpl'], ['george'], ['650'], ['lab'], ['labs'], ['telnet'], ['857'],
        ['data'], ['415'], ['85'], ['technology'], ['1999'], ['parts'], ['pm'], ['direct'], ['cs'],
        ['meeting'], ['original'], ['project'], ['re'], ['edu'], ['table'], ['conference']
    ]

    # Define the second index of each set the number of occurrences of word, we start with 0
    for word_data in words_frequency:
        word_data.append(0)

    # And the chars, same thing
    char_frequency = [[';'], ['('], ['['], ['!'], ['$'], ['#']]

    for char_data in char_frequency:
        char_data.append(0)

    
    app.run()

main()