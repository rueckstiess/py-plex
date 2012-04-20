from movie import Movie
from show import Show
from episode import Episode

class Section(object):
    def __init__(self, element, server):
        self.title = element.attrib['title']
        self.key = int(element.attrib['key'])
        self.type = element.attrib['type']
        self.server = server
    
        # get container and categories
        self.container = server.query("/library/sections/%d" % self.key)
        self.categories = {d.attrib['key']:d.attrib['title'] for d in self.container if not 'search' in d.attrib}

    def __str__(self):
        return "<Section: %s>" % self.title

    def __repr__(self):
        return "<Section: %s>" % self.title
    
    def getCategories(self):
        return self.categories
    
    def getSubCategories(self, category):
        assert category in self.categories.keys(), \
            "category must be one of the following: %s" % ", ".join(self.categories.keys())
        
        container = self.server.query("/library/sections/%d/%s" % (self.key, category))
        if len(container) > 0 and not 'type' in container[0].attrib:
            # get all subcategories and return them
            subcat = {d.attrib['key']:d.attrib['title'] for d in container}
            return subcat
        else:
            return None
    
    def getContent(self, category='all', subCategory=None):
        assert category in self.categories.keys(), \
            "category must be one of the following: %s" % ", ".join(self.categories.keys())
        
        if subCategory:
            subCategory = str(subCategory)
        subCategories = self.getSubCategories(category)
        
        assert (subCategory == None and subCategories == None) or (subCategory in subCategories.keys()), \
            "subCategory must be one of the following: %s. use method getSubCategories() to get key/title" \
            " pairs." % ", ".join(subCategories.keys())
        
        if subCategory == None:
            container = self.server.query("/library/sections/%d/%s" % (self.key, category))
        else:
            container = self.server.query("/library/sections/%d/%s/%s" % (self.key, category, subCategory))
        
        content = []
        for e in container:
            if not 'type' in e.attrib:
                continue
            type_ = e.attrib['type']
            if type_ == 'movie':
                # append movie
                obj = Movie(e, self.server)
            if type_ == 'show':                
                # append show
                obj = Show(e, self.server)
            if type_ == 'episode':
                obj = Episode(e, self.server)
            
            content.append(obj)
             
        return content
