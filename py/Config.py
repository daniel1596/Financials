from yaml import safe_load

from py.DictionaryToObjectConverter import DictionaryToObjectConverter

__config_dictionary = safe_load(open("config.yml"))
config = DictionaryToObjectConverter(__config_dictionary)

