from flask import Flask
app = Flask("任哥的Flash网站")

@app.route("/")
def index():
    return "欢迎访问任哥的网站"