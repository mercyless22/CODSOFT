import tkinter as tk
from tkinter import ttk, messagebox, Scrollbar
from tkcalendar import Calendar, DateEntry  # For calendar widget
from datetime import datetime, timedelta  # Import datetime module for date handling

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Manager")
        self.root.geometry("800x600")

        self.tasks = []
        self.due_today_tasks = []
        self.overdue_tasks = []

        # Frames
        self.header_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.header_frame.pack(fill="both", pady=10)

        self.task_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.task_frame.pack(fill="both", padx=20, pady=10)

        self.function_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.function_frame.pack(fill="both", padx=20, pady=10)

        self.list_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.list_frame.pack(fill="both", padx=20, pady=10, expand=True)

        # Header Label
        self.header_label = ttk.Label(self.header_frame, text="Todo List", font=("Arial", 24), background="#FAEBD7", foreground="#8B4513")
        self.header_label.pack(pady=10)

        # Task Entry
        self.task_label = ttk.Label(self.task_frame, text="Enter Task:", font=("Arial", 12), background="#FAEBD7", foreground="#000000")
        self.task_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.task_entry = ttk.Entry(self.task_frame, font=("Arial", 12), width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Due Date Entry using Calendar widget
        self.due_date_label = ttk.Label(self.task_frame, text="Due Date:", font=("Arial", 12), background="#FAEBD7", foreground="#000000")
        self.due_date_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.due_date_entry = DateEntry(self.task_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=10)

        # Add Task Button
        self.add_button = ttk.Button(self.function_frame, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10, pady=10)

        # Update Task Button
        self.update_button = ttk.Button(self.function_frame, text="Update Task", width=20, command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=10, pady=10)

        # Task Listbox
        self.task_label = ttk.Label(self.list_frame, text="Tasks:", font=("Arial", 12, "bold"), background="#FAEBD7", foreground="#000000")
        self.task_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.task_listbox = tk.Listbox(self.list_frame, width=70, height=5, selectmode="SINGLE", background="#FFFFFF", foreground="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.task_scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.task_listbox.yview)
        self.task_scrollbar.grid(row=1, column=1, sticky='ns')
        self.task_listbox.config(yscrollcommand=self.task_scrollbar.set)

        self.task_listbox.bind("<Double-1>", self.load_task_to_edit)

        # Due Today Tasks Listbox
        self.due_today_label = ttk.Label(self.list_frame, text="Due Today Tasks:", font=("Arial", 12, "bold"), background="#FAEBD7", foreground="#000000")
        self.due_today_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.due_today_listbox = tk.Listbox(self.list_frame, width=70, height=5, background="#F0F8FF", foreground="#000000")
        self.due_today_listbox.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        self.due_today_scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.due_today_listbox.yview)
        self.due_today_scrollbar.grid(row=1, column=3, sticky='ns')
        self.due_today_listbox.config(yscrollcommand=self.due_today_scrollbar.set)

        # Overdue Tasks Listbox
        self.overdue_label = ttk.Label(self.list_frame, text="Overdue Tasks:", font=("Arial", 12, "bold"), background="#FAEBD7", foreground="#000000")
        self.overdue_label.grid(row=0, column=4, padx=10, pady=10, sticky="w")

        self.overdue_listbox = tk.Listbox(self.list_frame, width=70, height=5, background="#FFDAB9", foreground="#000000")
        self.overdue_listbox.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

        self.overdue_scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.overdue_listbox.yview)
        self.overdue_scrollbar.grid(row=1, column=5, sticky='ns')
        self.overdue_listbox.config(yscrollcommand=self.overdue_scrollbar.set)

        # Delete Task Button
        self.del_button = ttk.Button(self.function_frame, text="Delete Task", width=20, command=self.delete_task)
        self.del_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete All Tasks Button
        self.del_all_button = ttk.Button(self.function_frame, text="Delete All Tasks", width=20, command=self.delete_all_tasks)
        self.del_all_button.grid(row=2, column=1, padx=10, pady=10)

        # Exit Button
        self.exit_button = ttk.Button(self.function_frame, text="Exit", width=20, command=self.root.destroy)
        self.exit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Categorize tasks based on due date
        self.categorize_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        due_date = self.due_date_entry.get_date()

        if not task:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        self.tasks.append((task, due_date))
        self.task_listbox.insert("end", f"{task} (Due: {due_date})")

        self.task_entry.delete(0, "end")
        self.due_date_entry.delete(0, "end")

        self.categorize_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a task to update.")
            return

        updated_task = self.task_entry.get().strip()
        updated_due_date = self.due_date_entry.get_date()

        if not updated_task:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        index = selected_index[0]
        self.tasks[index] = (updated_task, updated_due_date)
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, f"{updated_task} (Due: {updated_due_date})")

        self.task_entry.delete(0, "end")
        self.due_date_entry.delete(0, "end")

        self.categorize_tasks()

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

        self.categorize_tasks()

    def delete_all_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, "end")
        self.due_today_listbox.delete(0, "end")
        self.overdue_listbox.delete(0, "end")

    def load_task_to_edit(self, event):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            return

        index = selected_index[0]
        task, due_date = self.tasks[index]
        self.task_entry.delete(0, "end")
        self.task_entry.insert(0, task)
        self.due_date_entry.delete(0, "end")
        self.due_date_entry.set_date(due_date)

    def categorize_tasks(self):
        self.due_today_tasks.clear()
        self.overdue_tasks.clear()

        today = datetime.now().date()

        for task, due_date in self.tasks:
            if due_date < today:
                self.overdue_tasks.append((task, due_date))
            elif due_date == today:
                self.due_today_tasks.append((task, due_date))

        self.update_due_listbox()

    def update_due_listbox(self):
        self.due_today_listbox.delete(0, "end")
        self.overdue_listbox.delete(0, "end")

        if self.due_today_tasks:
            for task, due_date in self.due_today_tasks:
                self.due_today_listbox.insert("end", f"{task} (Due: {due_date})")

        if self.overdue_tasks:
            for task, due_date in self.overdue_tasks:
                self.overdue_listbox.insert("end", f"{task} (Due: {due_date})")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    app.run()
