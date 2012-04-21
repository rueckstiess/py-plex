class Client(object):
    
    def __init__(self, element, server):
        self.server = server
        
        self.name = element.attrib['name']
        self.address = element.attrib['address']
        self.port = element.attrib['port']
        self.version = element.attrib['version']
    
        self.navigationCommands = ['moveUp', 'moveDown', 'moveLeft', 'moveRight', 'pageUp', 'pageDown', 'nextLetter', 'previousLetter', 'select', 'back', 'contextMenu', 'toggleOSD']
        self.playbackCommands = ['play', 'pause', 'stop', 'rewind', 'fastForward', 'stepForward', 'bigStepForward', 'stepBack', 'bigStepBack', 'skipNext', 'skipPrevious']
        self.applicationCommands = ['playFile', 'playMedia', 'screenshot', 'sendString', 'sendKey', 'sendVirtualKey']
    
    def runCommand(self, command):
        # strip trailing slash
        if command[0] == '/':
            command = command[1:]
        
        if command in self.navigationCommands:
            self.server.execute("/system/players/%s/navigation/%s" % (self.address, command))
        elif command in self.playbackCommands:
            self.server.execute("/system/players/%s/playback/%s" % (self.address, command))
        elif command.split('?')[0] in self.applicationCommands:
            print "/system/players/%s/application/%s" % (self.address, command)
            self.server.execute("/system/players/%s/application/%s" % (self.address, command))
        else:
            raise ValueError("command not valid.")
        
        
    def playVideo(self, video, offset=0):
        path = "http://%s:%d%s" % (self.server.address, self.server.port, video.key)
        command = "/playMedia?key=%s&path=%s" % (video.key, path)
        if offset:
            command += "&viewOffset=%d" % offset
        self.runCommand(command)
    
        