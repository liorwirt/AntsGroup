import requests
from typing import List
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
class ServerComm(object):
    def __init__(self,configprovider:BaseConfigProvider):
        self._in_url=configprovider.GetConfigValueForSectionAndKey("Robots","GetURL")
        self._out_url=configprovider.GetConfigValueForSectionAndKey("Robots","PutURL")
    def GetAntsIds(self)->List[str]:
        ids=[]
        resp = requests.get(self._in_url)
        if resp.status_code != 200:
            print('Got No Ants!!!!!')

        else:
            for ant in resp.json():
                ids.append(ant['id'])
        return ids
    def perform_step(self,ant_id,steps:List[str]):
        for step in steps:
            task = {"antCommandsArr": step}
            resp = requests.put(format(f'http://localhost:3000/api/ants/{ant_id}'), json=task)
            if resp.status_code != 200:
                print(format(f'Ant {ant_id} Put falied {resp.status_code}'))
                return False
        return True

