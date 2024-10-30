from flask import Flask, render_template
from datetime import datetime, timedelta

next_saturday = Flask(__name__)

def time_until_saturday():
    today = datetime.now()
    days_until_saturday = 5 - today.weekday()
    if days_until_saturday <= 0:
        days_until_saturday += 7
    next_saturday = today + timedelta(days=days_until_saturday)
    return next_saturday.strftime("%A, %d %B %Y")

@next_saturday.route('/')
def index():
    next_saturday = time_until_saturday()
    return render_template('index.html', next_saturday=next_saturday)

if __name__ == '__main__':
    next_saturday.run()
