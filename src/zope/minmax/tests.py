import doctest
import unittest

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('minmax.txt'),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
