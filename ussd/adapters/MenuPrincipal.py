from interfaces.MenuInterfaces import MenuInterface
from adapters.Choix import Choix
from typing import List


class MenuPrincipal(MenuInterface):
    def __init__(self, title: str):
        super().__init__(title)
        self.options : List[Choix] = []

    def afficher_menu(self) -> None:
        print(f"Menu Principal: {self.title}")

    def ajouter_option(self, option):
        return super().ajouter_option(option)

    def page_suivante(self) -> None:
        print("Page suivante du menu principal")

    def page_precedente(self) -> None:
        print("Page précédente du menu principal")
