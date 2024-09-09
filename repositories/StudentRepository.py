import sqlite3;
from entities.Student import Student

class StudentRepository:
    def __init__(self) -> None:
        self.__connect = sqlite3.connect('UniversityApplications.db')
        self.__cursor = self.connect.cursor()
    
    def createStudent(self, student: Student) -> None:
        self.cursor.execute("INSERT INTO Students(id, name) VALUES(?, ?)", (student.id, student.fullName))
        self.connect.commit()
    
    def createStudents(self, students: list[Student]) -> None:
        self.cursor.executemany("INSERT INTO Students(id, name) VALUES(?, ?)",
                                [(student.id, student.fullName) for student in students])
        self.connect.commit()
    
    def readStudentById(self, student__id: int) -> Student:
        self.cursor.execute("SELECT id, name FROM Students WHERE id = ?", (student__id,))
        row = self.cursor.fetchone()
        if row:
            return Student(row[0], row[1])
        return None
    
    def readAllStudents(self) -> list[Student]:
        self.cursor.execute("SELECT id, name FROM Students")
        rows = self.cursor.fetchall()
        return [Student(row[0], row[1]) for row in rows]
    
    def updateStudent(self, student: Student):
        self.cursor.execute("UPDATE Students SET name = ? WHERE id = ?", (student.fullName, student.id))
        self.connect.commit()

    def deleteStudent(self, student__id: int):
        self.cursor.execute("DELETE FROM Students WHERE id = ?", (student__id,))
        self.connect.commit()