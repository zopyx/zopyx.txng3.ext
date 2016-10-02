# -*- coding: utf-8 -*-

################################################################
# zopyx.txng3.ext
# (C) 2005-2016, Andreas Jung, ZOPYX, www.zopyx.com
################################################################


import unittest, sys
from zopyx.txng3.ext.splitter import Splitter

class SplitterTests(unittest.TestCase):

    def _test(self, SP, text, expected):
        got = SP.split(text)
        self.assertEqual(got, expected)

    def testSimple(self):
        return
        SP = Splitter()
        self._test(SP, '',  [])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, ' foo ', ['foo'])
        self._test(SP, ' foo bar', ['foo','bar'])
        self._test(SP, ' foo bar ', ['foo','bar'])
        self._test(SP, ' foo 23 25 bar ', ['foo','23','25','bar'])


    def testDisabledCaseFolding(self):

        SP = Splitter(casefolding=0)
        self._test(SP, '',  [])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, ' Foo ',  ['Foo'])
        self._test(SP, ' Foo Bar', ['Foo','Bar'])
        self._test(SP, ' foo Bar ', ['foo','Bar'])


    def testEnabledCaseFolding(self):

        return
        SP = Splitter(casefolding=1)

        self._test(SP, '',  [])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, 'foo',  ['foo'])
        self._test(SP, ' Foo ',  ['foo'])
        self._test(SP, ' Foo Bar', ['foo','bar'])
        self._test(SP, ' foo Bar ', ['foo','bar'])

    def testMaxlen(self):
        return

        SP = Splitter(maxlen=5)
        self._test(SP, 'abcdefg foo barfoo', ['abcde','foo','barfo'])
        self._test(SP, 'abcdefg'*2000, ['abcde'])

    def testSeparator1(self):

        SP = Splitter(separator=".-")
        import pdb; pdb.set_trace() 
        self._test(SP, 'foo 22.33 bar',  ['foo','22.33','bar'])
        self._test(SP, 'foo 22-33 bar',  ['foo','22-33','bar'])
        self._test(SP, 'foo 22_33 bar',  ['foo','22','33','bar'])

    def testSeparator2(self):
        return
        SP = Splitter(separator=".")
        self._test(SP, 'end 12.12 line', ['end','12.12','line'])
        self._test(SP, 'end of. line.foo end.', ['end','of','line.foo','end'])
        self._test(SP, 'end of. line', ['end','of','line'])

    def testSingleChars(self):
        return

        SP = Splitter(singlechar=1)
        self._test(SP, 'ab a b c',  ['ab','a','b','c'])
        self._test(SP, 'foo 2 2 bar ', ['foo','2','2','bar'])

    def testGerman(self):
        return

        SP = Splitter(singlechar=1)
        self._test(SP, 'der b�cker Ging �ber die Br�cke',
                       ['der','b�cker','ging','�ber','die','br�cke'])

        self._test(SP, 'der ��cker Ging �ber die Br�cke',
                       ['der','��cker','ging','�ber','die','br�cke'])

    def testSwedish(self):
        return

        SP = Splitter(singlechar=1)
        self._test(SP, '�ke  vill ju inte alls leka med mig.',
                       ['�ke','vill','ju','inte','alls','leka','med','mig'])

    def testParagraphs(self):
        return
        SP = Splitter(singlechar=1, separator='�')

        self._test(SP, 'dies ist �8 b b�b',
                       ['dies', 'ist', '�8', 'b', 'b�b'])

def test_suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(SplitterTests))
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
