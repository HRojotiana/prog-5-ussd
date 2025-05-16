from adapters.choix.MVola import MVola
from adapters.Choix import Choix
from adapters.MenuPrincipal import MenuPrincipal


def main():
    # Créer MVola
    mvola = MVola("MVOLA")

    # Créer des choix pour MVola
    mvola_1 = Choix("Acheter Credit ou Offre Yas")
    mvola_2 = Choix("Transferer argent (vers toute destination)")
    mvola_3 = Choix("MVola Credit ou Epargne")
    mvola_4 = Choix("Retrait d'argent")
    mvola_5 = Choix("Paiement Factures & Partenaires")
    mvola_6 = Choix("Mon compte")
    mvola_7 = Choix("Recevoir de l argent")
    mvola_8 = Choix("Banques et Micro-Finances")

    # Ajouter les choix dans MVola
    mvola.ajouter_option(mvola_1)
    mvola.ajouter_option(mvola_2)
    mvola.ajouter_option(mvola_3)
    mvola.ajouter_option(mvola_4)
    mvola.ajouter_option(mvola_5)
    mvola.ajouter_option(mvola_6)
    mvola.ajouter_option(mvola_7)
    mvola.ajouter_option(mvola_8)
    # Afficher le menu Mvola
    # mvola.afficher_menu()

    # Ajouter MVola dans le menu principal
    menu_principal = MenuPrincipal("YAS et MOI")
    menu_principal.ajouter_option(mvola)
    # Afficher le menu principal
    menu_principal.afficher_menu()


if __name__ == "__main__":
    main()
