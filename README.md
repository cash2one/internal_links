permalink_adder
=======
SEO tool for adding permalinks to text contained in Django apps databases.

# Installation
Install with pip:

    pip install permalink_adder

# Usage
You need to specify where and what to look for in your Django app's settings in this manner:

    PERMALINK_ADDER_SETTINGS = [{'app': 'your_app_name',
                                'model_name': 'your_model_name',
                                'fields': ['list', 'of', 'fields', 'in', 'which', 'script', 'should', 'search'],
                                'words': ['list', 'of', 'words', 'to', 'search'],
                                'url': 'url_that_should_be_wrapped_around_found_text',
                                'dry_run': True}]

Setting `dry_run` to `False` will actually apply changes to database, instead of printing them out.

You can run the script either using `add_permalinks` management command or call `permalink_adder` function from `adder.py` module. 

# Output
No output if there are no occurrences of words or when they're already wrapped.

With `dry_run` set as `True`, the script will print out proposed changes, setting it to `False` will only show context of applied changes.  