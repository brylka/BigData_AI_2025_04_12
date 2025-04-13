import joblib
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Wczytanie zbioru danych MNIST
print("Wczytuję dane MNIST...")
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data.astype('float32')
y = mnist.target.astype('int')

# Normalizacja danych (skalowanie do przedziału [0,1])
X = X / 255.0

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Inicjalizacja klasyfikatora RandomForest z mniejszą większą drzew dla szybszego treningu
rf = RandomForestClassifier(n_estimators=200, random_state=42)

# Trenowanie modelu
print("Trenuję model...")
rf.fit(X_train, y_train)

print("Zapisanie modelu do pliku...")
joblib.dump(rf, 'mnist_model.pkl')