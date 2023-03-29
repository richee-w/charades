#!/usr/bin/python3
#
# This program is licensed under the GNU General Public License v3.0.
# See <https://www.gnu.org/licenses/gpl-3.0.en.html> for more details.

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

class RadioButtonWithMessage(tk.Frame):
    def __init__(self, master=None, text='', font=None, variable=None, value=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(anchor='w')

        self.radio_button = tk.Radiobutton(self, variable=variable, value=value)
        self.radio_button.pack(side='left')

        self.message = tk.Message(self, text=text, font=font, width=500)
        self.message.pack(side='left')

# Create a GUI window and display the chosen item and its category
window = tk.Tk()
window.title('Random Item Generator')

frame1 = tk.Frame(window)
frame1.pack(anchor='w', padx=10)

# Create a canvas to hold the frame and scrollbar
canvas = tk.Canvas(frame1)
canvas.pack(side='left', fill='both', expand=True)

# Create a scrollbar and attach it to the canvas
scrollbar = tk.Scrollbar(frame1, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the radio buttons
frame2 = tk.Frame(canvas)

# Add the frame to the canvas
canvas.create_window((0, 0), window=frame2, anchor='nw')

# Create a list to store the radio buttons
radio_buttons = []

# Create a variable to store the state of the radio buttons
radio_var = tk.StringVar(value='0')

def generate_items():
    global last_item

    # Clear any existing radio buttons from the previous set of items
    for radio_button in radio_buttons:
        radio_button.destroy()

    # Choose 5 random items from the master list
    chosen_items = random.sample(items, 5)

    # Add an extra item called "None of these"
    chosen_items.append("None of these")

    # Create a radio button for each chosen item
    for chosen_item in chosen_items:
        # Determine if the chosen item is a movie, song, TV show or "None of these"
        if chosen_item == "None of these":
            category = ""
        elif chosen_item in movies:
            category = 'Movie'
        elif chosen_item in songs:
            category = 'Song'
        else:
            category = 'TV Show'

        # Create a radio button for the chosen item and its category
        radio_button_text = f'{category} {chosen_item}'.strip() if category else chosen_item
        radio_button = RadioButtonWithMessage(frame2, text=radio_button_text, font=('Arial', 20), variable=radio_var, value=chosen_item)
        radio_button.pack(anchor='w')

        # Add the radio button to the list of radio buttons
        radio_buttons.append(radio_button)

    # Update the scroll region of the canvas
    frame2.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

# Add button to prompt user for another set of items
button1 = tk.Button(window, text='Generate Another Set of Items', font=('Arial', 15), command=generate_items)
button1.pack(side='left', padx=50)

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
