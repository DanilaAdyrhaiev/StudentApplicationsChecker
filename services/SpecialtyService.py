from entities.Specialty import Specialty
from repositories.SpecialtyRepository import SpecialtyRepository
from UniversityService import UniversityService

class SpecialtyService:
    def __init__(self, repository: SpecialtyRepository) -> None:
        self.__repository = repository

    def addSpecialty(self, specialty: Specialty) -> None:
        self.__repository.createSpecialty(specialty)

    def getSpecialty(self, specialty_id: int) -> Specialty:
        specialtyData = self.__repository.getSpecialtyById(specialty_id)
        university = UniversityService.getUniversity()

    def getAllSpecialties(self) -> list[Specialty]:
        return self.__repository.getAllSpecialties()

    def updateSpecialty(self, specialty_id: int, updated_specialty: Specialty) -> bool:
        return self.__repository.updateSpecialty(specialty_id, updated_specialty)

    def deleteSpecialty(self, specialty_id: int) -> bool:
        return self.__repository.deleteSpecialty(specialty_id)
