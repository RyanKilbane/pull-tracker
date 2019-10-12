import os
import yaml
from backend.setup import InitialSetup

home = os.path.expanduser("~")

setup = InitialSetup(home)

if not os.path.isfile(os.path.join(home, "setup.yml")):
    setup.make_dict().write_yaml(home)
    
with open(os.path.join(home, "setup.yml"), "r") as file:
    setup_data = yaml.load(file.read())
