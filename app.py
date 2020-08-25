from argparse import ArgumentParser
from flask import Flask

from py.blueprints.Api import api
from py.blueprints.Pages import pages
from py.database.DatabaseMethods import initialize_database_first_run

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(pages)

# Next objectives:
# TODO: get the app to read from the database rather than an in-memory list
# The view-model might remain similar but the Python class hierarchy is probably going to basically disappear.
# As is probably at least one Enum. But that's ok. I'll be trimming back on the fat of this application,
# and what will be left will be a working application that's well-built from the database layer up.
# Also will be scriptable, secure, etc.
# Really happy about how this is coming together so far. Feels like my previous work on similar apps
# is paying off as I can figure out on this app. Tabulator, Vue, Sqlite3, Flask, SQL, Bootstrap. Living the dream.

def run_web_app():
    app.run(debug=True)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--init_db", action="store_true")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.init_db:
        initialize_database_first_run()
        return

    run_web_app()


if __name__ == '__main__':
    main()
