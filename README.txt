!!!PROTOTYPE!!!
Flask cannot create a MySQL database, it can only connect to an existing one.
So MySQL Server must be installed using the native password setting.
Once the server is installed with root and password edit the password in createdb.py and uncomment the commented line.
Running this file will create the comics database.
Go into the app.py and edit the URI line so that the root password matches your root password.
Then to run type gunicorn app:app