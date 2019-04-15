import json
from os.path import expanduser

user_directory = expanduser("~")

default_settings = {"user_directory" : user_directory,
                    "venv_directory" : user_directory + "\\python_venvs",
                    "file_suffix" : "_venv",
                    "launcher_location": user_directory + "\\Desktop",
                    }

with open("default_settings.json", "w") as ds:
    json.dump(default_settings, ds)

print("default_settings.json created")