#!/usr/bin/env python


import polib

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext


POFILE = 'example/django.po'  # change to point to another gettext file
MOFILE = 'example/django.mo'  # leave blank if you dont want to create binary data


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
