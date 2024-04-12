import tkinter as tk

class NotePadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Pad App")
        self.root.geometry("600x400")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create file menu
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Create text area
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill="both", expand=1)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        # Open file dialog
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        # Save file dialog
        file_path = tk.filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = NotePadApp(root)
    root.mainloop()
