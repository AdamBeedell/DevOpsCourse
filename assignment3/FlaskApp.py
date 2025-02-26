#FlaskApp


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Do register first on a clean run</p>
    <p><a href="./content">content</p>
    <p><a href="./register">register</p>"""

@app.route("/content")
def readcontent():
    with open("words.txt", "r") as file:
        contents = file.read()
        return contents

@app.route("/register")
def writecontent():
    with open("words.txt", "w") as file:
        file.write("Adam Beedell")
        return "success", 201
