class Movie(object):
    
    def __init__(self, element, server):
        self.server = server
        
        # browse element and extract some information
        self.key = element.attrib['key']
        self.type = 'movie'
        self.title = element.attrib['title']
        self.year = int(element.attrib['year'])
        self.summary = element.attrib['summary']
        self.viewed = ('viewCount' in element.attrib) and (element.attrib['viewCount'] == '1')
        self.offset = int(element.attrib['viewOffset']) if 'viewOffset' in element.attrib else 0
        self.file = element.find('.Media/Part').attrib['file']
    
    def __str__(self):
        return "<Movie: %s (%s)>" % (self.title, self.year)
    
    def __repr__(self):
        return "<Movie: %s (%d)>" % (self.title, self.year)
    
    
