import joblib
from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route("/checkEmail", methods=['POST'])
def checkEmail():

    model = joblib.load("model/model.pkl")

    return Response(status=501)
    
def main():
    
    # Define in an array the words used by the database
    words_frequency = [
        'make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet',
        'order', 'mail', 'receive', 'will', 'people', 'report', 'addresses',
        'free', 'business', 'email', 'you', 'credit', 'your', 'font', '000',
        'money', 'hp', 'hpl', 'george', '650', 'lab', 'labs', 'telnet', '857',
        'data', '415', '85', 'technology', '1999', 'parts', 'pm', 'direct', 'cs',
        'meeting', 'original', 'project', 're', 'edu', 'table', 'conference'
    ]

    # And the chars
    char_frequency = [';', '(', '[', '!', '$', '#']

    app.run()

main()