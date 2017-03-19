from pymongo import MongoClient
import datetime
from bson import *

database = 'seriesDB'
series_collection = 'series'
episodes_collection = 'episodes'
daysBack = 2


class EpisodeRepo:

    def __init__(self, mongoClient):
        self.mongoClient = mongoClient
        self.db = self.mongoClient[database]
        self.collection = self.db[episodes_collection]
        
    def getSeriesInfoByName(self, name):
        return self.collection.find_one({'name': name})

    def getNotAiredEpisodes(self, _id):
        return self.collection.find_one({'id': _id, 'airdate':{'$gte': datetime.date.today()}})
    
    def getRecentlyAiredEpisodes(self, _id):
        return self.collection.find_one({'id': _id, 'airdate':{'$gte': (datetime.date.today() - timedelta(days=daysBack)), '$lte': datetime.date.today()}})

    def updateEpisodes(self, data):
        self.collection.update({data['id']},{"$set":{BSON.encode(data)}})

    def insertEpisodes(self, data):
        self.collection.insert({BSON.encode(data)})
        
class SeriesRepo:

    def __init__(self, mongoClient):
        self.mongoClient = mongoClient
        self.db = self.mongoClient[database]
        self.collection = self.db[series_collection]

    def getAllSeries(self):
        return self.collection.find()
    
    def getSeriesById(self, _id):
        return self.collection.find_one({'id': _id})

    def getSeriesByName(self, name):
        return self.collection.find_one({'name': name})

    def updateSeries(self, data):
        self.collection.update({data['id']},{"$set":{BSON.encode(data)}})
        
    def insertSeries(self, data):
        self.collection.insert({BSON.encode(data)})
    
class MongoManager: 

    def __init__(self):
        self.mongoClient = MongoClient() # Connect to localhost
        self.episodeRepo = EpisodeRepo(self.mongoClient)
        self.seriesRepo = SeriesRepo(self.mongoClient)

    def getEpisodeRepo(self):
        return self.episodeRepo

    def getSeriesRepo(self):
        return self.seriesRepo
