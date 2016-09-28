###########################################################################
# TextIndexNG V 3                
# The next generation TextIndex for Zope
#
# This software is governed by a license. See
# LICENSE.txt for the terms of this license.
###########################################################################


import sys, os, unittest, gzip
from Stemmer import Stemmer


__basedir__ = os.path.dirname(__file__)

class SimpleStemmerTests(unittest.TestCase):

    def getData(self, lang):

        with gzip.open(os.path.join(__basedir__, lang, 'voc.txt.gz')) as fp:
            content = fp.read()
        content = str(content, 'utf-8')
        voc = [line.strip() for line in content.split('\n')]

        with gzip.open(os.path.join(__basedir__, lang, 'output.txt.gz')) as fp:
            content = fp.read()
        content = str(content, 'utf-8')
        out = [line.strip() for line in content.split('\n')]

        assert len(voc) == len(out)
        return voc, out


    def doTest(self, language, encoding):
        """ simple stemming"""

        S = Stemmer(language)
        voc, out = self.getData(language)

        for v,r  in zip(voc,out):
            self.assertEqual(S.stemWords([v]), [r], 'term: %s\ngot: %s\nexpected: %s' % (repr(v), repr(S.stemWords([v])), repr(r)))

        self.assertEqual(S.stemWords(voc), out)

    def testGerman(self):
        self.doTest('german', 'utf-8')

    def testFrench(self):
        self.doTest('french', 'utf-8')

    def testDanish(self):
        self.doTest('danish', 'utf-8')

    def testDutch(self):
        self.doTest('dutch', 'utf-8')

    def testEnglish(self):
        self.doTest('english', 'utf-8')

    def testDanish(self):
        self.doTest('danish', 'utf-8')

    def testItalian(self):
        self.doTest('italian', 'utf-8')

    def testNorwegian(self):
        self.doTest('norwegian', 'utf-8')

    def testPortuguese(self):
        self.doTest('portuguese', 'utf-8')

    def testSpanish(self):
        self.doTest('spanish', 'utf-8')

    def testSwedisch(self):
        self.doTest('swedish', 'utf-8')

    def testRussian(self):
        self.doTest('russian', 'utf-8')

    def testPorter(self):
        self.doTest('porter', 'utf-8')

    def testFinnish(self):
        self.doTest('finnish', 'utf-8')
#
#    def testTurkish(self):
#        self.doTest('turkish', 'utf-8')
#
#    def testHungarian(self):
#        self.doTest('hungarian', 'utf-8')
#
##    def testRomanian(self):
#        self.doTest('romanian', 'utf-8')
#
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

