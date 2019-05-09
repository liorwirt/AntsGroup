from AntenaProject.AntZTest.AntsController.BaseAntsController import BaseAntsController
from typing import Dict
class SimpleAntsContrller(BaseAntsController):

    def _GetPreTestAdditionalData(self) -> Dict:
        return {}


    def _GetPrePreStepAdditionalData(self) -> Dict:
        return {}


    def _GetPostStepAdditionalData(self) -> Dict:
        return {}


    def _GetPostTestAdditionalData(self) -> Dict:
        return {}
