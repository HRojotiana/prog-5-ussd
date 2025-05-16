from adapters.Choix import Choix
from adapters.MenuPrincipal import MenuPrincipal
from typing import List


class MVola(Choix):
    def __init__(self, title: str):
        super().__init__(title)
        self.options : List[Choix] = []

    def afficher_menu(self) -> None:
        self.page_precedente()
        choix = input("\n")
        if choix == '#':
            self.page_suivante()
        elif choix == "*":
            self.page_precedente()
        elif choix == "**":
            menu_principal = MenuPrincipal("YAS et MOI")
            menu_principal.afficher_menu()
        else:
            choix_entier = int(choix)
            if 1 <= choix_entier <= len(self.options):
                self.options[choix_entier - 1].afficher_menu()
            else:
                print("Choix invalide")

    def choisir(self, element_options, choix, first_index, last_index) -> None:
        if choix == '#':
            self.page_suivante()
        elif choix == "*":
            self.page_precedente()
        elif choix == "**":
            menu_principal = MenuPrincipal("YAS et MOI")
            menu_principal.afficher_menu()
        else:
            choix_entier = int(choix)
            if first_index <= choix_entier <= last_index:
                element_options[choix_entier - first_index].afficher_menu()
            else:
                print("Choix invalide")

    def page_suivante(self) -> None:
        element_page_suivante = self.options[4:9]
        print(element_page_suivante)
        print(f"{self.title}")
        for i in range(4, 8):
            print(f"{i + 1} {self.options[i].title}")
        print("* Page précédente")
        print("** Menu principal")
        self.choisir(element_page_suivante, input("\n"), 5, 8)

    def page_precedente(self) -> None:
        element_page_precedente = self.options[:4]
        last_index = len(element_page_precedente)
        print(f"{self.title}")
        for i in range(4):
            print(f"{i + 1} {self.options[i].title}")
        print("# Page suivante")
        self.choisir(element_page_precedente, input("\n"), 1, last_index)

    def ajouter_option(self, option) -> None:
        self.options.append(option)
