import tkinter as tk

class ColorChooser:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Chooser")
        self.colors = ["Red", "Green", "Blue", "Yellow", "Black", "White"]
        self.color_vars = []
        self.color_labels = []

        for i, color in enumerate(self.colors):
            var = tk.IntVar()
            chk = tk.Checkbutton(root, text=color, variable=var)
            chk.grid(row=i, column=0)
            self.color_vars.append(var)
            self.color_labels.append(chk)

        self.result_label = tk.Label(root, text="Selected colors:")
        self.result_label.grid(row=len(self.colors), column=0)

        self.get_colors_button = tk.Button(root, text="Get Selected Colors", command=self.get_colors)
        self.get_colors_button.grid(row=len(self.colors) + 1, column=0)

    def get_colors(self):
        selected_colors = [color for i, color in enumerate(self.colors) if self.color_vars[i].get()]
        self.result_label.config(text="Selected colors: " + ", ".join(selected_colors))

root = tk.Tk()
color_chooser = ColorChooser(root)
root.mainloop()