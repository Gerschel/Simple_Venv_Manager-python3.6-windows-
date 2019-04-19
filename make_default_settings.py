import json
from os.path import expanduser

folder_location = expanduser("~")

default_settings = {"folder_location" : folder_location,
                    "folder_name" : folder_location + "\\python_venvs",
                    "venv_folder_suffix" : "_venv",
                    "launcher_location": folder_location + "\\Desktop",
                    }

with open("default_settings.json", "w") as ds:
    json.dump(default_settings, ds)
