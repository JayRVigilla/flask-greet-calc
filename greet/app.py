from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Returns 'welcome'"""

    return """
        <html>
            <body>
                <h1>Welcome!</h1>
            </body>
        </html>
    """

@app.route('/welcome/home')
def say_welcome_home():
    """Returns 'welcome home'"""

    return """
        <html>
            <body>
                <h1>Welcome home!</h1>
            </body>
        </html>
    """

@app.route('/welcome/back')
def say_welcome_back():
    """Returns 'welcome back'"""

    return """
        <html>
            <body>
                <h1>Welcome back!</h1>
            </body>
        </html>
    """