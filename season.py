from episode import Episode

class Season(object):

    def __init__(self, element, server):
        self.key = element.attrib['key']
        self.server = server
        self.type = 'season'
        self.title = element.attrib['title']
        self.index = int(element.attrib['index'])
        self.episodes_ = []

    def __len__(self):
        return self.size

    def __iter__(self):
        for e in self.episodes:
            yield e

    def __str__(self):
        return "<Season: %d>" % self.index

    def __repr__(self):
        return "<Season: %d>" % self.index

    def getEpisode(self, num):
        pass

    @property
    def episodes(self):
        if not self.episodes_:
            element = self.server.query(self.key)
            self.episodes_ = [Episode(e, self.server) for e in element if ('type' in e.attrib) and (e.attrib['type'] == 'episode')]

        return self.episodes_

