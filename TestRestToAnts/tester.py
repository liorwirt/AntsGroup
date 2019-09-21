import requests
import socket

def startants():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1337
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    resp = requests.get('http://localhost:3000/api/ants/')
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/ {}'.format(resp.status_code))
    for ant in resp.json():
        print('{} {}'.format(ant['id'], ant['antCommandsArr']))


    while True:
        task = {"antCommandsArr": "f1"}
        resp = requests.put('http://localhost:3000/api/ants/1', json=task)

        if resp.status_code != 200:
            raise Exception('POST /tasks/ {}'.format(resp.status_code))
        print('Created task. ID: {}'.format(resp.json()["id"]))
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print ("received message:", data)




if __name__ == '__main__':
    startants()