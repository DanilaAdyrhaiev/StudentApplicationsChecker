from Specialty import Specialty

class University:
    def __init__(self, id: int, title: str, url: str) -> None:
        self.__id: int = id
        self.__title: str = title
        self.__url: str = url

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        self.__url = value

    @property
    def specialties(self) -> list[Specialty]:
        return self.__specialties

    @specialties.setter
    def specialties(self, value: list[Specialty]) -> None:
        self.__specialties = value
