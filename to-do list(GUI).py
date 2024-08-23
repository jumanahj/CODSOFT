import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)  # Clear the entry field after adding the task
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to complete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=52)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(pady=5)

button_complete_task = tk.Button(root, text="Complete Task", command=complete_task)
button_complete_task.pack(pady=5)

button_clear_tasks = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
button_clear_tasks.pack(pady=5)

# Ensure the focus is set to the entry widget at the start
entry_task.focus_set()

# Run the application
root.mainloop()
