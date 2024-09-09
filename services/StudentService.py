from entities.Student import Student
from repositories.StudentRepository import StudentRepository

class StudentService:
    def __init__(self, repository: StudentRepository) -> None:
        self.__repository = repository

    def addStudent(self, student: Student) -> None:
        self.__repository.createStudent(student)
    
    def addStudents(self, students: list[Student]) -> None:
        self.__repository.createStudents(students)

    def updateStudent(self, student: Student) -> None:
        self.__repository.updateStudent(student)
    
    def getStudent(self, id) -> Student:
        return self.__repository.readStudentById(id)
    
    def getAllStudents(self) -> list[Student]:
        return self.__repository.readAllStudents()