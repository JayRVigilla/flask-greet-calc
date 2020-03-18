from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"""
        <html>
            <body>
                <h1>{operations.add(a, b)}</h1>
            </body>
        <html>
    """

@app.route('/sub')
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"""
        <html>
            <body>
                <h1>{operations.sub(a, b)}</h1>
            </body>
        <html>
    """

@app.route('/mult')
def mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"""
        <html>
            <body>
                <h1>{operations.mult(a, b)}</h1>
            </body>
        <html>
    """

@app.route('/div')
def div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"""
        <html>
            <body>
                <h1>{operations.div(a, b)}</h1>
            </body>
        <html>
    """

@app.route('/math/<operation>')
def do_math(operation):
    OPERATION = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

    return OPERATION.get(operation)()