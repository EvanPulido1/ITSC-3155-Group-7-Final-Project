# Clean up all html files
# Finish laying out remaining pages
# Code the forms and implement them

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/forums')
def forums():
    return render_template('forums.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

if __name__ == "__main__":
    app.run(debug=True)