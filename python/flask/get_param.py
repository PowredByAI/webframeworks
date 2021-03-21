from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/<name>', methods=['GET'])
def home(name):
    return "hello {0}".format(name)
if __name__ == '__main__':
    app.run(port=3030, host='0.0.0.0', debug=True)