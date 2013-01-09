# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Standard Mandarin model.
#

import anki.stdmodels

def addMandarinModel(col):
    mm = col.models
    m = mm.new(_("Mandarin"))
    fm = mm.newField(_("English"))
    mm.addField(m, fm)
    fm = mm.newField(_("Hanzi"))
    mm.addField(m, fm)
    fm = mm.newField(_("Pinyin"))
    mm.addField(m, fm)
    fm = mm.newField(_("Audio"))
    mm.addField(m, fm)


    t = mm.newTemplate(_("Recognition"))
 
    # recognition card
    t['qfmt'] = "{{English}}"
    t['afmt'] = "{{Pinyin}}"

    mm.addTemplate(m, t)
    mm.add(m)
    return m

anki.stdmodels.models.append((_("Mandarin"), addMandarinModel))
