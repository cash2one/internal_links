internal_links
=======
SEO tool for adding links to text contained in Django apps databases.

**Renamed package: https://pypi.python.org/pypi/permalink_adder**

# Installation
Install with pip:

    pip install internal_links

# Usage
You need to specify where and what to look for in your Django app's settings in this manner:

    INTERNAL_LINKS_SETTINGS = [{'app': 'your_app_name',
                                'model_name': 'your_model_name',
                                'fields': ['list', 'of', 'fields', 'in', 'which', 'script', 'should', 'search'],
                                'words': ['list', 'of', 'words', 'to', 'search'],
                                'url': 'url_that_should_be_wrapped_around_found_text'}]

Starting script with option `--start` will actually apply changes to database, instead of printing them out.

You can run the script either using `add_links` management command or call `link_adder` function from `adder.py` module. 

# Output
No output if there are no occurrences of words or when they're already wrapped.

Without `--start` option, script will only print out proposed changes.
