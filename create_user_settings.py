import json

def create_settings(folder_location, folder_name, venv_folder_suffix, launcher_location= "\\Desktop"):
    from os.path import expanduser
    user_settings = {"folder_location" : folder_location,
                     "folder_name" : folder_location + "\\" + folder_name,
                     "venv_folder_suffix" : venv_folder_suffix,
                     "launcher_location": expanduser("~") + launcher_location,
                    }

    with open("user_settings.json", "w") as user_settings_file:
        json.dump(user_settings, user_settings_file)
