import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Importowanie potrzebnych funkcji z bibliotek sklearn i tensorflow
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input

# Pobieranie zestawu danych dotyczących cen mieszkań w Kalifornii
california_housing = fetch_california_housing()
# Przypisanie danych do zmiennych X (cechy) i y (wartości docelowe)
X, y = california_housing.data, california_housing.target

# Podział danych na zestawy treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicjalizacja StandardScaler do skalowania danych
scaler = StandardScaler()
# Skalowanie danych treningowych
X_train = scaler.fit_transform(X_train)
# Skalowanie danych testowych
X_test = scaler.transform(X_test)

# Tworzenie modelu z użyciem funkcyjnego API Keras
inputs = Input(shape=(X_train.shape[1],))
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
outputs = Dense(1)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Kompilacja modelu z optymalizatorem Adam i funkcją straty mean_squared_error
model.compile(optimizer='adam', loss='mean_squared_error')

# Wyświetlanie podsumowania modelu
model.summary()

# Trenowanie modelu z 100 epokami i walidacją na 10% danych treningowych
history = model.fit(X_train, y_train, epochs=100, validation_split=0.1)

# Wykres funkcji straty dla danych treningowych i walidacyjnych
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
# Zapisujemy wykres
plt.savefig('loss_plot.png')
plt.close()  # Zamykamy figurę, aby zwolnić pamięć

# Przewidywanie wartości dla danych testowych
y_pred = model.predict(X_test)
# Obliczanie błędu średniokwadratowego (MSE) dla danych testowych
mse = tf.keras.losses.MeanSquaredError()
mse_value = mse(y_test, y_pred).numpy()
print(f'Mean squared error: {mse_value}')

# Nowa nieruchomość, dla której chcemy oszacować cenę
new_property = {
    'MedInc': 8.32,
    'HouseAge': 25,
    'AveRooms': 6.23,
    'AveBedrms': 1.01,
    'Population': 1800,
    'AveOccup': 3.5,
    'Latitude': 37.88,
    'Longitude': -122.23
}

# Tworzenie DataFrame z nowymi danymi
new_property_df = pd.DataFrame([new_property])

# Skalowanie danych wejściowych przy użyciu tego samego skalera użytego do trenowania modelu
scaled_new_property = scaler.transform(new_property_df)

# Prognozowanie ceny przy użyciu wytrenowanego modelu
predicted_price = model.predict(scaled_new_property)

# Wypisanie prognozowanej ceny
print(f'Prognozowana cena nieruchomości: {predicted_price[0][0]:.3f} (w jednostkach 100.000 USD)')

# Obliczenie wartości nieruchomości
property_value = predicted_price[0][0] * 100000
# Formatowanie wartości z separatorem
formatted_value = format(property_value, ',.0f').replace(',', '.')
# Wydrukowanie prognozowanej ceny nieruchomości z separatorem
print(f'Prognozowana cena nieruchomości: {formatted_value} dolarów.')

# Informacja o zapisanym wykresie
print("\nWykres funkcji straty został zapisany jako 'loss_plot.png'.")