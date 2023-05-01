from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    regno = request.form['regno']
    response = requests.get(f'http://backend:5001/api/v1/vaccination/{regno}')
    if response.status_code == 200:
        data = response.json()
        return render_template('result.html', data=data)
    else:
        return render_template('result.html', error=')


