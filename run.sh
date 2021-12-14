export LC_ALL=C.UTF-8
export LANG=C.UTF-8

export FLASK_ENV=development
export FLASK_APP=vacatio

#rm -rf migrations/
#rm -f vacatio/vacatio.db

#flask db init
#flask db migrate
#flask db upgrade

python3 -m flask run --host 0
