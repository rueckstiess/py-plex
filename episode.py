class Episode(object):
    
    def __init__(self, element, server):
        self.server = server
        self.key = element.attrib['key']
        self.type = 'episode'
        self.title = element.attrib['title']
        self.summary = element.attrib['summary']
        self.index = int(element.attrib['index'])
        
        self.viewed = ('viewCount' in element.attrib) and (element.attrib['viewCount'] == '1')
        self.offset = int(element.attrib['viewOffset']) if 'viewOffset' in element.attrib else 0
        self.file = element.find('.Media/Part').attrib['file']
    
    def __str__(self):
        return "<Episode: %s (%d)>" % (self.title, self.index)
        
    def __repr__(self):
        return "<Episode: %s (%d)>" % (self.title, self.index)

    