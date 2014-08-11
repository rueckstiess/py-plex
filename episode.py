from video import Video
from media import Media
class Episode(Video):

    def __init__(self, element, server):
        super(Episode, self).__init__(element, server)

        self.type = 'episode'
        try:
            self.index = int(element.attrib['index'])
        except KeyError as e:
            print "Missing key in element: ", e.message

    def __str__(self):
        return "<Episode: %s (%d)>" % (self.title, self.index)

    def __repr__(self):
        return "<Episode: %s (%d)>" % (self.title, self.index)

