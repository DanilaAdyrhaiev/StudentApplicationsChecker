class Student:
    def __init__(self, id: int, fullName: str) -> None:
        self.__id = id
        self.__fullName = fullName

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, value: str) -> None:
        self.__fullName = value

