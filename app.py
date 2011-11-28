import os
from flask import Flask, redirect
app = Flask(__name__)

redirect_base = "https://github.com/fxh32/partify/"

@app.route("/")
def hello():
    return redirect(redirect_base + 'wiki')

@app.route("/install")
def install():
    return redirect(redirect_base + 'wiki/install')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
