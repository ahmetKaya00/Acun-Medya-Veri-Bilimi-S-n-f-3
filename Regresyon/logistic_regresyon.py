import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


data_classification = {
    "Age": [22,25,47,52,46,56,55,60,62,61],
    "Income": [25000,32000,47000,52000,46000,58000,60000,62000,64000,63000],
    "Purchased": [0,0,1,1,1,1,1,1,1,1]
}

dt_classification = pd.DataFrame(data_classification)

print("Logistic Regresyon Veri Seti:")
print(dt_classification.head())

print("\n Veri Eğitim ve Test Setine Ayrılıyor...\n")

x = dt_classification[["Age","Income"]]
y = dt_classification["Purchased"]

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print(f"Eğitim Seti Boyutu: {x_train.shape}")
print(f"Test Seti Boyutu: {x_test.shape}")

print("\n Lineer Regresyon Modeli Eğitiliyor...\n")

model = LogisticRegression()

model.fit(x_train,y_train)

print("\n Lineer Regresyon Modeli Eğitildi!")
print("Katsayısal:")
print(model.coef_)
print(f"Intercept (b0): {model.intercept_}")

print("\n KNN Modeli Eğitiliyor...")

model_knn = KNeighborsClassifier(n_neighbors=3)

model_knn.fit(x_train,y_train)

print("\n KNN Modeli Eğitildi!")

print("\n KNN Modeli Test Verisi ile tahmin Yapıyor...")

y_pred_knn = model_knn.predict(x_test)

print("\n Gerçek vs Tahmin Edilen Değerler:")
for gerçek, tahmin in zip(y_test,y_pred_knn):
    print(f"Gerçek: {gerçek} -> Tahmin: {tahmin}")

print("\n KNN Modeli Performansı Ölçülüyor...")

accuracy_knn = accuracy_score(y_test,y_pred_knn)

print("\n KNN Modeli Performans Sonuçları:")
print(f"Doğruluk Skoru: {accuracy_knn}")
