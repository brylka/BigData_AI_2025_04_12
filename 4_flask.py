import numpy as np
from flask import Flask, render_template, request
from PIL import Image
import joblib

app = Flask(__name__)

model = joblib.load('mnist_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == ('POST'):
        file = request.files['file'] # Odbieramy plik

        img = Image.open(file).convert('L') # Konwertujemy obraz na skalę szarości
        img = img.resize((28, 28)) # Zmieniamy rozmiar do 28x28 pikseli

        img_array = np.array(img) # Przekształcamy obraz do wektora

        binary_image = (img_array <= 127).astype(int)

        # # Wyświetla cyfrę 0 i 1
        # print("\nReprezentacja binarna (0 i 1):")
        # for row in binary_image:
        #     print(' '.join(map(str, row)))
        #
        # # Wyświetlanie cyfry w bardziej czytelnej formie
        # print("\nWizualizacja w terminalu (# dla 1, spacja dla 0):")
        # for row in binary_image:
        #     line = ''
        #     for pixel in row:
        #         if pixel == 1:
        #             line += '#'
        #         else:
        #             line += ' '
        #     print(line)

        # Przekształć obraz do wektora dla modelu
        img_vector = (255 - img_array).reshape(1,-1) / 255.0

        # Przewidywanie cyfry
        prediction = model.predict(img_vector)[0]

    return render_template('digit.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)