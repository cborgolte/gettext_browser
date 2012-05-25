
pythonenv:
	virtualenv --system-site-packages pythonenv
	pythonenv/bin/pip install -U -r requirements.txt

runserver: pythonenv
	pythonenv/bin/python main.py

runserver9000: pythonenv
	pythonenv/bin/python manage.py runserver 0.0.0.0:9000
