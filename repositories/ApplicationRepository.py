import sqlite3;
from entities.Application import Application

class ApplicationRepository:
    def __init__(self) -> None:
        self.connect = sqlite3.connect('UniversityApplications.db')
        self.cursor = self.connect.cursor()

    def createApplication(self, application: Application) -> None:
        self.cursor.execute(
            "INSERT INTO Applications(id, studentId, specialtyId, rate, score, status, priority) "
            "VALUES(?, ?, ?, ?, ?, ?, ?)", 
            (application.id, application.student.id, application.specialty.id, application.rate, 
             application.score, application.status, application.priority)
        )
        self.connect.commit()

    def readApplicationById(self, applicationId: int) -> Application:
        self.cursor.execute(
            "SELECT id, studentId, specialtyId, rate, score, status, priority FROM Applications WHERE id = ?", 
            (applicationId,)
        )
        row = self.cursor.fetchone()
        return row

    def readAllApplications(self) -> list[Application]:
        self.cursor.execute("SELECT id, studentId, specialtyId, rate, score, status, priority FROM Applications")
        rows = self.cursor.fetchall()
        return rows
    
    def updateApplication(self, applicationId: int, updatedApplication: Application) -> bool:
        self.cursor.execute(
            "UPDATE Applications SET studentId = ?, specialtyId = ?, rate = ?, score = ?, status = ?, priority = ? WHERE id = ?",
            (updatedApplication.student.id, updatedApplication.specialty.id, updatedApplication.rate, 
             updatedApplication.score, updatedApplication.status, updatedApplication.priority, applicationId)
        )
        self.connect.commit()
        return self.cursor.rowcount > 0

    def deleteApplication(self, applicationId: int) -> bool:
        self.cursor.execute("DELETE FROM Applications WHERE id = ?", (applicationId,))
        self.connect.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connect.close()
