from part import Part
class Media(object):

    def __init__(self, element, server):
        self.server = server
        self.element = element
        self.part = Part(element.find('.Part'), self.server)
        try:
            self.videoFrameRate = element.attrib['videoFrameRate']
            self.videoCodec = element.attrib['videoCodec']
            self.container = element.attrib['container']
            self.bitrate = int(element.attrib['bitrate'])
            self.height = int(element.attrib['height'])
            self.width = int(element.attrib['width'])
            self.videoResolution = element.attrib['videoResolution']
            self.audioCodec = element.attrib['audioCodec']
        except KeyError as e:
            print "Missing key in element: ", e.message

    def __str__(self):
        return "<Media)>"

    def __repr__(self):
        return "<Media>"

