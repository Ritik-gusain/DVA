import tkinter as tk
from tkinter import ttk, messagebox

def submit():
    name   = entry_name.get()
    dob    = entry_dob.get()
    gender = gender_var.get()
    course = course_combo.get()
    email  = entry_email.get()
    phone  = entry_phone.get()

    if not all([name, dob, gender, course, email, phone]):
        messagebox.showwarning('Error', 'Please fill all fields!')
        return

    messagebox.showinfo('Success',
        f'Admission Form Submitted!\n\n'
        f'Name   : {name}\n'
        f'DOB    : {dob}\n'
        f'Gender : {gender}\n'
        f'Course : {course}\n'
        f'Email  : {email}\n'
        f'Phone  : {phone}'
    )

# Main Window
root = tk.Tk()
root.title('College Admission Form - GGSIPU')
root.geometry('480x420')
root.resizable(False, False)

# Title
tk.Label(root, text='COLLEGE ADMISSION FORM', font=('Arial',14,'bold'),
         bg='navy', fg='white').pack(fill='x', pady=5)

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(fill='both')

fields = ['Full Name', 'Date of Birth (DD/MM/YYYY)', 'Email', 'Phone No.']
entries = {}
for i, field in enumerate(fields):
    tk.Label(frame, text=field+':', anchor='w').grid(row=i, column=0, sticky='w', pady=5)
    e = tk.Entry(frame, width=30)
    e.grid(row=i, column=1, pady=5, padx=10)
    entries[field] = e

entry_name  = entries['Full Name']
entry_dob   = entries['Date of Birth (DD/MM/YYYY)']
entry_email = entries['Email']
entry_phone = entries['Phone No.']

# Gender
tk.Label(frame, text='Gender:', anchor='w').grid(row=4, column=0, sticky='w', pady=5)
gender_var = tk.StringVar(value='Male')
gf = tk.Frame(frame)
gf.grid(row=4, column=1, sticky='w', padx=10)
for g in ['Male', 'Female', 'Other']:
    tk.Radiobutton(gf, text=g, variable=gender_var, value=g).pack(side='left')

# Course
tk.Label(frame, text='Course:', anchor='w').grid(row=5, column=0, sticky='w', pady=5)
course_combo = ttk.Combobox(frame, width=27,
    values=['BCA', 'BBA', 'B.Tech', 'B.Sc', 'B.Com'])
course_combo.grid(row=5, column=1, pady=5, padx=10)
course_combo.set('Select Course')

# Buttons
bf = tk.Frame(root)
bf.pack(pady=10)
tk.Button(bf, text='Submit', command=submit, bg='green', fg='white',
          width=12).pack(side='left', padx=10)
tk.Button(bf, text='Reset', command=lambda: [e.delete(0,'end')
          for e in entries.values()], width=12).pack(side='left')

root.mainloop()
