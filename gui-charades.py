#!/usr/bin/python3

import random
import tkinter as tk

# Load the movie, song, and TV show lists from their respective files
with open('movies.txt', 'r') as f:
    movies = [line.strip() for line in f.readlines()]

with open('songs.txt', 'r') as f:
    songs = [line.strip() for line in f.readlines()]

with open('tv.txt', 'r') as f:
    tv_shows = [line.strip() for line in f.readlines()]

# Combine the lists into one master list
items = movies + songs + tv_shows

last_item = None

while True:
    # Randomly choose an item from the master list that is not the same as the last item
    chosen_item = random.choice([item for item in items if item != last_item])

    # Determine if the chosen item is a movie, song, or TV show
    if chosen_item in movies:
        category = 'Movie'
    elif chosen_item in songs:
        category = 'Song'
    else:
        category = 'TV Show'

    # Create a GUI window and display the chosen item and its category
    window = tk.Tk()
    window.title('Random Item Generator')

    label1 = tk.Label(window, text=f'{category}: {chosen_item}', font=('Arial', 20))
    label1.pack(pady=5)

    # Add buttons to prompt user for another item or to close the program
    button1 = tk.Button(window, text='Generate Another Item', font=('Arial', 15), command=window.destroy)
    button1.pack(side='left', padx=50)

    button2 = tk.Button(window, text='Exit Program', font=('Arial', 15), command=exit)
    button2.pack(side='right', padx=50)

    # Set minimum size of window to be large enough to display all items
    window.update_idletasks()
    window.geometry(f'{max(800, label1.winfo_width() + 100)}x{max(200, label1.winfo_height() + 30)}')

    # Make sure "x" button closes the window properly
    window.protocol("WM_DELETE_WINDOW", exit)

    # Set position of window to center of screen
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

    # Keep window always on top
    window.wm_attributes("-topmost", True)

    window.mainloop()