"""
    First File (__init__.py)-> A special file, tells python to treat this directory like a python package.
    Other files (asgi.py, wsgi.py) -> special configuration files that we don't need to deal with

    these are allow django to do actual communicate with server.

    urls.py -> allows us to configure different roots to different django applications.

    manage.py -> special file that access command line tool that allow us to do special things that make
    database migration, run python server, django admin panel.

    admin.py -> allows to register database models so that we can view them on in app

    # TEMPLATES -> it is a reusable HTML file that allows us to display the dynamic data
    # create template folder inside the application. Named only TEMPLATES, otherwise it won't work

"""


