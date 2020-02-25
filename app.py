#! /bin/usr/python
import subprocess
from flask import Flask


app = Flask(__name__)

@app.route('/<name>')
def exportDatabase(name):

    # var = "C:/Users/I520493/Downloads/Scripts/"
    # pipe = subprocess.Popen(["perl", "./DBexport.pl", var], stdin=subprocess.PIPE)
    # pipe.stdin.write(var)
    # pipe.stdin.close()
    return "Hello {}".format(name)


if __name__ == "__main__":
    app.run()