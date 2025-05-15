from adapters.Choix import Choix
from adapters.MenuPrincipal import MenuPrincipal
from typing import List


class MVola(Choix):
    def __init__(self, title: str):
        super().__init__(title)
        self.options : List[Choix] = []

    def afficher_menu(self) -> None:
        self.page_precedente()
        numero_choix = ""
        while numero_choix != "0":
            numero_choix = input("\n")
            if numero_choix == "#":
                self.page_suivante()
            elif numero_choix == "*":
                self.page_precedente()
            elif numero_choix == "**":
                menu_principal = MenuPrincipal("YAS et MOI")
                menu_principal.afficher_menu()

    def page_suivante(self) -> None:
        print(f"{self.title}")
        for i in range(4, 8):
            print(f"{i + 1} {self.options[i].title}")
        print("* Page précédente")
        print("** Menu principal")

    def page_precedente(self) -> None:
        print(f"{self.title}")
        for i in range(4):
            print(f"{i + 1} {self.options[i].title}")
        print("# Page suivante")

    def ajouter_option(self, option) -> None:
        self.options.append(option)
