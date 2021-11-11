from flask import Flask, render_template,jsonify,request
import sys
sys.path.append('../back/')
from huffman_final import huffman
app = Flask(__name__)

@app.route('/about')
def hello():
    # return "212"
    return render_template('about.html')

@app.route('/jsondemo', methods = ['post'])
def jsondemo():
    print('haha')
    info = request.json.get('name')
    print(info)

    path = "D:\vscodePythonSpace\Data_Structure_Course_Design\cs_dataData_Structure_Course_Design\cs_data\\"
    path += str(info)
    with open(path, "r") as f:
        data = f.read()
    return data

@app.route('/encode', methods = ['post'])
def encode():
    print('encode')
    ii = request.json.get('name')
    path1 = "cs_data/"
    print(path1)
    path1 += str(ii)
    a = huffman(path1)
    a.get_code()
    return a.encodingFile(path1)

if __name__ == '__main__':
    app.run(port=8080, debug=True)

