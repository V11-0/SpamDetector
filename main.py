import joblib
from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route("/checkEmail", methods=['POST'])
def main():

    model = joblib.load("model/model.pkl")

    return Response(status=501)
    

app.run()