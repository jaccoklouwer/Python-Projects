from flaskBlog import create_app

'''
when this file is celled the server is started.

The default host is used, which is localhost.
And the default port is used: 5000.
'''

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
