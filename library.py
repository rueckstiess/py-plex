from section import Section
from episode import Episode
from show import Show
from movie import Movie


class Library(object):
    def __init__(self, server):
        self.server = server
    
    def __str__(self):
        return "<Library: %s>" % self.server
    
    def __repr__(self):
        return "<Library: %s>" % self.server
    
    
    @property
    def sections(self):
        """ returns a list of all sections. """
        elem = self.server.query("/library/sections")
        seclist = [Section(e, self.server) for e in elem]
        return seclist
    
    @property
    def shows(self):
        """ returns a list of all sections with type 'show'. """
        elem = self.server.query("/library/sections")
        seclist = [Section(e, self.server) for e in elem if e.attrib['type'] == 'show']
        return seclist

    @property
    def movies(self):
        """ returns a list of all sections with type 'movie'. """
        elem = self.server.query("/library/sections")
        seclist = [Section(e, self.server) for e in elem if e.attrib['type'] == 'movie']
        return seclist


    def findAll(self, name, type=None):
        query = "/search?query=%s" % name.replace(" ", "%20")
        element = self.server.query(query)
        
        items = []
        
        for e in element:
            if type and e.attrib['type'] != type:
                continue
                
            if e.attrib['type'] == 'show':
                items.append(Show(e, self.server))
            elif e.attrib['type'] == 'movie':
                items.append(Movie(e, self.server))
            elif e.attrib['type'] == 'episode':
                items.append(Episode(e, self.server))
        
        return items

    def findShows(self, name):
        return self.findAll(name, type='show')
    
    def findMovies(self, name):
        return self.findAll(name, type='movie')
    
    def findEpisodes(self, name):
        return self.findAll(name, type='episode')
    
