from yaml import safe_load

_config = safe_load(open("config.yml"))

# Items to be imported by other files in the app.
# If we update key names in config.yml, we should only need to modify this file
# no matter how many times a variable may be referenced in the app.
db_location = _config["db_location"]
is_development = _config["is_development"]
