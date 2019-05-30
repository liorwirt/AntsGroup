from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
import configparser
class IniConfigProvider(BaseConfigProvider):
    def __init__(self,filename):
        self.__Configprovider=configparser.ConfigParser()
        self.__Configprovider.read(filenames=[filename])

    def GetConfigValueForSectionAndKey(self,section,key,defaultvalue=None):
        if section not in self.__Configprovider:
            return defaultvalue
        if key not in self.__Configprovider[section]:
            return defaultvalue
        return self.__Configprovider[section][key]
    def GetConfigSection(self,section,defaultvalue=None):
        if section not in self.__Configprovider:
            return defaultvalue
        return self.__Configprovider[section]

    def SetConfigSection(self, section,key, value):
        self.__Configprovider[section][key]=value