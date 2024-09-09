from Student import Student
from University import University

class Specialty:
    def __init__(self, id: int,
                 name: str, 
                 faculty: str, 
                 educationalProgram: str,
                 degree: str,
                 formOfStudy: str,
                 url: str,
                 university: University) -> None:
        self.__id = id
        self.__name = name
        self.__faculty = faculty
        self.__educationalProgram = educationalProgram
        self.__degree = degree
        self.__formOfStudy = formOfStudy
        self.__url = url
        self.__university = university

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def faculty(self) -> str:
        return self.__faculty

    @faculty.setter
    def faculty(self, value: str) -> None:
        self.__faculty = value

    @property
    def educationalProgram(self) -> str:
        return self.__educationalProgram

    @educationalProgram.setter
    def educationalProgram(self, value: str) -> None:
        self.__educationalProgram = value

    @property
    def degree(self) -> str:
        return self.__degree

    @degree.setter
    def degree(self, value: str) -> None:
        self.__degree = value

    @property
    def formOfStudy(self) -> str:
        return self.__formOfStudy

    @formOfStudy.setter
    def formOfStudy(self, value: str) -> None:
        self.__formOfStudy = value

    @property
    def students(self) -> list[Student]:
        return self.__students

    @students.setter
    def students(self, value: list[Student]) -> None:
        self.__students = value

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        self.__url = value

    @property
    def university(self) -> University:
        return self.__university

    @university.setter
    def university(self, value: University) -> None:
        self.__university = value