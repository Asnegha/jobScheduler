from flask import Flask, render_template
# import pandas as pd
# from pylab import *
# import matplotlib
# import matplotlib.pyplot as plt
# import gurobipy as gp
# from gurobipy import GRB
# import numpy as np



app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)