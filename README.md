Overcoming Troubles with Class-Based (Generic) Views
====================

This repository contains the code used in my DjangoCon 2013 presentation. All other materials may be accessed [here](http://afrg.co/otwcbv/).

**NB**: To ease setup of this demonstration, the Django Secret Key has not been removed from the `settings.py` file. This site should therefore never be used for production purposes.

Setup
---------------------

    $ git clone https://github.com/jambonrose/djangocon2013-otwcbv.git djotwcbv
    $ cd djotwcbv
    $ ./manage.py syncdb
    $ ./manage.py runserver 7777

Navigate your preferred browser to `127.0.0.1:7777`.

Source Code Perusal
---------------------

To make navigating the code easier, the project provides several tags. Each tag corresponds to a specific moment in the [presentation](https://speakerdeck.com/jambonrose/overcoming-troubles-with-class-based-generic-views)/[article](http://andrewsforge.com/article/overcoming-troubles-with-class-based-views/).

Any of the tags may be accessed with: `git checkout tagname`. For example: `git checkout cbgv-url-only`.

In order of appearance:

- `function-views`
    - The site uses functions to process requests.
- `cbv`
    - The site uses class-based views to process requests.
- `cbgv-basic`
    - The site uses class-based generic views (in `bank/views.py`) to process requests, removing the necessity for `bank/forms.py`.
- `cbgv-url-only`
    - The site uses class-based generic views in the URL mapping (`bank/urls.py`) to process requests, removing the necessity for `bank/views.py` (`bank/forms.py` still unnecessary).
- `cbgv-customized`
    - The site achieves the goals set forth in the [presentation](https://speakerdeck.com/jambonrose/overcoming-troubles-with-class-based-generic-views)/[article](http://andrewsforge.com/article/overcoming-troubles-with-class-based-views/) by customizing class-based generic views in `bank/views.py` and overriding `ModelForm` functionality in `bank/forms.py`. This last tag is equivalent to head of `master`.
