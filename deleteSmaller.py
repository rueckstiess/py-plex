from server import Server

server = Server("127.0.0.1", 32400)
tobedeleted = []
dryRun = False

import os
for show in server.library.shows[0].getContent('all'):
        oldres = 0
        oldpath = ''
        for episode in show.getAllEpisodes():
            for med in episode.media:
                try:
                    newres = int(med.videoResolution)
                except:
                    continue
                newpath = med.part.file
                if oldpath == '':
                    oldres = newres
                    oldpath = newpath
                    continue
                if oldres < newres:
                    tobedeleted.append(oldpath)
                    oldres = newres
                    oldpath = newpath
                else:
                    tobedeleted.append(newpath)
if dryRun:
    print tobedeleted
else:
    for delete in tobedeleted:
            try:
                os.remove(delete)
            except Exception:
                    print "Could not delete %s" % delete
