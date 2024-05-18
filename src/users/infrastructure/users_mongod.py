from ...mongo.connect import ConnectionMongo
from bson import json_util, ObjectId
import json

class MongodUser:
    def __init__(self):
        self.connect = ConnectionMongo()

    def user_connect(self, user, pasw):
        db = self.connect.con

        resultado = db["Users"].find({"user_id": user, "password_hash": pasw}, {"nombre":False, "email":False, "carrera":False, "rol":False, "fecha_registro":False, "_id":False})
        json_resultado = json.loads(json_util.dumps(resultado))
        
        if len(json_resultado) == 0:
            json_resultado = None

        return json_resultado

