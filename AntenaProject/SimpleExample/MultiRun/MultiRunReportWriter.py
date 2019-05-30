import xml.etree.ElementTree as ET
import os
class MultiRunReportWriter(object):
    def __init__(self,folder):
        self._InitDataDict={}
        self._ResultDataDict = {}
        self._DestFolder=folder

    def SetDataForProcess(self,id,data:str):
        self._InitDataDict[id]=data;

    def SetResultForProcess(self, id, data: str):
        self._ResultDataDict[id] = data;

    def ComposeReport(self):
        data = ET.Element('Report')
        for key in self._InitDataDict.keys():
            item = ET.SubElement(data, 'Process')
            item.set('Id',str(key))
            initialdata=ET.SubElement(item,'InitData')
            initialdata.text=self._InitDataDict[key];
            if (key in self._ResultDataDict):
                result = ET.SubElement(item, 'Result')
                result.text = self._ResultDataDict[key];




        # create a new XML file with the results
        with open(os.path.join(self._DestFolder,"Report.xml"), "w") as myfile:

            myfile.write(ET.tostring(data).decode("utf-8"))