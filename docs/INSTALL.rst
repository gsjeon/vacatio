Vacatio Installation guide
==========================

Vacatio is based on debian buster!

Clone source node.::

   $ git clone <REPO URL> 

Packages installation.::

   $ sudo apt install python3
   $ sudo apt install python3-pip

Setup virtualvenv.::

   $ python3 -m venv venv 
   $ . venv/bin/activate

DB migrate.::

   (venv) $ cd vacatio
   (venv) $ export FLASK_ENV=development
   (venv) $ export FLASK_APP=vacatio
   (venv) $ flask db init
   (venv) $ flask db migrate
   (venv) $ flask db upgrade  

Check DB Tables.::

   (venv) $ sudo apt install sqlite3
   (venv) $ sqlite3 vacatio/vacatio.db
   sqlite> .tables
   sqlite> .exit

Run Flask App.::

   (venv) $ sh run.sh
