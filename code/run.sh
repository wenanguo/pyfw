#/bin/sh

echo "===启动应用==="
#python manage.py runserver --host 0.0.0.0

gunicorn -b 0.0.0.0:8000 manage:app