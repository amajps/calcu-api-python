from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.json['a']
    b = request.json['b']
    op = request.json['op']

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        return jsonify({'error': 'Invalid operator'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
