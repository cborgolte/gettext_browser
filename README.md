gettext_browser
===============

Use the browser to edit gettext (*.po) files.
Makes use of html5 features `contenteditable` and `oninput`.

Runs as a [Django](http://www.djangoproject.com/) project.

Change the variable `gettext_browser.views.POFILE` to point to your desired gettext file.
Changes will overwrite this po-file so remember to backup your data.

Call `make runserver` and open (http://localhost:8000/poentry/)[http://localhost:8000/poentry/] in your browser.

The project is thought as a proof of concept.

Tested with:

   	* fedora-16, Chrome, Firefox

