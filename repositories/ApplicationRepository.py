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

    def getApplicationById(self, application__id: int) -> Application:
        self.cursor.execute(
            "SELECT id, studentId, specialtyId, rate, score, status, priority FROM Applications WHERE id = ?", 
            (application__id,)
        )
        row = self.cursor.fetchone()
        if row:
            student__id = row[1]
            specialty__id = row[2]
            return Application(row[0], student__id, specialty__id, row[3], row[4], row[5], row[6])
        return None

    def getAllApplications(self) -> list[Application]:
        self.cursor.execute("SELECT id, studentId, specialtyId, rate, score, status, priority FROM Applications")
        rows = self.cursor.fetchall()
        return [Application(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]

    def updateApplication(self, application__id: int, updated__application: Application) -> bool:
        self.cursor.execute(
            "UPDATE Applications SET studentId = ?, specialtyId = ?, rate = ?, score = ?, status = ?, priority = ? WHERE id = ?",
            (updated__application.student.id, updated__application.specialty.id, updated__application.rate, 
             updated__application.score, updated__application.status, updated__application.priority, application__id)
        )
        self.connect.commit()
        return self.cursor.rowcount > 0

    def deleteApplication(self, application__id: int) -> bool:
        self.cursor.execute("DELETE FROM Applications WHERE id = ?", (application__id,))
        self.connect.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connect.close()
