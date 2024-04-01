# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Главная страница Интернет магазина</h1>'
                  '<p class="cool-12 text-monospace text-center">Далее идет перечень товаров</p>')
    context = {'text': _text_info, 'title': 'Главная страница'}
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Страница о нас</h1>'
                  '<p class="cool-12 text-monospace text-center">Информация о нас</p>')
    context = {'text': _text_info, 'title': 'О Нас'}
    return render_template('about.html', **context)

@app.route('/contacts/')
def contacts():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Страница Контактов</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете связаться с нами</p>')
    context = {'text': _text_info, 'title': 'Наши контакты'}
    return render_template('contacts.html', **context)


@app.route('/clothes/')
def clothes():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Страница Одежды</h1>'
                  '<p class="cool-12 text-monospace text-center">Перечень Одежды</p>')
    context = {'text': _text_info, 'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Страница Обуви</h1>'
                  '<p class="cool-12 text-monospace text-center">Перечень Обуви</p>')
    context = {'text': _text_info, 'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Страница Курток</h1>'
                  '<p class="cool-12 text-monospace text-center">Перечень Курток</p>')
    context = {'text': _text_info, 'title': 'Куртки'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)