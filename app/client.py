import tkinter as tk
from tkinter import ttk
import service
from datetime import date
import debug

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("400x400")

        current_date = date.today()

        self.board = tk.StringVar()
        self.board.set("Board")
        board_options = service.getListOfBoardOptions()
        self.board_menu = ttk.OptionMenu(self.root, self.board, *board_options)
        self.board_menu.pack()

        # Create a dropdown menu
        tk.Label(self.root, text="Select a label").pack()
        self.label = tk.StringVar()
        self.label.set("Label")
        label_options = service.getListOfLabelOptions(self.board.get())
        self.label_menu = ttk.OptionMenu(self.root, self.label, *label_options)
        self.label_menu.pack()

        # Create 3 dropdown menus for day, month, year
        tk.Label(self.root, text="Select a date").pack()
        self.day = tk.StringVar()
        self.day.set("Day")
        day_options = ["Day"] + [str(i) for i in range(1, 32)]
        self.day_menu = ttk.OptionMenu(self.root, self.day, *day_options)
        self.day_menu.pack()

        self.month = tk.StringVar()
        self.month.set("Month")
        month_options = [current_date.month] + [str(i) for i in range(1, 13)]
        self.month_menu = ttk.OptionMenu(self.root, self.month, *month_options)
        self.month_menu.pack()

        self.year = tk.StringVar()
        self.year.set("Year")
        year_options = [current_date.year] + [str(i) for i in range(2023, 2024)]
        self.year_menu = ttk.OptionMenu(self.root, self.year, *year_options)
        self.year_menu.pack()

        self.list = tk.StringVar()
        self.list.set("List")
        list_options = service.getListOfListOptions()
        self.list_menu = ttk.OptionMenu(self.root, self.list, *list_options)
        self.list_menu.pack()

        # Create a textbox
        tk.Label(self.root, text="Enter a name").pack()
        self.name = tk.Text(self.root, height=5, width=60)
        self.name.pack()

        # Create a submit button
        tk.Button(self.root, text="Submit", command=self.submit).pack()

    def submit(self):
        # Get selected values from dropdown menus
        card = service.Card(
            self.board.get(),
            self.list.get(), 
            self.name.get("1.0", "end"), 
            self.label.get(),
            self.day.get(), self.month.get(), self.year.get())

        # Log selected values
        if debug.DEBUG:
            print("List:", card.list)
            print("ListId", card.listId)
            print("Label:", card.label)
            print("LabelId:", card.labelId)
            print("Date:", card.due)
            print("Name:", card.name)
            
        # Clear textbox
        self.name.delete("1.0",tk.END)

        service.createNewCard(card)

if __name__ == "__main__":
    app = MainWindow(tk.Tk())
    app.root.mainloop()