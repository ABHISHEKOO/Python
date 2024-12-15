import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

def open_url(url):
    webbrowser.open(url)

def google_search():
    query = search_entry.get()
    url = f"https://www.google.com/search?q={query}"
    open_url(url)

# Create the main window
root = tk.Tk()
root.title("My Web Browser")

# Create a text entry field for URL input
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a button to load the URL
load_button = tk.Button(root, text="Go", command=lambda: open_url(url_entry.get()))
load_button.pack()

# Load the Google Search icon
google_image = Image.open("google_icon.png")  # Replace with your icon path
google_photo = ImageTk.PhotoImage(google_image)

# Create a button for Google Search with the icon
google_button = tk.Button(root, image=google_photo, command=google_search)
google_button.pack()

root.mainloop()