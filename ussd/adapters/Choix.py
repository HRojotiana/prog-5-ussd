from interfaces.MenuInterfaces import MenuInterface


class Choix(MenuInterface):
    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def afficher_menu(self) -> None:
        print(f"{self.title}")

    def ajouter_option(self, option):
        return super().ajouter_option(option)

    def page_suivante(self) -> None:
        print("Page suivante du menu choix")

    def page_precedente(self) -> None:
        print("Page précédente du menu choix")

    def __repr__(self):
        return f"title: {self.title}"
