#Coding a Server - Flask

from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import requests as reqs


app = Flask(__name__) #configuring the server



import pandas as pd
import numpy as np
import pickle

#reading the data

#splitting the dataset

#serving the starting web page to the browser
@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


