import os
from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://github.com/fxh32/partify")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)