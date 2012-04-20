from server import Server

server = Server("10.0.0.2", 32400)
client = server.clients[0]
movies = server.library.movies[0]
m = movies.getContent('newest')[0]

# client.playVideo(m, m.offset)
# client.runCommand('stop')


shows = server.library.shows[0]
rock = shows.getContent('all')[0]
# print rock.title
# print rock.key

print rock.getNextUnwatchedEpisode()