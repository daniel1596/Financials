from argparse import ArgumentParser
from flask import Flask

from py.blueprints.Api import api
from py.blueprints.Pages import pages
from py.database.FinancialDatabaseHelper import FinancialDatabaseHelper

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(pages)


def run_web_app():
    app.run(debug=True)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--init_db", action="store_true")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.init_db:
        FinancialDatabaseHelper().initialize_database_first_run()
        return

    run_web_app()


if __name__ == '__main__':
    main()
