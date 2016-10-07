from flask import Flask,render_template,url_for
from Doc import Doc
#提供接口
app = Flask(__name__)
doc = Doc()

app.config['TEMPLATES_AUTO_RELOAD'] = False 
#前端页面
#搜索关键词后，出现符合条件的题号？
@app.route("/")
def hello():
	url_for('static', filename='angular.min.js')#amazeui.min.css
	url_for('static', filename='amazeui.min.css')#amazeui.min.css
	return render_template("index.html",code=" {{x}}",tips="{{tips}}") 
 
@app.route("/key/<keyword>")
def search(keyword):
	return doc.get(keyword)


if __name__ == '__main__':
	app.run(debug=True,port=8888,host="0.0.0.0")


#部署