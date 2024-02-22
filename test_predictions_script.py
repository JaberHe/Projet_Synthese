import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Charger les données
donnees = pd.read_csv('donnees.csv')
test = pd.read_csv('test.csv')

# Séparer les caractéristiques et les étiquettes dans donnees
X_train = donnees[['age', 'taille', 'Habitat', 'sexe']]
y_train = donnees['stade_evolution']

# Transformer les caractéristiques catégorielles en variables indicatrices
X_train = pd.get_dummies(X_train)

# Séparation des données en données d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Initialisation et entraînement du modèle (Random Forest Classifier ici)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prédiction sur les données de validation
y_pred = model.predict(X_val)

# Évaluation du modèle
accuracy = accuracy_score(y_val, y_pred)
print("Accuracy:", accuracy)

# Prédiction sur les données de test
X_test = test[['age', 'taille', 'Habitat', 'sexe']]
X_test = pd.get_dummies(X_test)
predictions = model.predict(X_test)

# Ajout des prédictions à la base de données 'test'
test['evolution_predite'] = predictions

# Sauvegarder les prédictions dans un nouveau fichier CSV
test.to_csv('test_predictions.csv', index=False)
