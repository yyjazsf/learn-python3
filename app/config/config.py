import pathlib
import yaml

# todo python3 app.py config=pathToOtherConfig
root = pathlib.Path(__file__).parent


def get_config(dev=True):
    if dev:
        path = root / 'dev.yaml'
    else:
        path = root / 'prod.yaml'

    with open(path) as f:
        config = yaml.load(f)
    return config
