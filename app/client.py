import tkinter as tk
from tkinter import ttk
import api
from datetime import date

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("400x400")

        current_date = date.today()

        # Create a dropdown menu
        tk.Label(self.root, text="Select a course").pack()
        self.courses = tk.StringVar()
        self.courses.set("Personal")
        course_options = ["Personal", "CIS351", "CIS343", "HNR350", "PHY220"]
        self.course_menu = ttk.OptionMenu(self.root, self.courses, *course_options)
        self.course_menu.pack()

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

        # Create a textbox
        tk.Label(self.root, text="Enter a description").pack()
        self.description = tk.Text(self.root, height=5, width=60)
        self.description.pack()

        # Create a submit button
        tk.Button(self.root, text="Submit", command=self.submit).pack()

    def submit(self):
        # Get selected values from dropdown menus
        course = self.courses.get()
        day = self.day.get()
        month = self.month.get()
        year = self.year.get()
        description = self.description.get("1.0", "end")

        # Log selected values
        print("Course:", course)
        print("Date:", day, month, year)
        print("Description:", description)

        api.create_new_card(description, api.date_formatter(year, month, day), course)


if __name__ == "__main__":
    app = MainWindow(tk.Tk())
    app.root.mainloop()
