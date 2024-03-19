"""
This script runs the FlaskWebProjectTest1 application using a development server.
"""

from os import environ
from FlaskWebProjectTest1 import create_app

app =create_app() 

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)