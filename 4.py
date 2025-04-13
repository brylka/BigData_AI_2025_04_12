from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Wczytanie zbioru danych MNIST
print("Wczytuję dane MNIST...")
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data.astype('float32')
y = mnist.target.astype('int')

# Normalizacja danych (skalowanie do przedziału [0,1])
X = X / 255.0

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicjalizacja klasyfikatora RandomForest z mniejszą liczbą drzew dla szybszego treningu
rf = RandomForestClassifier(n_estimators=50, random_state=42)

# Trenowanie modelu
print("Trenuję model...")
rf.fit(X_train, y_train)

# Predykcja na zbiorze testowym
print("Testuję model...")
y_pred = rf.predict(X_test)

# Ocena jakości modelu
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność: {accuracy:.4f}")

# Wyświetlenie raportu klasyfikacji
print("\nRaport klasyfikacji:")
print(classification_report(y_test, y_pred))

# Predykcja dla konkretnych przykładów
print("\nPrzykładowe predykcje:")
for i in range(5):
    idx = i * 100  # Bierzemy co 100-ny przykład, żeby mieć różnorodność
    true_label = y_test.iloc[idx]
    pred_label = y_pred[idx]
    print(f"Przykład {i+1}: Prawdziwa cyfra: {true_label}, Przewidywana cyfra: {pred_label}")