from pymongo import MongoClient
from decouple import config

class ConnectionMongo:

    def __init__(self):
        #_ NAME DB
        db = "EduBot"

        connection = MongoClient(config('MONGODB_URL'), uuidRepresentation='standard')
        self.con = connection[db]

