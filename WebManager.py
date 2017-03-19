#import urllib2
from urllib.request import urlopen

seriesUrl = 'http://api.tvmaze.com/singlesearch/shows?q='
episodesUrl = '&embed=episodes'

class ServiceManager:

    def getSeriesData(self, name):
        #return urllib2.urlopen(seriesUrl+name).read()
        return urlopen(seriesUrl+name).read()

    def getEpisodesData(self, name):
        #return urllib2.urlopen(seriesUrl+name+episodesUrl).read()
        return urlopen(seriesUrl+name+episodesUrl).read()
