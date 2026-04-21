import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ── Database Setup ──────────────────────────────
conn = sqlite3.connect('admission.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        name   TEXT NOT NULL,
        dob    TEXT,
        gender TEXT,
        course TEXT,
        email  TEXT,
        phone  TEXT
    )
''')
conn.commit()

# ── Insert Function ──────────────────────────────
def submit():
    name   = entry_name.get()
    dob    = entry_dob.get()
    gender = gender_var.get()
    course = course_combo.get()
    email  = entry_email.get()
    phone  = entry_phone.get()

    if not all([name, dob, gender, course, email, phone]):
        messagebox.showwarning('Error', 'Fill all fields!')
        return

    cursor.execute('''
        INSERT INTO students (name, dob, gender, course, email, phone)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, dob, gender, course, email, phone))
    conn.commit()
    messagebox.showinfo('Success', f'{name} admitted successfully!\nRecord saved to DB.')
    for e in [entry_name, entry_dob, entry_email, entry_phone]:
        e.delete(0, 'end')

def view_records():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    info = '\n'.join([f'{r[0]}. {r[1]} | {r[4]} | {r[5]}' for r in rows])
    messagebox.showinfo('Records', info if info else 'No records found.')

# ── GUI ─────────────────────────────────────────
root = tk.Tk()
root.title('Admission Form + SQLite DB')
root.geometry('480x440')

tk.Label(root, text='ADMISSION FORM (with Database)',
         font=('Arial',13,'bold'), bg='darkblue', fg='white').pack(fill='x', pady=5)

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(fill='both')

labels = ['Full Name', 'Date of Birth', 'Email', 'Phone']
entries_map = {}
for i, lbl in enumerate(labels):
    tk.Label(frame, text=lbl+':', anchor='w').grid(row=i, column=0, sticky='w', pady=5)
    e = tk.Entry(frame, width=30)
    e.grid(row=i, column=1, padx=10, pady=5)
    entries_map[lbl] = e

entry_name  = entries_map['Full Name']
entry_dob   = entries_map['Date of Birth']
entry_email = entries_map['Email']
entry_phone = entries_map['Phone']

tk.Label(frame, text='Gender:', anchor='w').grid(row=4, column=0, sticky='w', pady=5)
gender_var = tk.StringVar(value='Male')
gf = tk.Frame(frame); gf.grid(row=4, column=1, sticky='w', padx=10)
for g in ['Male','Female','Other']:
    tk.Radiobutton(gf, text=g, variable=gender_var, value=g).pack(side='left')

tk.Label(frame, text='Course:', anchor='w').grid(row=5, column=0, sticky='w', pady=5)
course_combo = ttk.Combobox(frame, width=27,
    values=['BCA','BBA','B.Tech','B.Sc','B.Com'])
course_combo.grid(row=5, column=1, padx=10, pady=5)
course_combo.set('Select Course')

bf = tk.Frame(root); bf.pack(pady=8)
tk.Button(bf, text='Submit & Save', command=submit,
          bg='green', fg='white', width=14).pack(side='left', padx=8)
tk.Button(bf, text='View Records', command=view_records,
          bg='steelblue', fg='white', width=14).pack(side='left', padx=8)

root.mainloop()
conn.close()
