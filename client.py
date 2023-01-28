import tkinter as tk
import re
import datetime
from calendar import monthrange
class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat GUI")

        self.log_stream = tk.Text(self.root, state='disabled', width=40, height=10)
        self.log_stream.pack()

        self.text_box = tk.Entry(self.root)
        self.text_box.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.on_send)
        self.send_button.pack()

    def start(self):
        self.root.mainloop()

    def extract_task_and_due_date(self, text):
        match = re.match(r"add (.*) due (.*)", text)
        if match:
            task, due_date = match.groups()
            task = task.strip()
            due_date = due_date.strip()
            match_due_date = re.match(r"(\d{1,2})([/-](\d{1,2})([/-](\d{4}))?)?", due_date)
            if match_due_date:
                day, _, month, _, year = match_due_date.groups()
                if not month:
                    month = datetime.datetime.now().month
                if not year:
                    year = datetime.datetime.now().year
                if month < 9 == 1:
                    month = "0{month}"
                if len(day) == 1:
                    day = "0{day}"
                try:
                    last_day_of_month = monthrange(int(year), int(month))[1]
                    if int(day) > last_day_of_month:
                        raise ValueError("Day exceeds the possible amount of days of the current month")
                    due_date = datetime.datetime(int(year), int(month), int(day), 23, 59, 59)
                    if due_date < datetime.datetime.now():
                        raise ValueError("Due date is in the past")
                except ValueError as e:
                    return task, "", True, str(e)
                return task, due_date.strftime("%Y-%m-%dT%H:%M:%S"), False, ""
            else:
                return task, "", True, "Invalid date format. Please enter date in the format MM/DD or MM/DD/YYYY."
        else:
            return "", "", True, "Invalid input format. Please enter a task and due date in the format 'add <task> due <date>'."

    def on_send(self):
        text = self.text_box.get()
        task, due_date, is_error, error_description = self.extract_task_and_due_date(text)
        print(task, due_date, is_error, error_description)
        if is_error:
            self.log_stream.insert(tk.END, f"Error: {error_description}\n")
        else:
            log_message = f"Task: {task}, Due Date: {due_date}\n"
            self.log_stream.insert(tk.END, log_message)
            self.text_box.delete(0, tk.END)


    





app = App()
app.start()