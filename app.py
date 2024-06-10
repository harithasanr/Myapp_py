from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "AWS Code Pipeline:'Hello_python' "


if __name__=='__main__':
    app.run(debug=False, port=5000)
