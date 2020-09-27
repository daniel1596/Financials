from pathlib import Path
from sys import modules
from yaml import safe_load

from py.helpers.DictionaryToObjectConverter import DictionaryToObjectConverter

# could also do something like Path(__file__).parent.parent to get to the root directory,
# but the __main__ but should be the same regardless of where this file moves to in the future

__root_path = Path(modules['__main__'].__file__).parent

__path_config_file = Path(__root_path / "config.yml")
__config_dictionary = safe_load(open(__path_config_file))
config = DictionaryToObjectConverter(__config_dictionary)

# Setting additional properties on the config object that are Path objects, not YAML/plain text
config.root_path = __root_path
config.db_path = config.root_path / config.db_location

