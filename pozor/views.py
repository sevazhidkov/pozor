import os

from flask import render_template, request

from . import app
from .db import add_pozor, list_pozor, get_pozor_rating


@app.route('/pozor/')
def pozor_desk():
    current_desk = list_pozor()
    return render_template('pozor.html', desk=current_desk)


@app.route('/pozor/rating/')
def pozor_rating():
    rating = get_pozor_rating()
    return render_template('pozor-rating.html', rating=rating)


@app.route('/pozor/add', methods=['GET', 'POST'])
def pozor_new():
    if request.method == 'POST':
        params = dict(request.form)
        if ('name' not in params or
                'action' not in params or
                'code' not in params):
            return render_template('new-pozor.html', message='Не все поля заполнены')
        if request.form['code'] != os.environ['SECRET_WORD']:
            return render_template('new-pozor.html', message='Неправильный секретный код')
        add_pozor({'name': request.form['name'], 'action': request.form['action']})
        return render_template('new-pozor.html', message='Добавлено!')
    return render_template('new-pozor.html')
