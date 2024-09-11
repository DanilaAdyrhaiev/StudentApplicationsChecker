from entities.University import University
import sqlite3

class UniversityRepository:
    def __init__(self) -> None:
        self.connect = sqlite3.connect('UniversityApplications.db')
        self.cursor = self.connect.cursor()

    def createUniversity(self, university: University) -> None:
        self.cursor.execute(
            "INSERT INTO Universities(id, title, url) VALUES(?, ?, ?)", 
            (university.id, university.title, university.url)
        )
        self.connect.commit()

    def readUniversityById(self, university__id: int) -> University:
        self.cursor.execute("SELECT id, title, url FROM Universities WHERE id = ?", (university__id,))
        row = self.cursor.fetchone()
        if row:
            return University(row[0], row[1], row[2])
        return None
    
    def readUniversityByName(self, university_name: str) -> University:
        self.cursor.execute("SELECT id, title, url FROM Universities WHERE title = ?", (university_name,))
        row = self.cursor.fetchone()
        if row:
            return University(row[0], row[1], row[2])
        return None

    def readAllUniversities(self) -> list[University]:
        self.cursor.execute("SELECT id, title, url FROM Universities")
        rows = self.cursor.fetchall()
        return [University(row[0], row[1], row[2]) for row in rows]

    def updateUniversity(self, university__id: int, updated__university: University) -> bool:
        self.cursor.execute(
            "UPDATE Universities SET title = ?, url = ? WHERE id = ?",
            (updated__university.title, updated__university.url, university__id)
        )
        self.connect.commit()
        return self.cursor.rowcount > 0

    def deleteUniversity(self, university__id: int) -> bool:
        self.cursor.execute("DELETE FROM Universities WHERE id = ?", (university__id,))
        self.connect.commit()
        return self.cursor.rowcount > 0