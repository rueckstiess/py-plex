from server import Server

server = Server("http://10.0.0.2/", 32400)


shows = server.library.shows[0]

# print shows.getCategories()
# print shows.getSubCategories('collection')

print shows.getContent('all')
