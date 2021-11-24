from flask import render_template
from app import app
from modules.calculator import *

@app.route('/add/<index_1>/<index_2>')
def add_url(index_1, index_2):
    result = add(index_1, index_2)
    return render_template('result_page.html', result=result)

@app.route('/subtract/<index_1>/<index_2>')
def subtract_url(index_1, index_2):
    result = subtract(index_1, index_2)
    return render_template('result_page.html', result=result)

@app.route('/multiply/<index_1>/<index_2>')
def multiply_url(index_1, index_2):
    result = multiply(index_1, index_2)
    return render_template('result_page.html', result=result)

@app.route('/divide/<index_1>/<index_2>')
def divide_url(index_1, index_2):
    result = divide(index_1, index_2)
    return render_template('result_page.html', result=result)