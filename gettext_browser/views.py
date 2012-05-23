#!/usr/bin/env python


import polib
import signal
import os

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext


# Location of .po and .mo files
POFILE = '/path/to/djangoproject/locale/it/LC_MESSAGES/django.po'  # change to point to another gettext file
MOFILE = '/path/to/djangoproject/locale/it/LC_MESSAGES/django.mo'  # leave blank if you dont want to create binary data

# if the translation files belong to a process like gunicorn, it will be restarted by 'kill -HUP' on every change
GUNICORN_PID = int(open('/path/to/gunicorn.pid').read().strip())  # leave blank if you dont want to restart the server


def show(request):
    """Show and edit translation msg."""
    pofile = polib.pofile(POFILE)
    count = len(pofile)
    idx = int(max(request.REQUEST.get('idx', 0), 0))
    idx = min(idx, count-1)
    entry = pofile[idx]
    if request.method == 'POST':
        msgstr = request.POST['msgstr-orig'].replace('\r', '')
        if msgstr != entry.msgstr:
            entry.msgstr = msgstr
            pofile.save(POFILE)
            if MOFILE:
                pofile.save_as_mofile(MOFILE)
            if GUNICORN_PID:
                os.kill(GUNICORN_PID, signal.SIGHUP)
        if idx < count - 1:
            idx += 1
        return redirect('{0}?idx={1}'.format(request.path, idx))

    nxt = '{0}'.format(idx + 1) if idx < count - 1 else ''
    prv = '{0}'.format(idx - 1) if idx > 0 else ''
    msgstr = entry.msgstr if entry.msgstr else entry.msgid
    return render_to_response('gettext_browser/entry.html', {'entry': entry,
                                                     'count': count,
                                                     'msgstr': msgstr,
                                                     'idx': idx,
                                                     'next': nxt,
                                                     'prev': prv},
                              RequestContext(request))
