import requests
from typing import List
import socket
import logging
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
class ServerComm(object):
    def __init__(self,configprovider:BaseConfigProvider):
        self._in_url=configprovider.GetConfigValueForSectionAndKey("Robots","GetURL")
        self._out_url=configprovider.GetConfigValueForSectionAndKey("Robots","PutURL")


        self._ack_udp_ip=configprovider.GetConfigValueForSectionAndKey("Robots","Ack_udp_ip")
        self._ack_udp_port = (int)(configprovider.GetConfigValueForSectionAndKey("Robots","Ack_udp_port"))
        self._ack_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._ack_sock.bind((self._ack_udp_ip, self._ack_udp_port))

    def GetAntsIds(self)->List[str]:
        ids=[]
        resp = requests.get(self._in_url)
        if resp.status_code != 200:
            logging.info('Got No Ants!!!!!')

        else:
            for ant in resp.json():
                ids.append(ant['id'])
        return ids
    def perform_step(self,ant_id,step):

        task = {"antCommandsArr": step}
        resp = requests.put(format(f'{self._out_url}{ant_id}'), json=task)
        if resp.status_code != 200:
            logging.info(format(f'Ant {ant_id} Put falied {resp.status_code}'))
            return False


        data, addr = self._ack_sock.recvfrom(1024)  # buffer size is 1024 bytes

        if len(data)==0:
            return False

        return True

