from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Wczytaj zbiór danych Iris
iris = load_iris()
X = iris.data      # cechy (długość i szerokość działki kielicha oraz płatka)
y = iris.target    # etykiety (gatunki irysów)

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicjalizacja klasyfikatora k-najbliższych sąsiadów
knn = KNeighborsClassifier(n_neighbors=3)

# Trenowanie modelu
knn.fit(X_train, y_train)

# Predykcja na zbiorze testowym
y_pred = knn.predict(X_test)

# Ocena wyników
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print(f"Dokładność: {accuracy:.2f}")
print("Raport klasyfikacji:")
print(report)

# Przykład przewidywania dla nowego kwiatu
# [długość_działki, szerokość_działki, długość_płatka, szerokość_płatka]
nowy_irys = [[5.1, 3.5, 1.4, 0.2]]  # przykładowe wymiary
przewidywany_gatunek = knn.predict(nowy_irys)
print(f"Przewidywany gatunek: {iris.target_names[przewidywany_gatunek[0]]}")