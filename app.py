from flask import Flask, render_template

app =Flask(__name__)


@app.route('/')
def homepage():
    return render_template('travel.html')


@app.route('/abouttravel/')
def about():
    return render_template('abouttravel.html')


@app.route('/review/')
def review():
    return render_template('review.html')


if __name__ == '__main__':
    app.run()