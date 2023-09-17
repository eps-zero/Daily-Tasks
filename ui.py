import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkcalendar import DateEntry
from task_manager import add_task, delete_task, edit_task
from database import cursor

def create_ui():
    
    root = tk.Tk()
    root.title('Daily Tasks')

    style = ThemedStyle(root)
    style.set_theme("equilux")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    
    style = ThemedStyle(root)
    style.set_theme("yaru")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill=tk.BOTH)
    
    listbox_frame = ttk.Frame(frame)
    listbox_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
    
    listbox = ttk.Treeview(listbox_frame, columns=("Task Name", "Created Date", "Due Date"), selectmode="browse", height=10)
    listbox.column("#0", width=0, stretch=tk.NO)
    listbox.heading("#1", text="Task Name")
    listbox.heading("#2", text="Created Date")
    listbox.heading("#3", text="Due Date")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    
    add_button = ttk.Button(frame, text='Add', command=lambda: add_task(entry=entry, due_date_entry=due_date_entry.get_date(), listbox=listbox))
    delete_button = ttk.Button(frame, text='Delete', command=lambda: delete_task(listbox=listbox))
    edit_button = ttk.Button(frame, text='Edit', command=lambda: edit_task(listbox=listbox))
    
    entry_label = ttk.Label(frame, text="Task name:")
    entry_label.pack(fill=tk.X, padx=10, pady=5)
    

    entry = ttk.Entry(frame, font=('Helvetica', 12))
    entry.pack(fill=tk.X, padx=10, pady=10, expand=True)
    
    due_date_label = ttk.Label(frame, text="Due Date:")
    due_date_label.pack(fill=tk.X, padx=10, pady=5)
    
    due_date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    due_date_entry.pack(fill=tk.X, padx=10, pady=5)
    
    add_button.pack(fill=tk.X, padx=10, pady=10)
    delete_button.pack(fill=tk.X, padx=10, pady=10)
    edit_button.pack(fill=tk.X, padx=10, pady=10)

    cursor.execute('SELECT task_name, created_at, due_date FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        listbox.insert("", "end", values=(task[0], task[1], task[2]))
    
    return root
