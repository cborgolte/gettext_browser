
pythonenv:
	virtualenv --system-site-packages pythonenv
	pythonenv/bin/pip install -U -r requirements.txt

runserver: pythonenv
	pythonenv/bin/python manage.py runserver
