import pickle 

metadata = {}

metadata[0] = ('A journey through the mind of an artist', 'Dustin Yellin')
metadata[1] = ('Art in the age of Instagram', 'Jia Jia Fei')
metadata[2] = ('How art can help you analyze', 'Amy E. Herman')
metadata[3] = ('Why art is important', 'Katerina Gregos')
metadata[4] = ('Every kid needs a champion', 'Rita Pierson')
metadata[5] = ('Teaching history in the 21st century', 'Thomas Ketchell')
metadata[6] = ('Why teachers teach but kids dont learn', 'Ben Richards')
metadata[7] = ('Are athletes really getting faster, better, stronger', 'David Epstein')
metadata[8] = ('The math behind basketballs wildest moves', 'Rajiv Maheswaran')
metadata[9] = ('The best teams have this secret weapon', 'Adam Grant')
metadata[10] = ('The real importance of sports', 'Sean Adams')
metadata[11] = ('A beginners guide to quantum computing', 'Shohini Ghose')
metadata[12] = ('The next step in nanotechnology', 'George Tulevski')
metadata[13] = ('The internet of things', 'Jordan Duffy')

pickle.dump(metadata, open('metadata.pkl', 'wb'))
