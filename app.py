from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final'
app.config['SECRET_KEY'] = 'team7'

db = SQLAlchemy(app)

class contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    qc = db.Column(db.String(500), nullable=False)

def __init__(self, name, email, qc):
    self.name = name
    self.email = email
    self.qc = qc

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forums')
def forums():
    return render_template('forums.html')

@app.route('/business')
def business():
    return render_template('business.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/social-sciences-and-history')
def ssh():
    return render_template('ssh.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/biological-and-biomedical-sciences')
def bbs():
    return render_template('bbs.html')

@app.route('/psychology')
def psychology():
    return render_template('psychology.html')

@app.route('/computer-and-information-sciences')
def cis():
    return render_template('cis.html')

@app.route('/visual-and-performing-arts')
def vpa():
    return render_template('vpa.html')

@app.route('/communication-and-journalism')
def cj():
    return render_template('cj.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contacted')
def contacted():
    return render_template('contacted.html', contacts = contacts.query.all())

@app.route('/contact-us', methods=['GET', 'POST'])
def contact_confirmation():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['qc']:
            flash('Please enter all fields', 'error')
        else:
            member = contacts(name = request.form['name'], email = request.form['email'], qc = request.form['qc'])

            db.session.add(member)
            db.session.commit()
            return redirect(url_for('contacted'))
    return render_template('contact_us.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

if __name__ == "__main__":
    app.run(debug=True)