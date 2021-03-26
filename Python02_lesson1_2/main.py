from flask import Flask, render_template, abort, request, redirect

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'author': 'Petro Petrovich',
        'title': 'Hello world!',
        'text': 'Hello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqwe'
    },
    {
        'id': 2,
        'author': 'Ivan Ivanovich',
        'title': 'World Hello',
        'text': 'World HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld Hello'
    }
]


@app.route('/')
def main_page():
    return render_template('index.html', title='ItStep Blog', articles=articles)


@app.route('/article/<int:id>')
def get_article(id):
    for article in articles:
        if article['id'] == id:
            return render_template('generic.html', article=article)
    abort(404)


@app.route('/about')
def about_page():
    return 'About page!'


@app.route('/create/article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'GET':
        print(render_template('create_article.html'))
        return render_template('create_article.html')
    if request.method == 'POST':
        articles.append({'author': request.form['article_author'],
                         'title': request.form['article_title'],
                         'text': request.form['article_text'],
                         })
        return redirect('/')
    else:
        return 'method not allowed'

    print(f'create article method {request.method}')
    return 'Hello World'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
