import json

def create_settings(folder_location, folder_name, folder_suffix, launcher_location):

    user_settings = {"folder_location" : folder_location,
                     "folder_name" : folder_location + "\\python_venvs",
                     "folder_suffix" : "_venv",
                     "launcher_location": folder_location + "\\Desktop",
                    }

    with open("user_settings.json", "w") as user_settings_file:
        json.dump(user_settings, user_settings_file)

    print("user_settings.json created")