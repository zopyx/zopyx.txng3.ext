# -*- coding: utf-8 -*-

################################################################
# zopyx.txng3.ext
# (C) 2005-2016, Andreas Jung, ZOPYX, www.zopyx.com
################################################################



def stopwordfilter(words, stopwords):
    return [w for w in words if w not in stopwords]
