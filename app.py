from argparse import ArgumentParser
from flask import Flask

from py.blueprints.Api import api
from py.blueprints.Pages import pages
from py.database.FinancialDatabaseHandler import FinancialDatabaseHandler
from py.helpers.ConfigHelper import config
from py.helpers.FileHelper import FileHelper

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
        # The FileHelper part has to come first, or else the FinancialDatabaseHelper
        # object can't be initialized.
        FileHelper.create_file(config.db_path)
        FinancialDatabaseHandler().init_financial_tables()
        return

    run_web_app()


if __name__ == '__main__':
    main()
