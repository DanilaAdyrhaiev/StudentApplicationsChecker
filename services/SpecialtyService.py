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
        if specialtyData != None:
            university = UniversityService.getUniversity(specialtyData[7])
            if university != None:
                return Specialty(specialtyData[0], specialtyData[1],specialtyData[2], specialtyData[3],specialtyData[4],specialtyData[5],specialtyData[6], university)

    def getAllSpecialties(self) -> list[Specialty]:
        specialties: list[Specialty] = [] 
        for specialty in self.__repository.getAllSpecialties():
            if specialty != None:
                university = UniversityService.getUniversity(specialty[7])
                if university != None:
                    specialties.append(Specialty(specialty[0], specialty[1],specialty[2],specialty[3],specialty[4],specialty[5],specialty[6], university))

    def updateSpecialty(self, specialty_id: int, updated_specialty: Specialty) -> bool:
        return self.__repository.updateSpecialty(specialty_id, updated_specialty)

    def deleteSpecialty(self, specialty_id: int) -> bool:
        return self.__repository.deleteSpecialty(specialty_id)
