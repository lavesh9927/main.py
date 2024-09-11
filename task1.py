"""Task 1 : To-Do-List
A To-Do List application is a useful project that helps users manage and organize their tasks
efficiently. This project aims to create a command-line or GUI-based application using
Python, allowing users to create, update, and track their to-do lists"""


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.tasks_listbox.pack()

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.mark_completed_button.pack()

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_tasks_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, 1):
            status = " (Completed)" if task["completed"] else ""
            self.tasks_listbox.insert(tk.END, f"{i}. {task['task']}{status}")

    def mark_task_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index]["completed"] = True
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if _name_ == "_main_":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
