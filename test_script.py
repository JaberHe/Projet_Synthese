import pandas as pd
import random



def calculer_taille(age):   
    taille = age * random.uniform(1, 2)
    taille_f = int(taille)
    return taille_f

donnees = {'age': [random.randint(1, 30) for i in range(10000)]}

df = pd.DataFrame(donnees)

df['taille'] = df['age'].apply(calculer_taille)

habitats = ['Plaine', 'Grotte', 'Montagne', 'Foret', 'Marecage', 'Desert']
sexe = ['femelle', 'male']

df['Habitat'] = [random.choice(habitats) for _ in range(len(df))]
df['sexe'] = [random.choice(sexe) for _ in range(len(df))]


df.to_csv('test.csv', index=False)
