# -*- coding: utf-8 -*-

################################################################
# zopyx.txng3.ext
# (C) 2005-2016, Andreas Jung, ZOPYX, www.zopyx.com
################################################################


import sys, os, unittest, gzip
from Stemmer import Stemmer


__basedir__ = os.path.dirname(__file__)

class SimpleStemmerTests(unittest.TestCase):

    def getData(self, lang):

        content = None
        for fn in ('voc.txt', 'voc.txt.gz'):
            filename = os.path.join(__basedir__, lang, fn)
            if os.path.exists(filename):
                if filename.endswith('.gz'):
                    with gzip.open(filename) as fp:
                        content = fp.read()
                        content = str(content, 'utf-8')
                    break
                elif filename.endswith('.txt'):
                    with open(filename) as fp:
                        content = fp.read()
                    break
        if not content:
            raise IOError('No input file found for {}'.format(lang))
        voc = [line.strip() for line in content.split('\n')]

        for fn in ('output.txt', 'output.txt.gz'):
            filename = os.path.join(__basedir__, lang, fn)
            if os.path.exists(filename):
                if filename.endswith('.gz'):
                    with gzip.open(filename) as fp:
                        content = fp.read()
                        content = str(content, 'utf-8')
                    break
                elif filename.endswith('.txt'):
                    with open(filename) as fp:
                        content = fp.read()
                    break
        if not content:
            raise IOError('No input file found for {}'.format(lang))
        out = [line.strip() for line in content.split('\n')]
        assert len(voc) == len(out)
        return voc, out

    def doTest(self, language):
        """ simple stemming"""

        S = Stemmer(language)
        voc, out = self.getData(language)
        for v,r  in zip(voc,out):
            self.assertEqual(S.stemWords([v]), [r], 'term: %s\ngot: %s\nexpected: %s' % (repr(v), repr(S.stemWords([v])), repr(r)))
        self.assertEqual(S.stemWords(voc), out)

    def testGerman(self):
        self.doTest('german')

    def testFrench(self):
        self.doTest('french')

    def testDanish(self):
        self.doTest('danish')

    def testDutch(self):
        self.doTest('dutch')

    def testEnglish(self):
        self.doTest('english')

    def testDanish(self):
        self.doTest('danish')

    def testItalian(self):
        self.doTest('italian')

    def testNorwegian(self):
        self.doTest('norwegian')

    def testPortuguese(self):
        self.doTest('portuguese')

    def testSpanish(self):
        self.doTest('spanish')

    def testSwedisch(self):
        self.doTest('swedish')

    def testRussian(self):
        self.doTest('russian')

    def testPorter(self):
        self.doTest('porter')

    def testFinnish(self):
        self.doTest('finnish')

    def testTurkish(self):
        self.doTest('turkish') 

    def testHungarian(self):
        self.doTest('hungarian')

    def testRomanian(self):
        self.doTest('romanian')

def test_suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(SimpleStemmerTests))
    return s

def main():
   unittest.TextTestRunner().run(test_suite())

def debug():
   test_suite().debug()

def pdebug():
    import pdb
    pdb.run('debug()')
   
if __name__=='__main__':
   if len(sys.argv) > 1:
      globals()[sys.argv[1]]()
   else:
      main()

