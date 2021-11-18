from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/train', methods=['GET', 'POST'])
def lic():
    return "+"


if __name__ == '__main__':
    app.run()
