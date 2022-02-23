from urllib import response
import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square', methods=['POST'])
def square():
    response = {}
    data = request.get_json( )
    if data.get('number', ''):
        number = int(data['number'])
        response = {'status': 200, 'result': math.sqrt(number)}
    else:
        response = {'status': 500, 'result': 'Error'}
    return jsonify(response)

@app.route('/score_Conv', methods=['GET', 'POST'])
def scoreConv():
    if request.method == 'GET':
        return render_template('score.html')
    else:
        result = {}
        data = request.get_json()
        if data.get('score'):
            score = int(data['score'])
            if score >= 90 and score <= 100:
                result = {
                    'status': 200,
                    'result': 'A',
                }
            elif score >= 80 and score < 90:
                result = {
                    'status': 200,
                    'result': 'B',
                }
            elif score >= 70 and score < 80:
                result = {
                    'status': 200,
                    'result': 'C',
                }
            elif score >= 60 and score < 70:
                result = {
                    'status': 200,
                    'result': 'D',
                }
            elif score > 0 and score < 60:
                result = {
                    'status': 200,
                    'result': 'E',
                }
            else:
                result = {
                    'status': 500,
                    'result': 'Error',
                }
        else:
            result = {'status': 500, 'result': 'Error'}
        return jsonify(result)

@app.route('/hypotenuse', methods=['GET', 'POST'])
def hypotenuse():
    if request.method == 'GET':
        return render_template('hypotenuse.html')
    else:
        result = {}
        data = request.get_json()
        if data.get('baseNumber', 'heightNumber'):
            baseNumber = int(data['baseNumber'])
            heightNumber = int(data['heightNumber'])
            result = {
                'status': 200,
                'result': math.sqrt(baseNumber**2 + heightNumber**2)
            }
        else:
            result = {'status': 500, 'result': 'Error'}
        return jsonify(result)
