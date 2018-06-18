import requests
import json
base_url = 'http://127.0.0.1:5000'

def getUsers():
    response = requests.get(base_url+'/users')
    print(response.text)

def getUser(userID):
    response = requests.get(base_url+'/users/'+str(userID))
    print(response.text)

def getEvents(userID):
    response = requests.get(base_url+'/users/'+str(userID)+'/events')
    print(response.text)

def getStickers(userID):
    response = requests.get(base_url+'/users/'+str(userID)+'/stickers')
    print(response.text)

getStickers(1)

while 1:
    x = 0
    x = int(input("Wybierz opcję: ")) 
    if x == 9:
        break
    if x == 2:
        print('krzeslo')
    if x == 1:
        getUsers()


