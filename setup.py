#!/usr/bin/env python

###########################################################################
# TextIndexNG V 3                
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################


import sys
import os
from setuptools import setup, find_packages, Extension

unicode_arg = sys.maxunicode>0xffff and "-DUNICODE_WIDTH=4" or "-DUNICODE_WIDTH=2" 
ext_args = sys.platform != "win32" and ['-Wall'] or [] 

description_txt = open('README.txt').read()
description_txt += '\n\nChanges\n-------\n\n'
description_txt += open('CHANGES.txt').read()

version = '3.4.1'

setup(name="zopyx.txng3.ext",
      version=version,
      maintainer= "Andreas Jung, ZOPYX Ltd. & Co. KG",
      maintainer_email = "info@zopyx.com",
      author = "Andreas Jung, ZOPYX Ltd. & Co. KG",
      author_email = "info@zopyx.com",
      zip_safe=False,
      description = 'Helper modules for TextIndexNG3 (Snowball stemmer, normalizer, splitter, etc.)',
      long_description = description_txt,
      url = "http://sf.net/projects/textindexng/",
      py_modules=['zopyx.__init__', 'zopyx.txng3.__init__', 'zopyx.txng3.ext.__init__'],
      install_requires=('setuptools',
          'python-Levenshtein',
          'PyStemmer'),
      test_suite='nose.collector',
      tests_require=('nose',),
      namespace_packages=('zopyx', 'zopyx.txng3', 'zopyx.txng3.ext'),
    )

