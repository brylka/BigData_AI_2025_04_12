from flask import Flask, render_template
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('digit.html')

if __name__ == '__main__':
    app.run(debug=True)