import os

user_directory = os.path.expanduser("~")
venv_directory = user_directory + "\\python_venvs"
launcher_location = user_directory + "\\Desktop"

if not os.path.exists(venv_directory):
    os.makedirs(venv_directory)

def main():
    """
    Creates a python virtual environment in a new folder called 'python_venvs'
    Creates a .bat file on the desktop used as a shortcut to launch the venv
    """
    project_name = input("Enter project name:\n")
    os.chdir(venv_directory)
    os.system(f"python -m venv {project_name}")
    os.chdir(launcher_location)

    with open(f"{project_name}.bat", "w") as bat_file:
        bat_file.write(f'@echo off\ncmd /k"cd {venv_directory}\\{project_name} & {venv_directory}\\{project_name}\\Scripts\\activate"')


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
