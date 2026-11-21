
import tkinter as tk
from tkinter import ttk

WIDTH = 800
HEIGHT = 600

class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Dining philosophers problem")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg='paleturquoise1')
        self.root.resizable(False, False)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        self.turn_status_label = tk.Label(
            self.root,
            text=f"Tura X | Status: Działa",
            bg='gray10',
            fg='lightgreen',
            anchor='center',
            justify='center',
            font=('Arial', 15),
            height=2
        )

        self.turn_status_label.grid(column=0, row=0, sticky='ew', columnspan=2)


        self.side_panel = tk.Frame(self.root, bg='springgreen3', width=200, height=HEIGHT)
        self.side_panel.grid(column=0, row=1, columnspan=2, sticky='w')
        self.side_panel.grid_propagate(False)

        tk.Label(self.side_panel,
                 text="Wybierz metodę:",
                font=("Times New Roman", 15),
                 bg='springgreen3'
                    ).grid(column=0, row=1, sticky='w', columnspan=2, pady=15)


        chosen_method = ttk.Combobox(
            self.side_panel,
            height= 5,
            width= 10,
            font= 'Helvetica',
            background='aquamarine',
            foreground= 'gray10',
            state='readonly'
        )
        chosen_method['values'] = (
            'MetodaA',
            'MetodaB',
        )
        chosen_method.current(0)
        chosen_method.grid(column=0, row=2, pady=5, padx=5, sticky='ew' )

        tk.Button(
            self.side_panel,
            text="Start",
            command=self.start,
            fg = 'gray10',
            bg = 'gray60',
            font=('Helvetica',15),
            width=5,
        ).grid(column=0, row=3)


        tk.Button(
            self.side_panel,
            text="Stop",
            command=self.start,
            fg='gray10',
            bg='gray60',
            font=('Helvetica', 15),
            width=5,
        ).grid(column=0, row=5)


        root.mainloop()

    def start(self):
        print("Start")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Gui(root)


    root.mainloop()