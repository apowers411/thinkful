from flask import Flask, render_template, request, redirect, url_for
from tip_calculator import *
from forms import CostForm
import decimal

app = Flask(__name__)      

app.secret_key= 'development key'

@app.route('/', methods=['GET'])
def home():
    form = CostForm()
    return render_template('form.html',form=form)
'''
@app.route('/results', methods=['GET','POST'])
def results():

    if request.method== 'POST':
        meal_info = calculate_meal_costs(form.mealcost.data, .07, form.tipcost.data)
        return render_template('results.html',finalbill=meal_info['total'])
    elif request.method == 'GET':
        return render_template('form.html',form=form)
'''

@app.route('/results', methods=['GET','POST'])
def results():
    form = CostForm()
    error_message={'errors':[]}
    try:
        assert float(request.form['mealcost']) > 0
        mealcost = float(request.form['mealcost'])
    except ValueError:
        error_message['errors'].append('The meal cost must be a number')
    except AssertionError:
        error_message['errors'].append('The meal cost must be greater than 0')

    try:
        assert float(request.form['tipcost']) > 0
        tipcost = float(request.form['tipcost'])
    except ValueError:
        error_message['errors'].append('The tip must be a number')
    except AssertionError:
        error_message['errors'].append('The tip must be greater than 0')

    try:
        result = mealcost*tipcost/100
    except (ValueError, UnboundLocalError):
        return render_template('home.html',error_message=error_message, form=form)

    return render_template('results.html', finalbill=result)


if __name__ == '__main__':
    app.run(debug=True)
