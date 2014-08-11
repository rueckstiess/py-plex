from video import Video
class Movie(Video):

    def __init__(self, element, server):
        super(Movie, self).__init__(element, server)

        self.type = 'movie'
        self.year = int(element.attrib['year'])

    def __str__(self):
        return "<Movie: %s (%s)>" % (self.title, self.year)

    def __repr__(self):
        return "<Movie: %s (%d)>" % (self.title, self.year)


