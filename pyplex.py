import urllib2
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML



class PlexServer(object):
    
    def __init__(self, address, port):
        # remove slash at end of address
        if address[-1] == '/':
            address = address[:-1]
        self.address = address
        self.port = port
        
    def query(self, path):
        if path[0] == '/':
            path = path[1:]
            
        # open url and get raw xml data
        try: 
            response = urllib2.urlopen("%s:%d/%s" % (self.address, self.port, path))
        except urllib2.URLError, e:
            print e
        
        # create element from xml data
        xmldata = response.read()
        element = XML(xmldata)
        return element
    
    
    def __str__(self):
        return "<PlexServer: %s:%d/>" % (self.address, self.port) 
    
    def __repr__(self):
        return "<PlexServer: %s:%d/>" % (self.address, self.port) 
    
    
    @property
    def library(self):
        elem = self.query("/library")
        return Library(self)
        


class Library(object):
    def __init__(self, server):
        self.server = server
    
    def __str__(self):
        return "<Library: %s>" % server
    
    def __repr__(self):
        return "<Library: %s>" % server
    
    
    @property
    def sections(self):
        elem = self.server.query("/library/sections")
        sectypes = {'movie':MovieSection, 'show':ShowSection}
        seclist = [sectypes[e.attrib['type']](e.attrib['title'], e.attrib['key']) for e in elem]
        return seclist
    
    @property
    def shows(self):
        elem = self.server.query("/library/sections")
        seclist = [ShowSection(e.attrib['title'], e.attrib['key'], self.server) for e in elem if e.attrib['type'] == 'show']
        return seclist
    


class Section(object):
    def __init__(self, name, key, server):
        self.name = name
        self.key = int(key)
        self.server = server

    def __str__(self):
        return "<Section: %s>" % self.name

    def __repr__(self):
        return "<Section: %s>" % self.name
    

class ShowSection(Section):
    def __init__(self, name, key, server):
        Section.__init__(self, name, key, server)
        
        self.episodeCategories = ['newest', 'recentlyAdded', 'recentlyViewed', 'onDeck']
        self.showCategories = ['all', 'unwatched', 'recentlyViewedShows']
        self.containerCategories = ['collection', 'firstCharacter', 'genre', 'year', 'contentRating', 'folder']
    
    def __str__(self):
        return "<ShowSection: %s>" % self.name

    def __repr__(self):
        return "<ShowSection: %s>" % self.name
    
    def getEpisodes(self, category='newest'):
        assert category in self.episodeCategories
        
        elem = self.server.query("/library/sections/%d/%s" % (self.key, category))
        print elem[0].attrib
    
    
    
    
    

class MovieSection(Section):
    def __init__(self, name, key, server):
        Section.__init__(self, name, key, server)
        
        self.categories = ['all', 'unwatched', 'recently_released', 'recently_added', 'recently_viewed', 'on_deck']
    
    def __str__(self):
        return "<MovieSection: %s>" % self.name

    def __repr__(self):
        return "<MovieSection: %s>" % self.name


if __name__ == '__main__':
    
    server = PlexServer("http://10.0.0.2/", 32400)
    
    server.library.shows[0].getEpisodes(category='newest')

    
    