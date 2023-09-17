import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle
from database import cursor
from database import conn

def add_task(entry, listbox, due_date_entry):
    task = entry.get()
    if task:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        due_date = due_date_entry
        cursor.execute('INSERT INTO tasks (task_name, created_at, due_date) VALUES (?, ?, ?)', (task, current_time, due_date))
        conn.commit()
        listbox.insert("", "end", values=(task, current_time, due_date))
        entry.delete(0, tk.END)

def delete_task(listbox):
    selected_task_index = listbox.selection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        selected_task_name = listbox.item(selected_task_index, "values")[0]
        
        cursor.execute('DELETE FROM tasks WHERE task_name = ?', (selected_task_name,))
        conn.commit()
        listbox.delete(selected_task_index)


def edit_task(listbox):
    selected_task_index = listbox.selection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        selected_task_name = listbox.item(selected_task_index, "values")[0]
        selected_due_date = listbox.item(selected_task_index, "values")[2]

        selected_due_date_parts = selected_due_date.split(" ")
        selected_due_date_date = selected_due_date_parts[0]

        dialog = tk.Toplevel()
        dialog.title("Edit Task")

        style = ThemedStyle(dialog)
        style.set_theme("yaru")

        task_label = ttk.Label(dialog, text="Task New Name:")
        task_label.pack()

        task_entry = ttk.Entry(dialog, font=('Helvetica', 12))
        task_entry.insert(0, selected_task_name)
        task_entry.pack()

        due_date_label = ttk.Label(dialog, text="New Due Date (YYYY-MM-DD):")
        due_date_label.pack()

        due_date_entry = DateEntry(dialog, width=12, background='darkblue', foreground='white', borderwidth=2)
        formatted_date = datetime.datetime.strptime(selected_due_date_date, "%Y-%m-%d").strftime("%m/%d/%Y")
        due_date_entry.set_date(formatted_date) 
        due_date_entry.pack()

        save_button = ttk.Button(dialog, text='Save', command=lambda: save_edited_task(dialog, selected_task_name, listbox, selected_task_index, task_entry.get(), due_date_entry.get_date()))
        save_button.pack()


def save_edited_task(dialog, selected_task_name, listbox, selected_task_index, edited_task, edited_due_date):
    if edited_task and edited_due_date:
        cursor.execute('UPDATE tasks SET task_name = ?, due_date = ? WHERE task_name = ?', (edited_task, edited_due_date, selected_task_name))
        conn.commit()
        listbox.item(selected_task_index, values=(edited_task, listbox.item(selected_task_index, "values")[1], edited_due_date))
        dialog.destroy()