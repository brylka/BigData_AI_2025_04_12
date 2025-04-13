from flask import Flask, render_template
import joblib

app = Flask(__name__)

model = joblib.load('mnist_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():

    # logika rozpoznawania cyfr

    return render_template('digit.html')

if __name__ == '__main__':
    app.run(debug=True)