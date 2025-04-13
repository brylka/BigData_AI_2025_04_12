from sklearn.datasets import fetch_openml

# Numer indeksu interesującej nas cyfry
num = 3

# Wczytanie zbioru danych MNIST
print("Wczytuję dane MNIST...")
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data.astype('float32')
y = mnist.target.astype('int')

# Weźmy pierwszą cyfrę z zestawu danych
first_digit = X.iloc[num].values

# Przekształćmy ją do formatu macierzy 28x28
digit_image = first_digit.reshape(28, 28)

# Ustawmy próg konwersji na binarne wartości (0 i 1)
threshold = 127  # Wartości są w zakresie 0-255 przed normalizacją
binary_image = (digit_image > threshold/255.0).astype(int)  # konwersja do 0 i 1

# Wyświetlanie cyfry w postaci binarnej (0 i 1)
print(f"Cyfra: {y.iloc[num]}")
print("\nReprezentacja binarna (0 i 1):")
for row in binary_image:
    print(' '.join(map(str, row)))

# Wyświetlanie cyfry w bardziej czytelnej formie
print("\nWizualizacja w terminalu (# dla 1, spacja dla 0):")
for row in binary_image:
    line = ''
    for pixel in row:
        if pixel == 1:
            line += '#'
        else:
            line += ' '
    print(line)