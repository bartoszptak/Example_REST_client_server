import requests
import sys
base_url = 'http://127.0.0.1:5000'


# /users
def getUsers():
    response = requests.get(base_url + '/users')
    print(response.text)


def postUsers(name, mail):
    data = {'name': name, 'mail': mail}
    response = requests.post(base_url + '/users', json=data)
    print(response.text)


# /users/<userID>
def getUser(userID):
    response = requests.get(base_url + '/users/' + str(userID))
    print(response.text)


def putUser(userID, name, mail):
    data = {'name': name, 'mail': mail}
    response = requests.put(base_url + '/users/' + str(userID), json=data)
    print(response.text)


def deleteUser(userID):
    response = requests.delete(base_url + '/users/' + str(userID))
    print(response.text)


# /users/<userID>/stickers

def getStickers(userID):
    response = requests.get(base_url + '/users/' + str(userID) + '/stickers')
    print(response.text)


def postStickers(userID, title, text, color):
    data = {'title': title, 'text': text, 'color': color}
    response = requests.post(base_url + '/users/' + str(userID) + '/stickers', json=data)
    print(response.text)


# /users/<userID>/events

def getEvents(userID):
    response = requests.get(base_url + '/users/' + str(userID) + '/events')
    print(response.text)


def postEvents(userID, title, time):
    data = {'title': title, 'time': time}
    response = requests.post(base_url + '/users/' + str(userID) + '/events', json=data)
    print(response.text)


# /users/<userID>/stickers/<stickerID>

def getSticker(userID, stickerID):
    response = requests.get(base_url + '/users/' + str(userID) + '/stickers/' + str(stickerID))
    print(response.text)


def putSticker(userID, stickerID, title, text, color):
    data = {'title': title, 'text': text, 'color': color}
    response = requests.put(base_url + '/users/' + str(userID) + '/stickers/' + str(stickerID), json=data)
    print(response.text)


def deleteSticker(userID, stickerID):
    response = requests.delete(base_url + '/users/' + str(userID) + '/stickers/' + str(stickerID))
    print(response.text)


# /users/<userID>/events/<eventID>

def getEvent(userID, eventID):
    response = requests.get(base_url + '/users/' + str(userID) + '/events/' + str(eventID))
    print(response.text)


def putEvent(userID, eventID, title, time):
    data = {'title': title, 'time': time}
    response = requests.put(base_url + '/users/' + str(userID) + '/events/' + str(eventID), json=data)
    print(response.text)


def deleteEvent(userID, eventID):
    response = requests.delete(base_url + '/users/' + str(userID) + '/events/' + str(eventID))
    print(response.text)

if __name__ == '__main__':
    if sys.argv[1] == 'users':
        if sys.argv[2] == 'get':
            getUsers()
        if sys.argv[2] == 'put':
            pass
        if sys.argv[2] == 'post':
            postUsers(sys.argv[3],sys.argv[4])
        if sys.argv[2] == 'delete':
            pass
    if sys.argv[1] == 'user':
        if sys.argv[2] == 'get':
            getUser(sys.argv[3])
        if sys.argv[2] == 'put':
            putUser(sys.argv[3],sys.argv[4],sys.argv[5])
        if sys.argv[2] == 'post':
            pass
        if sys.argv[2] == 'delete':
            deleteUser(sys.argv[3])
    if sys.argv[1] == 'stickers':
        if sys.argv[2] == 'get':
            getStickers(sys.argv[3])
        if sys.argv[2] == 'put':
            pass
        if sys.argv[2] == 'post':
            postStickers(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
        if sys.argv[2] == 'delete':
            pass
    if sys.argv[1] == 'events':
        if sys.argv[2] == 'get':
            getEvents(sys.argv[3])
        if sys.argv[2] == 'put':
            pass
        if sys.argv[2] == 'post':
            postEvents(sys.argv[3],sys.argv[4],sys.argv[5])
        if sys.argv[2] == 'delete':
            pass
    if sys.argv[1] == 'sticker':
        if sys.argv[2] == 'get':
            getSticker(sys.argv[3],sys.argv[4])
        if sys.argv[2] == 'put':
            putSticker(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        if sys.argv[2] == 'post':
            pass
        if sys.argv[2] == 'delete':
            deleteSticker(sys.argv[3], sys.argv[4])
    if sys.argv[1] == 'event':
        if sys.argv[2] == 'get':
            getEvent(sys.argv[3],sys.argv[4])
        if sys.argv[2] == 'put':
            putEvent(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
        if sys.argv[2] == 'post':
            pass
        if sys.argv[2] == 'delete':
            deleteEvent(sys.argv[3], sys.argv[4])