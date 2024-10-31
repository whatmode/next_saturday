from flask import Flask, render_template
from datetime import datetime, timedelta

next_saturday = Flask(__name__)

def time_until_saturday():
    today = datetime.now()
    weekday = today.weekday()

    if weekday == 0:  # Monday
        return 5
    elif weekday == 1:  # Tuesday
        return 4
    elif weekday == 2:  # Wednesday
        return 3
    elif weekday == 3:  # Thursday
        return 2
    elif weekday == 4:  # Friday
        return 1
    elif weekday == 5:  # Saturday
        return 7
    elif weekday == 6:  # Sunday
        return 6

@next_saturday.route('/')
def index():
    next_saturday = time_until_saturday()
    return render_template('index.html', next_saturday=next_saturday)

if __name__ == '__main__':
    next_saturday.run()
