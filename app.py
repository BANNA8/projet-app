import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")
st.title("My portfolio")
st.write("bienvenue dans mon portfolio")
st.markdown("---")

with st.sidebar:
    st.image("yd.jpg" , width=200)
    st.title("Yancouba Djitté")
    

menu = st.sidebar.selectbox("", ["Accueil", "Projets", "Contact"])

if menu == "Accueil":
    st.subheader("profil")
    st.write("Je suis un élève ingenieur en agronomie, passionné par l'agriculture durable et les nouvelles technologies appliquées à l'agriculture")

    st.markdown("---")

    st.subheader("parcours")
    st.write("J’ai été au lycée de Médina Wandifa, où j’ai obtenu mon baccalauréat en série S2. Par la suite, j’ai intégré l’École Supérieure Polytechnique de Diamniadio, où je poursuis actuellement mes études supérieures.Je suis en deuxième année dans la filière des sciences agricoles et agroalimentaires.")

    st.markdown("---")

    st.subheader("competences")   

    st.write("""
        Les enseignements de la Licence 1, complétés par mes recherches personnelles, m’ont permis d’acquérir des connaissances solides et pratiques dans plusieurs domaines.
        En agriculture, je maîtrise des notions liées à la nutrition et au développement des plantes, à l’analyse des sols ainsi qu’à la phytosanitaire.
        En informatique, j’ai développé des compétences en développement web.
        Enfin, en gestion, j’ai acquis des bases en organisation et en suivi d’activités.)
        """)
    st.markdown("###Agriculture")
    st.write("Nutrition et développement des plantes")
    st.progress(60)

    st.write("Analyse des sols")
    st.progress(50)

    st.write("phytosanitaire")
    st.progress(40)

    st.markdown("###Informatique")
    st.write("Développement web")
    st.progress(50)

    st.markdown("###Gestion")
    st.write("Gestion de projet")
    st.progress(50)
    st.markdown("---")

elif menu =="Projets":
  st.header("Projets")
  st.write("""
  Voici deux projets importants que j’ai réalisés ou que je développe actuellement dans le domaine agricole et agroalimentaire.
  """)



  st.subheader("Plateforme de commercialisation agricole")

  col1, col2 = st.columns([2, 1])

  with col1:
    st.write("""
    Je développe actuellement une plateforme de vente en ligne destinée aux cultivateurs de ma commune rurale, une zone très reculée où les producteurs rencontrent des difficultés pour écouler leurs produits agricoles après la récolte.

     **Objectif :** faciliter la commercialisation des produits agricoles en connectant directement les producteurs aux restaurants et aux entreprises agroalimentaires du pays.
    """)

    with col2:
     st.image(
        "ky.jpg", 
        use_container_width=True, caption="photo de la plateforme en cours de developpement"
        )

  st.markdown("---")


  st.subheader("Gestion de production agricole familiale")

  col1, col2 = st.columns([2, 1])

  with col1:
    st.write("""
     L’année dernière, j’ai piloté la production agricole de notre exploitation familiale en tant qu’apprenti agronome.  

     La saison s’est bien déroulée avec un rendement supérieur aux attentes grâce à une meilleure organisation et un suivi technique des cultures.
     """)

  with col2:
    st.video(
    "od.mp4", 
    format="video/mp4", start_time=0, width=100
    )
elif menu == "Contact":
  st.header("Contact")    
  st.write("contactez moi pour plus d'information sur mes projets ou pour toute collaboration ")
  st.write("Email:djitteyancouba8@gmail.com")
  st.write("📞Téléphone:+221 77 921 23 27 ")
  st.write("Adresse: Touba Moricounda, Sedhiou, Sénégal")
  






