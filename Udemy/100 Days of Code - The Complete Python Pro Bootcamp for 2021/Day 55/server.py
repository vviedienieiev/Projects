from flask import Flask
import random

app = Flask(__name__)
target_number = random.randint(0,9)

def make_bold(fun):
    def wrapper():
        return '<b>'+fun()+'</b>'
    return wrapper


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9<h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def greet(number):
    if number < target_number:
        return f'<h1 style="color:red">The number is too small</h1>'\
                '<img src="https://media.giphy.com/media/3o7TKr3nzbh5WgCFxe/giphy.gif">'
    elif number > target_number:
        return f'<h1 style="color:darkblue">The number is too high</h1>' \
               '<img src="https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif">'
    return f'<h1 style="color:darkgreen">You guessed the number</h1>' \
               '<img src="https://media.giphy.com/media/gd0Dqg6rYhttBVCZqd/giphy.gif">'





if __name__ == '__main__':
    app.run(debug=True)