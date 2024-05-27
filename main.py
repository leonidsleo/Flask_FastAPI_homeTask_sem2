"""Задание №9
📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты."""

from flask import Flask, render_template, request, redirect, url_for
from flask import make_response


app = Flask(__name__)


@app.post('/')
def index_post():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response(redirect('welcom'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response

@app.get('/')
def index_get():
    return render_template('index.html')

@app.route('/welcom/')
def welcom():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('welcom.html', name=user_name)
    return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)