import os

#Settings
user_directory = os.path.expanduser("~")
venv_directory = user_directory + "\\python_venvs"
file_suffix = "_venv"
launcher_location = user_directory + "\\Desktop"


def main():
    """
    Creates a python virtual environment in a new folder called 'python_venvs'
    Creates a .bat file on the desktop used as a shortcut to launch the venv
    """
    #Create directory where all venvs will be created in if it doesn't exist
    if not os.path.exists(venv_directory):
        os.makedirs(venv_directory)
    
    project_name = input("Enter project name:\n")
    os.chdir(venv_directory)
    
    #Check to see if project already exists, if so, give a warning
    if not os.path.exists(venv_directory + f"\\{project_name}{file_suffix}"):
        os.system(f"python -m venv {project_name}{file_suffix}")
        os.chdir(launcher_location)
        #
        with open(f"{project_name}{file_suffix}.bat", "w") as bat_file:
            bat_file.write(f'@echo off\ncmd /k"cd {venv_directory}\\{project_name}{file_suffix} & {venv_directory}\\{project_name}{file_suffix}\\Scripts\\activate"')
        print(f"""
Success.
Project: "{project_name}{file_suffix}" created. 
""")
    else:
        print(f"""
Project Name "{project_name}{file_suffix}" already exists.

To start fresh, please delete project folder "{project_name}{file_suffix}" in:
    "{venv_directory}"
""")
    input("Press Enter to exit.")


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
        print("Press Enter to continue ..." )
        input()
