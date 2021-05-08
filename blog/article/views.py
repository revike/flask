from flask import Blueprint, render_template, redirect

article = Blueprint('article', __name__,
                    url_prefix='/articles', static_folder='../static')

ARTICLES = [
    {
        'id': 1,
        'title': 'some title #1',
        'text': 'some text #1',
        'author': {
            'name': 'Alice',
            'id': 1,
        },
    },
    {
        'id': 2,
        'title': 'some title #2',
        'text': 'some text #2',
        'author': {
            'name': 'John',
            'id': 2,
        },
    }
]


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
        title_body='articles:',
        title='article list'
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_pk = ARTICLES[pk-1]
    except IndexError:
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        title_body=article_pk['title'],
        text=article_pk['text'],
        author=article_pk['author'],
        title=f'article - {article_pk["title"]}'
    )
