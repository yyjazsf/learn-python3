import pathlib
import yaml

# todo python3 app.py config=pathToOtherConfig
path = pathlib.Path(__file__).parent / 'dev.yaml'


def get_config():
    with open(path) as f:
        config = yaml.load(f)
    return config
