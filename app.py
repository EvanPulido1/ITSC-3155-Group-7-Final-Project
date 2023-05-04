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

class answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(200), nullable=False)

def __init__(self, answer):
    self.answer = answer

class answers2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer2 = db.Column(db.String(200), nullable=False)

def __init__(self, answer2):
    self.answer2 = answer2

class answers3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer3 = db.Column(db.String(200), nullable=False)

def __init__(self, answer3):
    self.answer3 = answer3

class answers4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer4 = db.Column(db.String(200), nullable=False)

def __init__(self, answer4):
    self.answer4 = answer4

class answers5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer5 = db.Column(db.String(200), nullable=False)

def __init__(self, answer5):
    self.answer5 = answer5

class answers6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer6 = db.Column(db.String(200), nullable=False)

def __init__(self, answer6):
    self.answer6 = answer6

class answers7(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer7 = db.Column(db.String(200), nullable=False)

def __init__(self, answer7):
    self.answer7 = answer7

class answers8(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer8 = db.Column(db.String(200), nullable=False)

def __init__(self, answer8):
    self.answer8 = answer8

class answers9(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer9 = db.Column(db.String(200), nullable=False)

def __init__(self, answer9):
    self.answer9 = answer9

class answers10(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer10 = db.Column(db.String(200), nullable=False)

def __init__(self, answer10):
    self.answer10 = answer10

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
    return render_template('business.html', answers = answers.query.all())

@app.route('/health')
def health():
    return render_template('health.html', answers2 = answers2.query.all())

@app.route('/social-sciences-and-history')
def ssh():
    return render_template('ssh.html', answers3 = answers3.query.all())

@app.route('/engineering')
def engineering():
    return render_template('engineering.html', answers4 = answers4.query.all())

@app.route('/biological-and-biomedical-sciences')
def bbs():
    return render_template('bbs.html', answers5 = answers5.query.all())

@app.route('/psychology')
def psychology():
    return render_template('psychology.html', answers6 = answers6.query.all())

@app.route('/computer-and-information-sciences')
def cis():
    return render_template('cis.html', answers7 = answers7.query.all())

@app.route('/visual-and-performing-arts')
def vpa():
    return render_template('vpa.html', answers8 = answers8.query.all())

@app.route('/communication-and-journalism')
def cj():
    return render_template('cj.html', answers9 = answers9.query.all())

@app.route('/education')
def education():
    return render_template('education.html', answers10 = answers10.query.all())

@app.route('/business-reply-form', methods=['GET', 'POST'])
def business_reply_form():
    if request.method == 'POST':
        if not request.form['answer']:
            flash('Please enter all fields', 'error')
        else:
            answer = answers(answer = request.form['answer'])

            db.session.add(answer)
            db.session.commit()
            return redirect(url_for('business'))
    return render_template('business_reply.html')

@app.route('/health-reply-form', methods=['GET', 'POST'])
def health_reply_form():
    if request.method == 'POST':
        if not request.form['answer2']:
            flash('Please enter all fields', 'error')
        else:
            answer2 = answers2(answer2 = request.form['answer2'])

            db.session.add(answer2)
            db.session.commit()
            return redirect(url_for('health'))
    return render_template('health_reply.html')

@app.route('/ssh-reply-form', methods=['GET', 'POST'])
def ssh_reply_form():
    if request.method == 'POST':
        if not request.form['answer3']:
            flash('Please enter all fields', 'error')
        else:
            answer3 = answers3(answer3 = request.form['answer3'])

            db.session.add(answer3)
            db.session.commit()
            return redirect(url_for('ssh'))
    return render_template('ssh_reply.html')

@app.route('/engineering-reply-form', methods=['GET', 'POST'])
def engineering_reply_form():
    if request.method == 'POST':
        if not request.form['answer4']:
            flash('Please enter all fields', 'error')
        else:
            answer4 = answers4(answer4 = request.form['answer4'])

            db.session.add(answer4)
            db.session.commit()
            return redirect(url_for('engineering'))
    return render_template('engineering_reply.html')

@app.route('/bbs-reply-form', methods=['GET', 'POST'])
def bbs_reply_form():
    if request.method == 'POST':
        if not request.form['answer5']:
            flash('Please enter all fields', 'error')
        else:
            answer5 = answers5(answer5 = request.form['answer5'])

            db.session.add(answer5)
            db.session.commit()
            return redirect(url_for('bbs'))
    return render_template('bbs_reply.html')

@app.route('/psychology-reply-form', methods=['GET', 'POST'])
def psychology_reply_form():
    if request.method == 'POST':
        if not request.form['answer6']:
            flash('Please enter all fields', 'error')
        else:
            answer6 = answers6(answer6 = request.form['answer6'])

            db.session.add(answer6)
            db.session.commit()
            return redirect(url_for('psychology'))
    return render_template('psychology_reply.html')

@app.route('/cis-reply-form', methods=['GET', 'POST'])
def cis_reply_form():
    if request.method == 'POST':
        if not request.form['answer7']:
            flash('Please enter all fields', 'error')
        else:
            answer7 = answers7(answer7 = request.form['answer7'])

            db.session.add(answer7)
            db.session.commit()
            return redirect(url_for('cis'))
    return render_template('cis_reply.html')

@app.route('/vpa-reply-form', methods=['GET', 'POST'])
def vpa_reply_form():
    if request.method == 'POST':
        if not request.form['answer8']:
            flash('Please enter all fields', 'error')
        else:
            answer8 = answers8(answer8 = request.form['answer8'])

            db.session.add(answer8)
            db.session.commit()
            return redirect(url_for('vpa'))
    return render_template('vpa_reply.html')

@app.route('/cj-reply-form', methods=['GET', 'POST'])
def cj_reply_form():
    if request.method == 'POST':
        if not request.form['answer9']:
            flash('Please enter all fields', 'error')
        else:
            answer9 = answers9(answer9 = request.form['answer9'])

            db.session.add(answer9)
            db.session.commit()
            return redirect(url_for('cj'))
    return render_template('cj_reply.html')

@app.route('/education-reply-form', methods=['GET', 'POST'])
def education_reply_form():
    if request.method == 'POST':
        if not request.form['answer10']:
            flash('Please enter all fields', 'error')
        else:
            answer10 = answers10(answer10 = request.form['answer10'])

            db.session.add(answer10)
            db.session.commit()
            return redirect(url_for('education'))
    return render_template('education_reply.html')

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