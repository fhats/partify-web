import os
from flask import Flask, redirect
app = Flask(__name__)

base_url = "https://github.com/fxh32/partify/"

@app.route("/")
def hello():
    return redirect(base_url + "wiki")

@app.route("/install")
def install():
    return redirect(base_url + "wiki/Installation")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
