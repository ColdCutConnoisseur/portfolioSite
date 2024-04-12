import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'portfolio_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

Bootstrap(app)

class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.Text)
    review_text = db.Column(db.Text)
    review_source = db.Column(db.String(64))
    review_score = db.Column(db.Float)

    #def __repr__(self):
    #    return "%s --%s" % self.review_text, self.review_source


@app.route('/')
def index():
    return render_template("introduction.html")

@app.route('/testimonials')
def serve_testimonials():
    all_testimonials = Testimonial.query.all()
    return render_template("testimonials.html", all_testimonials=all_testimonials)

#@app.route('/art-gallery')
#def serve_gallery():
#    return render_template("gallery.html")
