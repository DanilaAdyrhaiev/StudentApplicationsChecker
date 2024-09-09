from Student import Student
from Specialty import Specialty

class Application:
    def __init__(self, id: int,
                 student: Student,
                 specialty: Specialty, 
                 rate: int,
                 score: float,
                 status: str,
                 priority: str) -> None:
        self.__id = id
        self.__student = student
        self.__specialty = specialty
        self.__rate = rate
        self.__score = score
        self.__status = status
        self.__priority = priority

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    @property
    def student(self) -> Student:
        return self.__student

    @student.setter
    def student(self, value: Student) -> None:
        self.__student = value

    @property
    def specialty(self) -> Specialty:
        return self.__specialty

    @specialty.setter
    def specialty(self, value: Specialty) -> None:
        self.__specialty = value

    @property
    def rate(self) -> int:
        return self.__rate

    @rate.setter
    def rate(self, value: int) -> None:
        self.__rate = value

    @property
    def score(self) -> float:
        return self.__score

    @score.setter
    def score(self, value: float) -> None:
        self.__score = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        self.__status = value

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, value: str) -> None:
        self.__priority = value
