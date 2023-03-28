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

# Create a GUI window and display the chosen item and its category
window = tk.Tk()
window.title('Random Item Generator')

frame1 = tk.Frame(window)
frame1.pack(pady=5)

# Create a list to store the radio buttons and their associated variables
radio_buttons = []
radio_vars = []

def generate_items():
    # Clear any existing radio buttons from the frame
    for radio_button in radio_buttons:
        radio_button.destroy()

    # Clear the radio button and variable lists
    radio_buttons.clear()
    radio_vars.clear()

    # Randomly choose 5 items from the master list that are not the same as the last item
    chosen_items = random.sample([item for item in items if item != last_item], 5)

    # Create a radio button for each chosen item
    for chosen_item in chosen_items:
        # Determine if the chosen item is a movie, song, or TV show
        if chosen_item in movies:
            category = 'Movie'
        elif chosen_item in songs:
            category = 'Song'
        else:
            category = 'TV Show'

        # Create a variable to store the state of the radio button
        var = tk.StringVar(value='0')
        radio_vars.append(var)

        # Create a radio button for the chosen item and its category
        radio_button = tk.Radiobutton(frame1, text=f'{category}: {chosen_item}', font=('Arial', 20), variable=var, value='1')
        radio_button.pack(anchor='w')

        # Add the radio button to the list of radio buttons
        radio_buttons.append(radio_button)

# Add buttons to prompt user for another item or to close the program
button1 = tk.Button(window, text='Generate Another 5 Items', font=('Arial', 15), command=generate_items)
button1.pack(side='left', padx=50)

button2 = tk.Button(window, text='Exit Program', font=('Arial', 15), command=exit)
button2.pack(side='right', padx=50)

# Make sure "x" button closes the window properly
window.protocol("WM_DELETE_WINDOW", exit)

# Set position of window to center of screen
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

# Keep window always on top
window.wm_attributes("-topmost", True)

# Generate initial items
generate_items()

# Set minimum size of window to be large enough to display all items
window.update_idletasks()
window.geometry(f'{max(800, window.winfo_width() + 100)}x{max(200, window.winfo_height() + 30)}')

window.mainloop()
