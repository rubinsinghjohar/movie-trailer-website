__author__ = 'rubinsingh'
class movie:
    """The movie object holds information about a single movie
    Instance Variables:
        title - denotes the title of the movie
        poster_image_url - a link to the poster art of the movie
        trailer_youtube_url - a url to the youtube trailer for the movie
    """
    def __init__(self, title=None, poster_image_url=None, trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url