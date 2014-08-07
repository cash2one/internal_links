# encoding: utf-8
from helpers import add_permalinks


def permalink_adder():
        app = raw_input('Type in app name: ')
        model_name = raw_input('Type in model name: ')
        amount_of_fields = int(raw_input('Type in amount of fields: '))
        fields = []
        for i in xrange(amount_of_fields):
            fields.append(raw_input('Type in field name: '))

        word = raw_input('Type in word to search for: ')
        url = raw_input('Type in url to wrap the word with: ')
        dry_run = False if raw_input('Dry run (no change in database)? (yes/no): ').lower() == 'no' else True
        add_permalinks(app, model_name, fields, word, url, dry_run)
