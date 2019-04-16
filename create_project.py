import os
import json

def load_settings():
    """
    Load User Settings if it exists, otherwise, will load default settings
    """
    cur_d = os.getcwd()
    if os.path.exists(cur_d + "\\user_settings.json"):
        with open(cur_d + "\\user_settings.json") as settings_file:
            settings = json.load(settings_file)
    else:
        with open(cur_d + "\\default_settings.json") as settings_file:
            settings = json.load(settings_file)
    return settings


def initialize_settings():
    """
    On first run, will create the default settings file
    otherwise, will exit if it exists
    """
    cur_d = os.getcwd()
    if os.path.exists(cur_d + "\\user_settings.json"):
        return
    else:
        import make_default_settings

#Settings TODO: rework main to have the initialize settings, 
initialize_settings()
settings = load_settings()


def main():
    """
    Creates a python virtual environment in a new folder called 'python_venvs'
    Creates a .bat file on the desktop used as a shortcut to launch the venv
    """
    #Create directory where all venvs will be created in if it doesn't exist
    if not os.path.exists(settings['venv_directory']):
        os.makedirs(settings['venv_directory'])
    
    project_name = input("Enter project name:\n")
    os.chdir(settings['venv_directory'])
    
    #Check to see if project already exists, if so, give a warning
    if not os.path.exists(settings['venv_directory'] + f"\\{project_name}{settings['file_suffix']}"):
        os.system(f"python -m venv {project_name}{settings['file_suffix']}")
        os.chdir(settings['launcher_location'])
        #
        with open(f"{project_name}{settings['file_suffix']}.bat", "w") as bat_file:
            bat_file.write(f'@echo off\ncmd /k"cd {settings["venv_directory"]}\\{project_name}{settings["file_suffix"]} & {settings["venv_directory"]}\\{project_name}{settings["file_suffix"]}\\Scripts\\activate"')
        print(f"""
Success.
Project: "{project_name}{settings['file_suffix']}" created. 
""")
    else:
        print(f"""
Project Name "{project_name}{settings['file_suffix']}" already exists.

To start fresh, please delete project folder "{project_name}{settings['file_suffix']}" in:
    "{settings['venv_directory']}"
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
