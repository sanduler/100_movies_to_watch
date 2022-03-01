# Name: Ruben Sanduleac
# Date: February 28, 2022
# Description: This program scrapes the top 100 movies of all time from a website.
#              Then, the program generate a text file called `movies.txt` that lists
#              the movie titles in ascending order (starting from 1).

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# get a response from the webpage
response = requests.get(URL)
# convert the response to text
top_movies = response.text
# create a new BeautifulSoup object for this website and parse the text
soup = BeautifulSoup(top_movies, "html.parser")
# create a list of all the top movies including the ranking
movie_titles = soup.find_all(name="h3", class_="title")
# print(movie_titles)
movie_rankings = []
movie_listings = []
for article_tag in movie_titles:
    # gets the integer ranking for each movie
    movie_ranking = int(article_tag.get_text().split()[0][:-1])
    # append to the list
    movie_rankings.append(movie_ranking)
    # seperates the movie list from the string ratings
    movie_list = article_tag.get_text().split(") ")[-1]
    # append to the list
    movie_listings.append(movie_list)

# reverse the list so the rankings and the movie list are in ascending order
int_movie_rankings = movie_rankings[::-1]
string_movie_listings = movie_listings[::-1]

# open and create a new file if doesn't exist
file = open("movies.txt", "w")

# loop through each index in the rantings and movie list
for index in range(len(int_movie_rankings)):
    # use an f string to write the movies to a file as a well
    # as use the index of the movie location in the movie_listings
    file.write(f"{int_movie_rankings[index]}) {string_movie_listings[index]} \n")
# close the opened file.
file.close()