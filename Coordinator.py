from MongoManager import *
from WebManager import *
import json

class Coordinator:

    def __init__(self):
        self.mongoManager = MongoManager()
        self.serviceManager = ServiceManager()

    def updateSeries(self):
        for series in self.mongoManager.getAllSeries():
            data = json.loads(self.serviceManager.getSeriesData(series['name']))
            if ( data['updated'] > series['updated']):
                self.mongoManager.getSeriesRepo.updateSeries(series['id'], data)
                episodesData = json.loads(self.serviceManager.getEpisodesData(series['name']))
                self.mongoManager.getEpisodeRepo.updateEpisodes(series['id'], episodesData)

    def getRecentEpisodes(self):
                for series in self.mongoManager.getAllSeries():
                    _id = series['id']
                    print(self.mongoManager.getEpisodesRepo.getRecentlyAiredEpisodes(_id))


    def bulkInsert(self):
        series1 = 'Sherlock'
        series2 = 'Kingdom'
        series_data1 = self.serviceManager.getSeriesData(series1)
        series_data2 = self.serviceManager.getSeriesData(series2)
        episodes1 = self.serviceManager.getEpisodesData(series1)
        episodes2 = self.serviceManager.getEpisodesData(series2)

        self.mongoManager.getSeriesRepo().insertSeries(series_data1)
        self.mongoManager.getSeriesRepo().insertSeries(series_data2)
        self.mongoManager.getEpisodeRepo().insertEpisodes(episodes1)
        self.mongoManager.getEpisodeRepo().insertEpisodes(episodes2)

c = Coordinator()
c.bulkInsert()


    
                
