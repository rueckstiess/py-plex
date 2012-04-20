from season import Season
from episode import Episode

class Show(object):
    def __init__(self, element, server):
        self.server = server
        self.type = 'show'
        self.key = element.attrib['key']
        self.title = element.attrib['title']
        self.summary = element.attrib['summary']
        
        self.genres = [e.attrib['tag'] for e in element.findall('.Genre')]
        self.collections = [e.attrib['tag'] for e in element.findall('.Collection')]
        
        self.seasons_ = []
    
    def __len__(self):
        """ returns the number of seasons of this show. """
        return len(self.seasons)
    
    def __iter__(self):
        """ iterate over all seasons. """
        for s in self.seasons:
            yield s
    
    def __str__(self):
        return "<Show: %s>" % self.title
    
    def __repr__(self):
        return "<Show: %s>" % self.title
    
    @property
    def seasons(self):
        """ property that returns a list to all seasons of the show. caches it's value after first call. """
        if not self.seasons_:
            element = self.server.query(self.key)
            self.seasons_ = [Season(e, self.server) for e in element if ('type' in e.attrib) and (e.attrib['type'] == 'season')]
            
        return self.seasons_


    def getSeason(self, num):
        """ returns the season with the index number `num` or None if it doesn't exist. """
        return next((s for s in self.seasons if s.index == num), None)

    def getAllEpisodes(self):
        """ returns a list of all episodes of the show independent of seasons. """
        key = '/'.join(self.key.split('/')[:-1]) + '/allLeaves'
        element = self.server.query(key)
        episodes = [Episode(e, self.server) for e in element if ('type' in e.attrib) and (e.attrib['type'] == 'episode')]
        return episodes
    
    def getNextUnwatchedEpisode(self):
        """ returns the episode that follows the last watched episode in the show over 
            all seasons. if all are watched, return None. 
        """
        key = '/'.join(self.key.split('/')[:-1]) + '/allLeaves'
        element = self.server.query(key)
        
        prev = None
        for e in reversed(element):
            if ('viewCount' in e.attrib) and (e.attrib['viewCount'] == '1'):
                if prev == None:
                    return None
                else:
                    return Episode(prev, self.server)
            prev = e
        return Episode(element[0], self.server)
        

    