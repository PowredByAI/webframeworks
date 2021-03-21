from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "hi~"
if __name__ == '__main__':
    app.run(port=3030, host='0.0.0.0', debug=True)
