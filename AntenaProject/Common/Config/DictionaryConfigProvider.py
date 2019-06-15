from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
import configparser


class DictionaryConfigProvider(BaseConfigProvider):
    def __init__(self,baseDict={}):
        self.__Dict=baseDict

    def GetConfigValueForSectionAndKey(self,section,key,defaultvalue=None):
        if section not in self.__Dict:
            return defaultvalue
        if key not in self.__Dict[section]:
            return defaultvalue
        return self.__Dict[section][key]
    def GetConfigSection(self,section,defaultvalue=None):
        if section not in self.__Dict:
            return defaultvalue
        return self.self.__Dict[section]
    def SetValue(self,section,key,value):
        if section not in self.__Dict:
            self.__Dict[section]={}
        self.__Dict[section][key]=value