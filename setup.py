#!/usr/bin/env python

###########################################################################
# TextIndexNG V 3
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################


import sys
from setuptools import setup, Extension

unicode_arg = "-DUNICODE_WIDTH=4" if sys.maxunicode > 0xffff else "-DUNICODE_WIDTH=2"
ext_args = ["-Wall"] if sys.platform != "win32" else []

with open('README.txt') as f:
    description_txt = f.read()
description_txt += '\n\nChanges\n-------\n\n'
with open('CHANGES.txt') as f:
    description_txt += f.read()

version = '4.0.0'

setup(name="zopyx.txng3.ext",
      version=version,
      maintainer= "Andreas Jung, ZOPYX Ltd. & Co. KG",
      maintainer_email = "info@zopyx.com",
      author = "Andreas Jung, ZOPYX Ltd. & Co. KG",
      author_email = "info@zopyx.com",
      zip_safe=False,
      description = 'Helper modules for TextIndexNG3 (Snowball stemmer, normalizer, splitter, etc.)',
      long_description = description_txt,
      classifiers = [
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Operating System :: OS Independent',
      ],
      url = "http://sf.net/projects/textindexng/",
      py_modules=['zopyx.__init__', 'zopyx.txng3.__init__', 'zopyx.txng3.ext.__init__'],
      install_requires=('setuptools',),
      test_suite='nose.collector',
      tests_require=('nose',),
      namespace_packages=('zopyx', 'zopyx.txng3', 'zopyx.txng3.ext'),
      extras_require=dict(test=()),
          ext_modules=[

            Extension("zopyx.txng3.ext.normalizer",
                [ "zopyx/txng3/ext/normalizer_src/normalizer.c" ],
            ),

            Extension("zopyx.txng3.ext.splitter",
                [ "zopyx/txng3/ext/splitter_src/splitter.c",
                  "zopyx/txng3/ext/splitter_src/hashtable.c",
                  "zopyx/txng3/ext/splitter_src/dict.c"
                ],
            ),

            Extension("zopyx.txng3.ext.support",
                [ "zopyx/txng3/ext/support.c" ],
            ),

            Extension('zopyx.txng3.ext.levenshtein',
                      sources = ['zopyx/txng3/ext/python-Levenshtein-0.10/Levenshtein.c'],
                      extra_compile_args=ext_args),

            Extension("zopyx.txng3.ext.stemmer",
                ["zopyx/txng3/ext/stemmer_src/stemmer.c" ,
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/libstemmer/libstemmer.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/runtime/api.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/runtime/utilities.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_danish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_dutch.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_english.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_finnish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_french.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_german.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_hungarian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_italian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_norwegian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_porter.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_portuguese.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_2_romanian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_spanish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_ISO_8859_1_swedish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_KOI8_R_russian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_danish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_dutch.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_english.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_finnish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_french.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_german.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_hungarian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_kraaij_pohlmann.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_italian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_norwegian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_porter.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_portuguese.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_romanian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_russian.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_spanish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_swedish.c",
                 "zopyx/txng3/ext/stemmer_src/libstemmer_c/src_c/stem_UTF_8_turkish.c",
                ],
                include_dirs=['zopyx/txng3/ext/stemmer_src/libstemmer_c/include',
                              'zopyx/txng3/ext/stemmer_src/libstemmer_c',
                              'zopyx/txng3/ext/stemmer_src/libstemmer_c/libstemmer'],
            ),
        ]
    )
