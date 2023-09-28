# Importation des bibliothèques nécessaires
import pandas as pd
from io import BytesIO
import plotly.express as px
import streamlit as st
import folium
import streamlit_folium as st_folium
from streamlit_folium import folium_static
import geopandas as gpd
from folium import plugins

# Chargement des données géospatiales des régions françaises à partir du fichier GeoJSON
geojson_path = "C:/Users/alken/OneDrive/Bureau/advanced programming/dashboardtest/regions.geojson"
geojson = gpd.read_file(geojson_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Real estate: Data and Trends", page_icon=":houses:", layout="wide")

# Spécification du chemin vers le fichier CSV de données immobilières
csv_file_path = "C:/Users/alken/OneDrive/Bureau/advanced programming/Data_sans_description.csv"

# Lecture du fichier CSV dans un DataFrame
df = pd.read_csv(csv_file_path)

# Affichage d'un texte d'accueil dans la barre latérale
multi = '''Welcome to our Real Estate: Data and Trends Dashboard! Here, you will find interactive charts, figures, and a map to closely monitor the French real estate market. Explore and stay informed to make informed decisions.'''
st.sidebar.markdown(multi)

# Configuration du panneau latéral pour la sélection des filtres
st.sidebar.header("Filter:")

# Sélection de la région
region = st.sidebar.multiselect(
    "Select one of the regions:",
    options=df["REGION"].dropna().unique(),
    default="Grand Est"
)

# Sélection du nombre de pièces
pieces = st.sidebar.multiselect(
    "Select the number of rooms:", 
    options=df["Pieces"].dropna().unique()
)
 
# Sélection de la plage de prix à l'aide d'un curseur
prix = st.sidebar.slider(
    'Select a range of price',
    min_value=17500,
    max_value=3590000,
    value = [17500, 3590000],
    step=1000
)

# Filtrage des données en fonction des critères sélectionnés
df_selection=df.query(
    "REGION==@region & Pieces == @pieces & @prix[0] <= Prix <= @prix[1]")

# Vérification si le DataFrame filtré est vide
if df_selection.empty:
    st.warning("No available data !")
    st.stop()  # Arrêt de l'exécution de l'application

# Sélection du format de visualisation à partir d'une liste déroulante
select = st.sidebar.selectbox('Choose your visualization format: ', ['Histogram', 'Map of France', 'Data table'], key='2')

# Début de la page principale
st.title(":house: Real Estate: Data and Trends")
st.markdown("##")

# Affichage des principaux indicateurs
nb_annonces = int(df_selection["Numero"].count())
prixm = round(df_selection["Prix moyen du metre carre"].mean(), 1)
moinscher = round(df_selection["Prix"].min(), 2)

# Fonction pour obtenir le titre de la meilleure opportunité
def get_titre(moinscher):
    for index, row in df_selection.iterrows():
        if row["Prix"] == moinscher:
            return row["Titre"]
    return None

titre = get_titre(moinscher)

# Fonction pour obtenir le prix par mètre carré de la meilleure opportunité
def get_pappart(moinscher):
    for index, row in df_selection.iterrows():
        if row["Prix"] == moinscher:
            return row["Prix du metre carre"]
    return None

pappart = round(get_pappart(moinscher), 2)

# Affichage des KPIs dans 4 colonnes
left_column, middle_left_column, middle_right_column, right_column = st.columns(4)
with left_column:
    st.markdown("<h6>Number of listings :</h6>", unsafe_allow_html=True)
    st.subheader(f"{nb_annonces} :1234:")
with middle_left_column:
    st.markdown("<h6>Price per meter square in this region(s) :</h6>", unsafe_allow_html=True)
    st.subheader(f"{prixm} :euro:")
with middle_right_column:
    st.markdown("<h6>Best opportunity :</h6>", unsafe_allow_html=True)
    st.subheader(f"Prix : {moinscher} :euro:  {titre}")
with right_column:
    st.markdown("<h6>Its price per meter square :  </h6>", unsafe_allow_html=True)
    st.subheader(f"{pappart} :euro:")

# Ligne de séparation
st.markdown("""---""")

# Choix de la visualisation en fonction de la sélection
if select == "Histogram":

    # Création d'un histogramme pour les annonces par région
    annonces_par_region = df_selection.groupby(by=["REGION"])[["Numero"]].count()
    fig_annonces_par_region = px.bar(
        annonces_par_region,
        x=annonces_par_region.index,
        y="Numero",
        title="<b>Listings per region</b>",
        color_discrete_sequence=["#0083B8"] * len(annonces_par_region),
        template="plotly_white",
    )
    fig_annonces_par_region.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    # Création d'un histogramme pour le prix moyen au mètre carré par région
    prix_metre_carre_region = df_selection.groupby(by=["REGION"])[["Prix moyen du metre carre"]].mean()
    fig_prix_metre_carre = px.bar(
        prix_metre_carre_region,
        x="Prix moyen du metre carre",
        y=prix_metre_carre_region.index,
        orientation="h",
        title="<b>Price for meter square in this region</b>",
        color_discrete_sequence=["#0083B8"] * len(prix_metre_carre_region),
        template="plotly_white",
    )
    fig_prix_metre_carre.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    # Affichage des histogrammes dans deux colonnes
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_annonces_par_region, use_container_width=True)
    right_column.plotly_chart(fig_prix_metre_carre, use_container_width=True)
    
elif select == 'Map of France':

    # Création d'une carte de la France avec des indicateurs géospatiaux
    st.title("Map of France \U0001F1EB\U0001F1F7")
    initialize_map = folium.Map(location=[46.603354, 1.888334], zoom_start=5, tiles='CartoDB positron')

    # Lecture des données géospatiales supplémentaires
    dfdeux = gpd.read_file("C:/Users/alken/OneDrive/Bureau/advanced programming/dashboardtest/regions_fusionnees.geojson")

    # Création d'un choroplèthe sur la carte
    add_choropleth = folium.Choropleth(
        geo_data=dfdeux,
        name='choropleth',
        data=dfdeux,
        columns=['nom', 'Prix moyen du metre carre'],
        key_on='feature.properties.nom',
        fill_color='YlOrRd',
        line_opacity=1,
        highlight=True
    ).add_to(initialize_map)

    # Ajout de tooltips aux régions sur la carte
    add_choropleth.geojson.add_child(folium.features.GeoJsonTooltip(["nom", "Prix moyen du metre carre"]))

    # Ajout d'un marqueur personnalisé sur la carte
    folium.Marker(
        location=[48.584, 7.756],
        tooltip="PEGE",
        popup="PEGE",
        icon=folium.Icon(icon="cloud"),
    ).add_to(initialize_map)

    # Affichage statique de la carte dans Streamlit
    st_folium.folium_static(initialize_map)
    
else: 
    # Affichage du DataFrame filtré sous forme de tableau de données
    st.dataframe(df_selection)

# Masquage des styles Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

