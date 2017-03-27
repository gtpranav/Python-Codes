import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Toys come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc") 

interstellar = media.Movie("Interstellar",
                           "Man goes in other universe to find solution to human problem",
                           "https://en.wikipedia.org/wiki/Interstellar_(film)#/media/File:Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=ePbKGoIGAXY")
gaurdians_of_galaxy = media.Movie("Gaurdians of the galaxy",
                                  "Human and some other creatures saves unvierse",
                                  "https://en.wikipedia.org/wiki/Guardians_of_the_Galaxy_(film)#/media/File:GOTG-poster.jpg",
                                  "https://www.youtube.com/watch?v=89q_HH-3ghk")
fifty_first_dates = media.Movie("50 First dates",
                             "Man falls in love with woman who forgets her past every day she wakes up",
                             "https://en.wikipedia.org/wiki/50_First_Dates#/media/File:50FirstDates.jpg",
                             "https://www.youtube.com/watch?v=ErjP5xMTc8I")
midnight_in_paris = media.Movie("Midnight in paris",
                                "Man discovers taht every midnight a car stops and takes him to past while on vacation in paris.",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=5nOF93SzX6s")

movies = [toy_story, interstellar, gaurdians_of_galaxy, fifty_first_dates, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)
