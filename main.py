import joblib
from flask import Flask, jsonify, Response, request

app = Flask(__name__)

words_frequency = []
char_frequency = []

@app.route("/checkEmail", methods=['POST'])
def checkEmail():

    model = joblib.load("model/model.pkl")

    message = request.json['message']
        
    if len(message) == 0:
        return Response(status=400)

    # Count Words

    return message
    
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