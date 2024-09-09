from entities.Specialty import Specialty
import sqlite3

class SpecialtyRepository:
    def __init__(self) -> None:
        self.connect = sqlite3.connect('UniversityApplications.db')
        self.cursor = self.connect.cursor()

    def createSpecialty(self, specialty: Specialty) -> None:
        self.cursor.execute(
            "INSERT INTO Specialties(id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId) "
            "VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
            (specialty.id, specialty.name, specialty.faculty, specialty.educationalProgram, specialty.degree, 
             specialty.formOfStudy, specialty.url, specialty.university.id)
        )
        self.connect.commit()

    def getSpecialtyById(self, specialty__id: int) -> tuple[Specialty]:
        self.cursor.execute(
            "SELECT id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId FROM Specialties WHERE id = ?", 
            (specialty__id,)
        )
        row = self.cursor.fetchone()
        return row

    def getAllSpecialties(self) -> list[tuple[Specialty]]:
        self.cursor.execute("SELECT id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId FROM Specialties")
        rows = self.cursor.fetchall()
        return rows

    def updateSpecialty(self, specialty__id: int, updated__specialty: Specialty) -> bool:
        self.cursor.execute(
            "UPDATE Specialties SET name = ?, faculty = ?, educationalProgram = ?, degree = ?, formOfStudy = ?, url = ?, universityId = ? WHERE id = ?",
            (updated__specialty.name, updated__specialty.faculty, updated__specialty.educationalProgram, 
             updated__specialty.degree, updated__specialty.formOfStudy, updated__specialty.url, updated__specialty.university.id, specialty__id)
        )
        self.connect.commit()
        return self.cursor.rowcount > 0

    def deleteSpecialty(self, specialty__id: int) -> bool:
        self.cursor.execute("DELETE FROM Specialties WHERE id = ?", (specialty__id,))
        self.connect.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connect.close()
