#Assignment 3.py


# 1

a=1/0

# 2

try:
    a=1/0
except:
    print("illegal operation kinda")


# 3

 # guess, no coz indent?

try:
    x=1
finally:
    print("finally")

 # works with indent, not without

# 4

# not-syntax errors
# ctrl-c
# system-level stuff, inc system exit


# 5

# except

try:
    print(goosemoose)
except:
    print("no goosemoose found")
finally:
    print("finally")

# you can catch exceptions that you actually want, like ctrl+c

#6

## except IOError will catch file read/write issues etc
## except zerodivisionerror catches diving by zero only

## seems best to use except type followed by except exception:

#7 + 8

with open("words.txt", "w") as file:
    file.write("Adam Beedell")
    file.close

#9 

with open("words.txt", "r") as file:
    contents = file.read()
    print(contents)
    file.close()
    #print(file.read())

#10

hebrew = """מה זה, לעזעזאל, לורם איפסום?
לורם איפסום הוא כינוי לטקסט חסר משמעות לחלוטין - הנקרא לפעמים גם דמי טקסט או ג'יבריש - ומיועד להיות ממוקם בסקיצות עיצוביות - של עלונים, מגזינים, מודעות, אתרי אינטרנט וכו' - במקום הטקסט האמיתי הסופי - עד שיהיה טקסט אמיתי.
"""

with open("words.txt", "w") as file:
    file.write(hebrew)
    #file.close

### unicode error, so need to set that somewhere

with open("hebrew.txt", "w", encoding="utf-8") as file:
    file.write(hebrew)
    #print(file.read())
    #file.close

with open("hebrew.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)
    #file.close() - not needed with using with

### some significant fucking aroud with virtual environments here

savedthiselsewhere = """

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ""<p>Do register first on a clean run</p>
    <p><a href="./content">content</p>
    <p><a href="./register">register</p>""

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
@
"""

### python -m flask --app FlaskApp run --port 30000


#technically 3 routes but wanted that to be navigateable