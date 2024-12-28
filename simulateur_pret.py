import streamlit as st

def simulateur_pret(taux_annuel, montant, duree_annees):
    # Conversion du taux annuel en taux mensuel
    taux_mensuel = taux_annuel / 12 / 100
    # Nombre total de mensualités
    nombre_mensualites = duree_annees * 12
    # Calcul de la mensualité
    mensualite = (montant * taux_mensuel) / (1 - (1 + taux_mensuel) ** -nombre_mensualites)
    return mensualite

def main():
    st.title("Simulateur de Prêt")

    st.sidebar.header("Paramètres du prêt")

    # Entrées utilisateur
    taux_annuel = st.sidebar.number_input("Taux annuel (%)", min_value=0.0, max_value=100.0, value=4.2, step=0.1)
    montant = st.sidebar.number_input("Montant du prêt (€)", min_value=0, value=300000, step=1000)
    duree_annees = st.sidebar.number_input("Durée du prêt (années)", min_value=1, max_value=50, value=25, step=1)

    if st.sidebar.button("Calculer la mensualité"):
        # Calcul de la mensualité
        mensualite = simulateur_pret(taux_annuel, montant, duree_annees)
        st.write(f"### La mensualité est de : {mensualite:.2f} €")

if __name__ == "__main__":
    main()
