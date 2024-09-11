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
    
    def readSpecialtyById(self, specialtyId: int) -> tuple[Specialty]:
        self.cursor.execute(
            "SELECT id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId FROM Specialties WHERE id = ?", 
            (specialtyId,)
        )
        row = self.cursor.fetchone()
        return row
    
    def readSpecialtyByName(self, specialty_name: str) -> tuple[Specialty]:
        self.cursor.execute(
            "SELECT id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId FROM Specialties WHERE name = ?", 
            (specialty_name,)
        )
        row = self.cursor.fetchone()
        return row

    def readAllSpecialties(self) -> list[tuple[Specialty]]:
        self.cursor.execute("SELECT id, name, faculty, educationalProgram, degree, formOfStudy, url, universityId FROM Specialties")
        rows = self.cursor.fetchall()
        return rows

    def updateSpecialty(self, specialtyId: int, updatedSpecialty: Specialty) -> bool:
        self.cursor.execute(
            "UPDATE Specialties SET name = ?, faculty = ?, educationalProgram = ?, degree = ?, formOfStudy = ?, url = ?, universityId = ? WHERE id = ?",
            (updatedSpecialty.name, updatedSpecialty.faculty, updatedSpecialty.educationalProgram, 
             updatedSpecialty.degree, updatedSpecialty.formOfStudy, updatedSpecialty.url, updatedSpecialty.university.id, specialtyId)
        )
        self.connect.commit()
        return self.cursor.rowcount > 0

    def deleteSpecialty(self, specialtyId: int) -> bool:
        self.cursor.execute("DELETE FROM Specialties WHERE id = ?", (specialtyId,))
        self.connect.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connect.close()
