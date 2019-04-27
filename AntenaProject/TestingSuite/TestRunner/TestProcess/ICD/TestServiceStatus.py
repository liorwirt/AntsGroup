from AntenaProject.Common.Services.Communication.ControlConnection.ICD.StatusMessege import StatusMessege
#Holds Test Data report
class TestServiceStatus(StatusMessege):
    def __init__(self,id):
        StatusMessege.__init__(self,id=id)
        pass