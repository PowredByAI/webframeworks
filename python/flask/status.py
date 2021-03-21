from flask import Flask,request,jsonify,make_response
app = Flask(__name__)
@app.route('/<code>', methods=['GET'])
def home(code):
    res = make_response("hello",code)
    return res
if __name__ == '__main__':
    app.run(port=3030, host='0.0.0.0', debug=True)