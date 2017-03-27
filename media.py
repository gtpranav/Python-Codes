import webbrowser

class Movie():

    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story_line = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
         webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    
