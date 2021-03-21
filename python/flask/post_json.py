from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/', methods=['POST'])
def home():
    data = request.json
    return jsonify(data)
if __name__ == '__main__':
    app.run(port=3030, host='0.0.0.0', debug=True)