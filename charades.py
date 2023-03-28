#!/usr/bin/python3

import random

# Load the movie, song, and TV show lists from their respective files
with open('movies.txt', 'r') as f:
    movies = [line.strip() for line in f.readlines()]

with open('songs.txt', 'r') as f:
    songs = [line.strip() for line in f.readlines()]

with open('tv.txt', 'r') as f:
    tv_shows = [line.strip() for line in f.readlines()]

# Combine the lists into one master list
items = movies + songs + tv_shows

# Randomly choose an item from the master list
chosen_item = random.choice(items)

# Determine if the chosen item is a movie, song, or TV show
if chosen_item in movies:
    category = 'Movie'
elif chosen_item in songs:
    category = 'Song'
else:
    category = 'TV Show'

# Print the chosen item and its category
print(f'{category}: {chosen_item}')
