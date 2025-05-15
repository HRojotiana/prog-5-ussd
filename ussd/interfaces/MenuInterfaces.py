from abc import ABC, abstractmethod


class MenuInterface(ABC):
    def __init__(self, title: str):
        self.title = title

    @property
    @abstractmethod
    def afficher_menu(self, title: str) -> None:
        pass

    @abstractmethod
    def page_suivante(self) -> None:
        pass

    @abstractmethod
    def page_precedente(self) -> None:
        pass
