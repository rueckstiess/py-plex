from media import Media
class Video(object):

    def __init__(self, element, server):
        self.element = element
        self.server = server

        # browse element and extract some information
        self.key = element.attrib['key']
        self.type = 'video'
        self.title = element.attrib['title']
        self.summary = element.attrib['summary']

        self.viewed = ('viewCount' in element.attrib) and (element.attrib['viewCount'] >= '1')
        self.offset = int(element.attrib['viewOffset']) if 'viewOffset' in element.attrib else 0

        self.media = [Media(e, self.server) for e in element.findall('.Media')]

    def __str__(self):
        return "<Video: %s>" % (self.key)

    def __repr__(self):
        return "<Video: %s>" % (self.key)
