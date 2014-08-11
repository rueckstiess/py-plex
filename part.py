class Part(object):

    def __init__(self, element, server):
        self.element = element
        try:
            self.container = element.attrib['container']
            'The container format for example mkv'
            self.size = element.attrib['size']
            'Size in bytes'
            self.duration = element.attrib['duration']
            'Duration in seconds'
            self.key = element.attrib['key']
            'This is the url to the file on the server'
            self.file = element.attrib['file']
            'This is the absolute path on the server'
        except KeyError as e:
            print "Missing key in element: ", e.message

    def __str__(self):
        return "<Part)>"

    def __repr__(self):
        return "<Part>"

