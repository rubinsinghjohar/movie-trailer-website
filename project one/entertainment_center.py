__author__ = 'rubinsingh'
from media import movie

#creating movie objects and assigning them to variables
movieOne = movie(title="Speed 1",
                 poster_image_url="http://ia.media-imdb.com/images/M/MV5BNzczNDQyMTc2MF5BMl5BanBnXkFtZTgwNjI2NzQxMTE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                 trailer_youtube_url="https://www.youtube.com/watch?v=Fk4A1AY10U0")
movieTwo = movie(title="Who Framed Roger Rabbit",
                 poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTgxOTE1NjA0OV5BMl5BanBnXkFtZTcwODM3MTYxMQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
                 trailer_youtube_url="https://www.youtube.com/watch?v=6hSI5wTtUX8"
                 )
movieThree = movie(title="Hot Tub Time Machine 1",
                   poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTQwMjExODA4Ml5BMl5BanBnXkFtZTcwNTYwMDYxMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                   trailer_youtube_url="https://www.youtube.com/watch?v=_TXNEE6SaoI")

#creating a list to make available to fresh_tomatoes.py
movies = []
movies.append(movieOne)
movies.append(movieTwo)
movies.append(movieThree)