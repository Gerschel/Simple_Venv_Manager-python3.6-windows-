import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import create_project

create_project.initialize_settings()
SETTINGS = create_project.load_settings()

#TODO: Consider binding instead of trace, I don't like the use of dummy variables, it isn't explicit
def update_button(*_dummyargs):
    """Updates textvariable on the Create button"""
    create_button_var.set("Create: " + SETTINGS["folder_name"] + "\\" +venv_name_entry_var.get() + venv_folder_suffix_var.get())

def update_sttng_var(*_dummyargs):
    setns_folder_loc_var.set(setns_folder_loc_e.get())
    setns_folder_name_var.set(setns_folder_nam_e.get())
    setns_venv_fldr_var.set(setns_venv_fldr_e.get())

def update_user_settings():
    import create_user_settings
    create_user_settings.create_settings(
       setns_folder_loc_var.get(),
       setns_folder_name_var.get(),
       setns_venv_fldr_var.get(),
       )
    folder_loc_var.set(setns_folder_loc_var.get())
    folder_name_var.set(setns_folder_name_var.get())
    venv_folder_suffix_var.set(setns_venv_fldr_var.get())
    create_button_var.set("Create: " + folder_loc_var.get() + "\\" + folder_name_var.get() + "\\" + venv_name_entry_var.get() + venv_folder_suffix_var.get())
   
def set_directory():
    dir_name = filedialog.askdirectory()
    if dir_name:
        setns_folder_loc_e.delete(0, 'end')
        setns_folder_loc_e.insert(0, dir_name)

# *! TODO: Frame instantiation needed to occur before buttons that set the command for tkraise()
# *! TODO: Rearrange: Group Frame elements together, then sub-group textvars, labels, entries, buttons
# *!       Consider creating a Frame class to do this

app = tk.Tk()
app.title("Simple Venv Manager")
app.minsize(600, 300)
app.resizable(width=True, height=False)

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
# *! FIXME: Consider using binding instead of trace
venv_name_entry_var.trace('w', update_button)

#row grids
folder_loc_lab.grid(row=2, column=0)
folder_name_lab.grid(row=2, column=1)
venv_name_entry.grid(row=2, column=2)
venv_folder_suffix_lab.grid(row=2, column=3)


#Large Create button row
create_button_var = tk.StringVar()
create_button_var.set("Create: " + folder_loc_var.get() + "\\" + folder_name_var.get() + "\\" +venv_name_entry_var.get() + venv_folder_suffix_var.get())
create_button = ttk.Button(main_frame, textvariable=create_button_var, width=90, command= lambda: create_project.create_venv(create_project.load_settings(), venv_name_entry_var.get()))
create_button.grid(row=3, column=0, columnspan=4, sticky=(tk.E, tk.W))

#Settings frame widgets

setns_folder_loc_lab = ttk.Label(settings_frame, text="Folder Location:")
setns_folder_name_lab = ttk.Label(settings_frame, text="Folder Name:")
setns_venv_suff_lab = ttk.Label(settings_frame, text="Venv Name Suffix:")

setns_folder_loc_var = tk.StringVar()
setns_folder_name_var = tk.StringVar()
setns_venv_fldr_var = tk.StringVar()

# *! TODO: Handle split here as well, same split is occuring
setns_folder_loc_var.set(SETTINGS["folder_location"])
setns_folder_name_var.set(SETTINGS["folder_name"].split('\\')[-1])
setns_venv_fldr_var.set(SETTINGS["venv_folder_suffix"])

setns_folder_loc_e = tk.Entry(settings_frame, textvariable=setns_folder_loc_var)
setns_folder_nam_e = tk.Entry(settings_frame, textvariable=setns_folder_name_var)
setns_venv_fldr_e = tk.Entry(settings_frame, textvariable=setns_venv_fldr_var)

# *! FIXME: Consider using binding instead of trace
setns_folder_loc_var.trace('w', update_sttng_var)
#Testing filedialog on setting var
file_button = ttk.Button(settings_frame, text="Browse", command=set_directory)
file_button.grid(row=0, column=2)
# *! FIXME: Consider using binding instead of trace
setns_folder_name_var.trace('w', update_sttng_var)
# *! FIXME: Consider using binding instead of trace
setns_venv_fldr_var.trace('w', update_sttng_var)
# *! TODO: FIXME: lamdba not triggering functions
save_settings_b = ttk.Button(settings_frame, text="Save", command=lambda: (main_frame.tkraise(), update_user_settings()))
back_b = ttk.Button(settings_frame, text="Back", command=main_frame.tkraise)

setns_folder_loc_lab.grid(row=0, column=0) 
setns_folder_name_lab.grid(row=1, column=0)
setns_venv_suff_lab.grid(row=2, column=0)

setns_folder_loc_e.grid(row=0, column=1)
setns_folder_nam_e.grid(row=1, column=1)
setns_venv_fldr_e.grid(row=2, column=1)

save_settings_b.grid(row=3, column=1)
back_b.grid(row=3, column=0)


app.mainloop()