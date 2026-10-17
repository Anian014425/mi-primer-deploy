import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

# 1. Dataset integrado de Seaborn

df = sns.load_dataset("penguins").dropna()

 

# 2. Operaciones rápidas con Pandas

resumen = df.groupby("species")["body_mass_g"].agg(["mean", "count"])

print("--- Resumen de masa corporal (g) ---")

print(resumen.round(1))

 

# 3. Visualización con Seaborn

sns.set_theme(style="whitegrid")

sns.scatterplot(

    data=df,

    x="flipper_length_mm",

    y="body_mass_g",

    hue="species",

    style="sex",

    palette="viridis",

)

 

plt.title("Masa corporal vs Longitud de aleta")

plt.xlabel("Largo de aleta (mm)")

plt.ylabel("Peso (g)")

plt.tight_layout()

plt.show()