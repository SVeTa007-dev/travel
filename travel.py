from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Commentari(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commenta = db.Column(db.Text, nullable = False)
    email = db.Column(db.string(100), nullable=False)

    def __repr__(self):
        return'<Commentari %r>' % self.id

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