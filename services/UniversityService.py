from entities.University import University
from repositories.UniversityRepository import UniversityRepository

class UniversityService:
    def __init__(self, repository: UniversityRepository) -> None:
        self.__repository = repository

    def addUniversity(self, university: University) -> None:
        self.__repository.createUniversity(university)

    def getUniversity(self, university_id: int) -> University:
        return self.__repository.getUniversityById(university_id)

    def getAllUniversities(self) -> list[University]:
        return self.__repository.getAllUniversities()

    def updateUniversity(self, university_id: int, updated_university: University) -> bool:
        return self.__repository.updateUniversity(university_id, updated_university)

    def deleteUniversity(self, university_id: int) -> bool:
        return self.__repository.deleteUniversity(university_id)
