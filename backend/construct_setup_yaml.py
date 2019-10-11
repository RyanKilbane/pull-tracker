import os
import yaml
from backend.setup import InitialSetup

if not os.path.isfile("setup.yml"):
    setup = InitialSetup().make_dict().write_yaml()
    
with open("setup.yml", "r") as file:
    setup_data = yaml.load(file.read())
