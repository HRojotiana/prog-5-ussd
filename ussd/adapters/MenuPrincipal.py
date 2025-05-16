from interfaces.MenuInterfaces import MenuInterface
from adapters.Choix import Choix
from typing import List


class MenuPrincipal(MenuInterface):
    def __init__(self, title: str):
        super().__init__(title)
        self.options : List[Choix] = []

    def afficher_menu(self) -> None:
        self.page_precedente()
        choix = int(input("\n"))
        if choix == 0:
            self.page_suivante()
        elif 1 <= choix <= len(self.options):
            self.options[choix - 1].afficher_menu()
        else:
            print("Veuillez choisir parmi la liste")
            self.afficher_menu()

    def page_suivante(self) -> None:
        print("Page suivante du menu principal")

    def page_precedente(self) -> None:
        print(f"{self.title}")
        for i in range(len(self.options)):
            print(f"{i + 1} {self.options[i].title}")
        print("0 Page suivante")

    def ajouter_option(self, option) -> None:
        self.options.append(option)
