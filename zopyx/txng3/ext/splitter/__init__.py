# -*- coding: utf-8 -*-

################################################################
# zopyx.txng3.ext
# (C) 2005-2016, Andreas Jung, ZOPYX, www.zopyx.com
################################################################


import re


class Splitter(object):

    def __init__(self, casefolding=True, maxlen=None, singlechar=True, separator=u' '):
        self.casefolding = casefolding
        self.maxlen = maxlen
        self.singlechar = singlechar
        self.separator = separator

    def split(self, text):
        if self.casefolding:
            text = text.lower()

        sep = '|'.join(['\\{}'.format(s) for s in self.separator])
        text = re.split(sep, text)

        if self.maxlen:
            text = [t[:self.maxlen + 1] for t in text]

        if not self.singlechar:
            text = [t for t in text if len(text) > 1]

        text = [t.strip() for t in text if t]
        return text
