import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.markdown(
    """
    <div style='text-align:center'>
    <h1> Analyse des données et statistiques descriptives </h1>
    <p style=color:blue> Cas des logements en Californie</p>
    </div>
    """, unsafe_allow_html=True
)


url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

try:
    donnees = pd.read_csv(url)
except Exception as e:
    st.error(f"Erreur de lecture : {e}")
    donnees = None


menu = st.sidebar.selectbox("Navigation", [
    "Chargement",
    "Aperçu des données",
    "Statistiques descriptives",
    "Corrélation",
    "Visualisation"
])


if donnees is not None:

    if menu == "Chargement":
        st.write("Aperçu complet des données")
        st.dataframe(donnees)

    elif menu == "Aperçu des données":
        st.subheader("Afficher les 5 premières lignes")
        st.dataframe(donnees.head())

        st.subheader("Afficher les 5 dernières lignes")
        st.dataframe(donnees.tail())

        st.subheader("Distribution des types de quartiers (ocean_proximity)")
        repartition = donnees['ocean_proximity'].value_counts()
        st.bar_chart(repartition)

    elif menu == "Statistiques descriptives":
        st.subheader("Statistiques descriptives")
        st.write(donnees.describe())

    elif menu == "Corrélation":
        st.subheader("Analyse de la corrélation (variables numériques uniquement)")
        donnees_numeriques = donnees.select_dtypes(include=[np.number])
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(donnees_numeriques.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)

    elif menu == "Visualisation":
        st.subheader("Visualisation : Prix en fonction d'une variable")
        variables_possibles = [col for col in donnees.columns if col != 'median_house_value']
        variable = st.selectbox("Choisissez une variable :", variables_possibles)

        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=donnees, x=variable, y='median_house_value', ax=ax2)
        st.pyplot(fig2)

else:
    st.warning("Les données n'ont pas pu être chargées. Veuillez vérifier l'URL.")
