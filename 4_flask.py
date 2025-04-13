import numpy as np
from flask import Flask, render_template, request
from PIL import Image
import joblib

app = Flask(__name__)

model = joblib.load('mnist_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == ('POST'):
        file = request.files['file'] # Odbieramy plik

        img = Image.open(file).convert('L') # Konwertujemy obraz na skalę szarości
        img = img.resize((28, 28)) # Zmieniamy rozmiar do 28x28 pikseli

        img_array = np.array(img) # Przekształcamy obraz do wektora

        print(img_array)

    return render_template('digit.html')

if __name__ == '__main__':
    app.run(debug=True)