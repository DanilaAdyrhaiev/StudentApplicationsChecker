from entities.Application import Application
from repositories.ApplicationRepository import ApplicationRepository
from StudentService import StudentService
from SpecialtyService import SpecialtyService

class ApplicationService:
    def __init__(self, repository: ApplicationRepository) -> None:
        self.__repository = repository

    def addApplication(self, application: Application) -> None:
        self.__repository.createApplication(application)

    def getApplication(self, applicationId: int) -> Application:
        applicationData = self.__repository.getApplicationById(applicationId)
        if applicationData is not None:
            student = StudentService.getStudent(applicationData[1])
            specialty = SpecialtyService.getSpecialty(applicationData[2])
            if student is not None and specialty is not None:
                return Application(applicationData[0], student, specialty, applicationData[3], 
                                   applicationData[4], applicationData[5], applicationData[6])

    def getAllApplications(self) -> list[Application]:
        applications: list[Application] = []
        for application in self.__repository.getAllApplications():
            if application is not None:
                student = StudentService.getStudent(application[1])
                specialty = SpecialtyService.getSpecialty(application[2])
                if student is not None and specialty is not None:
                    applications.append(Application(application[0], student, specialty, 
                                                    application[3], application[4], application[5], application[6]))
        return applications

    def updateApplication(self, applicationId: int, updated_application: Application) -> bool:
        return self.__repository.updateApplication(applicationId, updated_application)

    def deleteApplication(self, applicationId: int) -> bool:
        return self.__repository.deleteApplication(applicationId)