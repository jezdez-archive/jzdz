jzdz.me
=======

This is a very tiny Django project to be used as a dumb Tinyurl replacement.

Installation of requirements
----------------------------

    $ virtualenv jzdz-env
    $ source jzdz/bin/activate
    $ (jzdz-env)easy_install pip
    [..]
    $ (jzdz-env)pip install requirements/project.txt

Running it
----------

Sync the db:

    $ (jzdz-env)python manage.py upgradedb --execute
    [..]

Add to your vhost's Apache configuration:
    
    WSGIDaemonProcess jzdz-prod python-path=/path/to/jzdz-env/lib/python2.X/site-packages
    WSGIProcessGroup jzdz-prod

    WSGIScriptAlias / /path/to/jzdz/deploy/wsgi.py
    <Directory /path/to/jzdz>
        Order deny,allow
        Allow from all
    </Directory>
