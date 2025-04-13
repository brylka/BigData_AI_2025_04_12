from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_property = {
            'MedInc':       float(request.form['MedInc']),
            'HouseAge':     float(request.form['HouseAge']),
            'AveRooms':     float(request.form['AveRooms']),
            'AveBedrms':    float(request.form['AveBedrms']),
            'Population':   float(request.form['Population']),
            'AveOccup':     float(request.form['AveOccup']),
            'Latitude':     float(request.form['Latitude']),
            'Longitude':    float(request.form['Longitude'])
        }

    return render_template('housing.html')

if __name__ == '__main__':
    app.run(debug=True)
