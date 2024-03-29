# -*- coding: iso-8859-1 -*-
# -----------------------------------------------------------------------------
# pcm.py - pcm file parser
# -----------------------------------------------------------------------------
# $Id: pcm.py 3983 2009-05-14 18:58:44Z tack $
#
# -----------------------------------------------------------------------------
# kaa-Metadata - Media Metadata for Python
# Copyright (C) 2003-2006 Thomas Schueppel, Dirk Meyer
#
# First Edition: Thomas Schueppel <stain@acm.org>
# Maintainer:    Dirk Meyer <dischi@freevo.org>
#
# Please see the file AUTHORS for a complete list of authors.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MER-
# CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# -----------------------------------------------------------------------------

from __future__ import absolute_import

__all__ = ['Parser']

# python imports
import sndhdr

# import kaa_metadata.audio core
from . import core

class PCM(core.Music):
    def __init__(self,file):
        core.Music.__init__(self)
        t = self._what(file)
        if not t:
            raise core.ParseError()
        (self.type, self.samplerate, self.channels, self.bitrate, \
         self.samplebits) = t
        if self.bitrate == -1:
            # doesn't look right
            raise core.ParseError()
        self.mime = "audio/%s" % self.type

    def _what(self,f):
        """Recognize sound headers"""
        h = f.read(512)
        for tf in sndhdr.tests:
            try:
                res = tf(h, f)
            except IndexError:
                # input too small.
                continue
            if res:
                return res
        return None


Parser = PCM
