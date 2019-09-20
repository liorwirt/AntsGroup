from AntenaProject.AntZTest.AntsController.BaseStepEnabler import BaseStepEnabler
class DummyStepEnabler(BaseStepEnabler):

    def ShouldPerformStep(self) -> bool:
        return True