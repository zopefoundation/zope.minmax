import unittest


class ConformsToIAbstractValue:

    def _getTargetClass(self):
        raise NotImplementedError()

    def _makeOne(self, *args, **kw):
        raise NotImplementedError()

    def test_class_conforms_to_IAbstractValue(self):
        from zope.interface.verify import verifyClass

        from zope.minmax.interfaces import IAbstractValue
        verifyClass(IAbstractValue, self._getTargetClass())

    def test_instance_conforms_to_IAbstractValue(self):
        from zope.interface.verify import verifyObject

        from zope.minmax.interfaces import IAbstractValue
        verifyObject(IAbstractValue, self._makeOne())


class AbstractValueTests(unittest.TestCase, ConformsToIAbstractValue):

    def _getTargetClass(self):
        from zope.minmax._minmax import AbstractValue
        return AbstractValue

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_ctor_defaults(self):
        av = self._makeOne()
        self.assertIsNone(av.value)

    def test_ctor_explicit(self):
        value = object()
        av = self._makeOne(value)
        self.assertIs(av.value, value)

    def test___getstate__(self):
        value = object()
        av = self._makeOne(value)
        self.assertIs(av.__getstate__(), value)

    def test___setstate__(self):
        value = object()
        av = self._makeOne()
        av.__setstate__(value)
        self.assertIs(av.value, value)

    def test___bool__w_falseish_value(self):
        av = self._makeOne()
        av.__setstate__([])
        self.assertFalse(av)

    def test___bool__w_truthy_value(self):
        av = self._makeOne()
        av.__setstate__(['abc'])
        self.assertTrue(av)

    def test__p_resolve_conflict_abstract(self):
        old, committed, new = object(), object(), object()
        av = self._makeOne()
        self.assertRaises(NotImplementedError,
                          av._p_resolveConflict, old, committed, new)


class MaximumTests(unittest.TestCase, ConformsToIAbstractValue):

    def _getTargetClass(self):
        from zope.minmax._minmax import Maximum
        return Maximum

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test__p_resolve_conflict_committed_gt_new(self):
        old, committed, new = 1, 3, 2
        av = self._makeOne()
        self.assertEqual(av._p_resolveConflict(old, committed, new), committed)

    def test__p_resolve_conflict_committed_lt_new(self):
        old, committed, new = 1, 2, 3
        av = self._makeOne()
        self.assertEqual(av._p_resolveConflict(old, committed, new), new)


class MinimumTests(unittest.TestCase, ConformsToIAbstractValue):

    def _getTargetClass(self):
        from zope.minmax._minmax import Minimum
        return Minimum

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test__p_resolve_conflict_committed_gt_new(self):
        old, committed, new = 1, 3, 2
        av = self._makeOne()
        self.assertEqual(av._p_resolveConflict(old, committed, new), new)

    def test__p_resolve_conflict_committed_lt_new(self):
        old, committed, new = 1, 2, 3
        av = self._makeOne()
        self.assertEqual(av._p_resolveConflict(old, committed, new), committed)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
