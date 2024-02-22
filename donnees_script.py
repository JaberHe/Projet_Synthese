import pandas as pd
import random



def calculer_taille(age):
    taille = age * random.uniform(1, 2)
    taille_f = int(taille)
    return taille_f

def calcul_facteur_evolution(age, taille, habitat, sexe):
    facteur_age = age/30 #entre 0 et 1
    facteur_taille = taille/60 #entre 0 et 1
    habitats_favorables = ['Plaine', 'Foret', 'Montagne', 'Marecage', 'Grotte', 'Desert','']
    habitats_defavorables = habitats_favorables[::-1]
    facteur_habitat = habitats_defavorables.index(habitat)/6 #ex: index grotte defav = 2 => 2/6 = 0.33 / entre 0 et 1
    facteur_sexe = 1 if sexe == 'femelle' else 0.5 #soit 0.5 soit 1
    facteur_evolution = int(min(facteur_age + facteur_taille + facteur_habitat + facteur_sexe, 3))
    return facteur_evolution

donnees = {'age': [random.randint(1, 30) for i in range(10000)]}

df = pd.DataFrame(donnees)

df['taille'] = df['age'].apply(calculer_taille)

habitats = ['Plaine', 'Grotte', 'Montagne', 'Foret', 'Marecage', 'Desert']
sexe = ['femelle', 'male']

df['Habitat'] = [random.choice(habitats) for _ in range(len(df))]
df['sexe'] = [random.choice(sexe) for _ in range(len(df))]

df['stade_evolution'] = df.apply(lambda row: calcul_facteur_evolution(row['age'], row['taille'], row['Habitat'], row['sexe']), axis=1)

df.to_csv('donnees.csv', index=False)
