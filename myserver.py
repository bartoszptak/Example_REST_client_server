from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import datetime

db_connect = create_engine('sqlite:///notes.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select u.name, u.name from Users u")
        return {'users': [i[0] for i in query.cursor.fetchall()]}
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        name = request.json['name']
        mail = request.json['mail']
        today = datetime.date.today()
        date = today.strftime('%Y-%m-%d %H:%M:%S')
        query = conn.execute("insert into Users values(null,'{0}','{1}','{2}')".format(name,mail,date))
        return {'status':'success'}

class UsersID(Resource):
    def get(self, userID):
        conn = db_connect.connect()
        query = conn.execute("select * from Users where UserId =%d "  %int(userID))
        result = {'user': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Stickers(Resource):
    def get(self, userID):
        conn = db_connect.connect()
        query = conn.execute("select * from Stickers where UserId =%d "  %int(userID))
        result = {'stickers': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def post(self,userID):
        conn = db_connect.connect()
        print(request.json)
        title = request.json['title']
        text = request.json['text']
        color = request.json['color']
        query = conn.execute("insert into Stickers values(null,{0},'{1}','{2}',{3})".format(int(userID),title,text,int(color)))
        return {'status':'success'}

class StickerID(Resource):
    def get(self, userID, stickerID):
        conn = db_connect.connect()
        query = conn.execute("select * from Stickers where UserId =%d and stickerID=%d"  %(int(userID),int(stickerID)))
        result = {'sticker': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)   

    def delete(self, userID, stickerID):
        conn = db_connect.connect()
        query = conn.execute("delete from Stickers where UserId =%d and stickerID=%d" %(int(userID),int(stickerID)))
        return {'status':'success'}

class Events(Resource):
    def get(self, userID):
        conn = db_connect.connect()
        query = conn.execute("select * from Events where UserId =%d "  %int(userID))
        result = {'events': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    
    def post(self,userID):
        conn = db_connect.connect()
        print(request.json)
        title = request.json['title']
        time = request.json['time']
        query = conn.execute("insert into Events values(null,{0},'{1}','{2}')".format(int(userID),title,time))
        return {'status':'success'}

class EventID(Resource):
    def get(self, userID, eventID):
        conn = db_connect.connect()
        query = conn.execute("select * from Events where UserId =%d and eventsID=%d"  %(int(userID),int(eventID)))
        result = {'event': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)   

    def delete(self, userID, eventID):
        conn = db_connect.connect()
        query = conn.execute("delete from Events where UserId =%d and eventsID=%d" %(int(userID),int(eventID)))
        return {'status':'success'}

api.add_resource(Users, '/users')
api.add_resource(UsersID, '/users/<userID>')
api.add_resource(Stickers, '/users/<userID>/stickers')
api.add_resource(StickerID, '/users/<userID>/stickers/<stickerID>')
api.add_resource(Events, '/users/<userID>/events')
api.add_resource(EventID, '/users/<userID>/events/<eventID>')

if __name__ == '__main__':
     app.run()
