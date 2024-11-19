import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)

root = tk.Tk()
root.title("File Explorer")

browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack()

file_path_label = tk.Label(root, text="")
file_path_label.pack()

root.mainloop()