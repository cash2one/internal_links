permalink_adder
=======
SEO tool for adding permalinks to text contained in Django apps databases.

# Installation
Install with pip:

    pip install permalink_adder

# Usage
You need to specify where and what to look for in you django settings app in this manner:

    PERMALINK_ADDER_SETTINGS = [{'app': 'your_app_name',
                                'model_name': 'your_model_name',
                                'fields': ['list', 'of', 'fields', 'in', 'which', 'script', 'should', 'search'],
                                'words': ['list', 'of', 'words', 'to', 'search'],
                                'url': 'url_that_should_be_wrapped_around_found_text',
                                'dry_run': True}]

Setting `dry_run` to `False` will actually apply changes to database, instead of printing them out.