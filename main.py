import tkinter as tk
from tkinter import ttk

import create_project

SETTINGS = create_project.load_settings()

def update_button(dummya,dummyb,dummyc):
    create_button_var.set("Create: " + SETTINGS["folder_name"] + "\\" +venv_name_entry_var.get() + venv_folder_suffix_var.get())


app = tk.Tk()
app.title("Simple Venv Manager")
app.geometry("600x300")
app.resizable(width=False, height=False)

#Settings Frame instantiate
settings_frame = ttk.Frame(app)
settings_frame.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))


#Main Frame
main_frame = ttk.Frame(app)
main_frame.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))
main_frame.columnconfigure(0, minsize=156)
main_frame.columnconfigure(1, minsize=136)
main_frame.columnconfigure(2, minsize=136)
main_frame.columnconfigure(3, minsize=136)

#Change Settings Row
curr_sett_l = ttk.Label(main_frame, text="Current Settings")
curr_sett_l.grid(row=0, column=0)
ch_sett_b = ttk.Button(main_frame, text="Change Settings", command=settings_frame.tkraise)
ch_sett_b.grid(row=0, column=1)

#Label of Setting Names row
f_loc_lab = ttk.Label(main_frame, text="Folder Location")
f_loc_lab.grid(row=1, column=0)

f_name_lab = ttk.Label(main_frame, text="Folder Name")
f_name_lab.grid(row=1, column=1)

venv_name_lab = ttk.Label(main_frame, text="Venv Name")
venv_name_lab.grid(row=1, column=2)

venv_suff_lab = ttk.Label(main_frame, text="Venv Suffix")
venv_suff_lab.grid(row=1, column=3)

#Current Settings display row, with an entry field
folder_loc_var = tk.StringVar()
folder_name_var = tk.StringVar()
venv_folder_suffix_var = tk.StringVar()

folder_loc_var.set(SETTINGS["folder_location"])
#
"""#TODO: Get rid of the split, which means to find areas like,
   folder_location + folder_name
   and refactor to either combine in each area and remove the combination before hand
   or to not use folder_location once folder name is established
   example: make_default_settings.py line 7; 
   Which way of doing such is still under consideration.
"""
folder_name_var.set(SETTINGS["folder_name"].split('\\')[-1])
venv_folder_suffix_var.set(SETTINGS["venv_folder_suffix"])

#row labels
folder_loc_lab = ttk.Label(main_frame, textvariable=folder_loc_var)
folder_name_lab = ttk.Label(main_frame, textvariable=folder_name_var)
venv_folder_suffix_lab = ttk.Label(main_frame, textvariable=venv_folder_suffix_var)

#row entry
venv_name_entry_var = tk.StringVar()
venv_name_entry = ttk.Entry(main_frame, textvariable= venv_name_entry_var)
venv_name_entry_var.trace('w', update_button)

#row grids
folder_loc_lab.grid(row=2, column=0)
folder_name_lab.grid(row=2, column=1)
venv_name_entry.grid(row=2, column=2)
venv_folder_suffix_lab.grid(row=2, column=3)


#Large Create button row
create_button_var = tk.StringVar()
create_button_var.set("Create: " + SETTINGS["folder_name"] + "\\" +venv_name_entry_var.get() + venv_folder_suffix_var.get())
create_button = ttk.Button(main_frame, textvariable=create_button_var, width=90)
create_button.grid(row=3, column=0, columnspan=4, sticky=(tk.E, tk.W))

#Settings frame widgets
'''sett_folder_loc_var
sett_folder_loc_lab

sett_folder_name_var
sett_folder_name_lab
'''







save_settings_b = ttk.Button(settings_frame, text="Save", command=main_frame.tkraise)
save_settings_b.grid(row=2, column=2)
back_b = ttk.Button(settings_frame, text="Back", command=main_frame.tkraise)
back_b.grid(row=2, column=0)


app.mainloop()