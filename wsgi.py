from blog.app import create_app


if __name__ == '__main__':
    app = create_app()
    print('http://127.0.0.1:5000/users/')
    app.run(host='127.0.0.1', debug=True)
