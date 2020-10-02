import imdb                      # importing the module
ia = imdb.IMDb()                 # creating instance of IMDB
print("=======================")
name = input("Enter movie, tv series name : ")                # movie name
search = ia.search_movie(name)   # searching the movie
lst = list()		# defining a list
lst1 = list()
lst2 = list()
for j in range(len(search)) :
    id = search[j].movieID
    lst1.append(search[j]["title"] + " : " + id)
    lst2.append(id)
print(lst1)
print("====================================")
print("As there might me many unwanted results. Please select the movie you want the plot of")
print("\n")
movie = input("Enter the id of the movie or tv series whose plot you want : ")
index = lst2.index(movie)
Movie = search[index]
ia.update(Movie, info = ["plot"])		# to get the plot of the movie
print(Movie["plot"])
print("\n")
print("Cast of the movie or tv series : ")
movies = ia.get_movie(movie)
cast = movies["cast"]		# to get the cast of the movie
for i in cast :
    actor = i
    print(actor)
print("\n")
print("Director of film or writer of series : ")
for director in movies["directors"] :			# try and except is used to prevent error messages that show up while compiling
	print(director["name"])
for writer in movies["writer"] :
	print(writer["name"])
print("\n")
print("Ratings : ")
rating = movies.data["rating"]
print(rating)
print("\n")
print("Genres : ")
genre = movies.data["genres"]
print(genre)
