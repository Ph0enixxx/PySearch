from flask import Flask
from Doc import Doc
#提供接口
app = Flask(__name__)
doc = Doc()

@app.route("/")
def hello():
	return "index"

@app.route("/key/<keyword>")
def search(keyword):
	return doc.get(keyword)

if __name__ == '__main__':
	app.run(debug=True,port=8888,host="0.0.0.0")