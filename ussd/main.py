from adapters.choix.MVola import MVola
from adapters.Choix import Choix
from adapters.MenuPrincipal import MenuPrincipal


def main():
    # Créer MVola
    mvola = MVola("MVOLA")

    # Liste des titres des choix dans MVola
    titres = [
        "Acheter Credit ou Offre Yas",
        "Transferer argent (vers toute destination)",
        "MVola Credit ou Epargne",
        "Retrait d'argent",
        "Paiement Factures & Partenaires",
        "Mon compte",
        "Recevoir de l argent",
        "Banques et Micro-Finances"
    ]

    # Ajouter les choix dans MVola
    for titre in titres:
        mvola.ajouter_option(Choix(titre))

    # Afficher le menu Mvola
    # mvola.afficher_menu()

    # Ajouter MVola dans le menu principal
    menu_principal = MenuPrincipal("YAS et MOI")
    menu_principal.ajouter_option(mvola)
    # Afficher le menu principal
    menu_principal.afficher_menu()


if __name__ == "__main__":
    main()
