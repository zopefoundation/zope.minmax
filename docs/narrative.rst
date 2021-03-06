=====================================================
 Conflict Resolution using Maximum or Minimum Values
=====================================================

The :class:`zope.minmax.AbstractValue` class provides a super class which can
be subclassed to store arbitrary *homogeneous* values in a persistent
storage and apply different conflict resolution policies.

.. autoclass:: zope.minmax.interfaces.IAbstractValue
.. autoclass:: zope.minmax.AbstractValue
   :private-members:

The subclasses defined here are resolving the conflicts using always
either the maximum or the minimum of the conflicting values.

Maximum
=======

.. autoclass:: zope.minmax.Maximum


The :class:`zope.minmax.Maximum` class always resolves conflicts favoring the
maximum value.  Let's instantiate one object and verify that it
satisfies the interface.

.. doctest::

    >>> import zope.minmax
    >>> import zope.interface.verify
    >>> max_favored = zope.minmax.Maximum()
    >>> zope.interface.verify.verifyObject(
    ...     zope.minmax.interfaces.IAbstractValue, max_favored)
    True

We can confirm that the initial value is zero.

.. doctest::

    >>> bool(max_favored)
    False
    >>> print(max_favored.value)
    None

Now, we can store a new value in the object.

.. doctest::

    >>> max_favored.value = 11
    >>> print(max_favored.value)
    11
    >>> bool(max_favored)
    True

Or we can use the methods.

.. doctest::

    >>> max_favored.__setstate__(4532)
    >>> max_favored.__getstate__()
    4532
    >>> print(max_favored.value)
    4532
    >>> bool(max_favored)
    True

Do notice that using a direct assignment to the value attribute is a
more natural use.

Minimum
=======

.. autoclass:: zope.minmax.Minimum

The :class:`zope.minmax.Minimum` class always resolves conflicts favoring the
minimum value.  Again, we instantiate an object and verify that it
satisfies the interface.

.. doctest::

    >>> min_favored = zope.minmax.Minimum()
    >>> zope.interface.verify.verifyObject(
    ...     zope.minmax.interfaces.IAbstractValue, min_favored)
    True

We need a confirmation that the initial value is zero.

.. doctest::

    >>> bool(min_favored)
    False
    >>> print(min_favored.value)
    None

Let's populate this one too.

.. doctest::

    >>> min_favored.value = 22
    >>> print(min_favored.value)
    22
    >>> bool(min_favored)
    True

Or we can use the methods, again.

.. doctest::

    >>> min_favored.__setstate__(8796)
    >>> min_favored.__getstate__()
    8796
    >>> print(min_favored.value)
    8796
    >>> bool(min_favored)
    True

Please, notice, again, that using a direct assignment to the value
attribute is a more natural use.

Conflict Resolution
===================

Now, we need to exercise the conflict resolution interface.
First for the :class:`zope.minmax.Maximum`:

Let's try differing values larger than the old value.

.. doctest::

    >>> max_favored._p_resolveConflict(max_favored.value, 4536, 4535)
    4536
    >>> max_favored._p_resolveConflict(max_favored.value, 4573, 4574)
    4574

What happens when all the values are equal, including the old.

.. doctest::

    >>> max_favored._p_resolveConflict(max_favored.value, 4532, 4532)
    4532

Notice that when the old value is larger than both the committed and
new, it is still disregarded.

.. doctest::

    >>> max_favored._p_resolveConflict(max_favored.value, 4531, 4530)
    4531

Now, the :class:`zope.minmax.Minimum`:

Let's try differing values smaller than the old value.

.. doctest::

    >>> min_favored._p_resolveConflict(min_favored.value, 8792, 8791)
    8791
    >>> min_favored._p_resolveConflict(min_favored.value, 8785, 8786)
    8785

What happens when all the values are equal, including the old.

.. doctest::

    >>> min_favored._p_resolveConflict(min_favored.value, 8796, 8796)
    8796

Notice that when the old value is smaller than both the committed and
new, it is still disregarded.

.. doctest::

    >>> min_favored._p_resolveConflict(min_favored.value, 8798, 8799)
    8798

How about an example that is not numerical?

.. doctest::

    >>> max_word = zope.minmax.Maximum('joy')
    >>> print(max_word.value)
    joy
    >>> bool(max_word)
    True
    >>> max_word._p_resolveConflict(max_word.value, 'happiness', 'exuberance')
    'happiness'
    >>> max_word._p_resolveConflict(max_word.value, 'exuberance', 'happiness')
    'happiness'
    >>> min_word = zope.minmax.Minimum(max_word.value)
    >>> print(min_word.value)
    joy
    >>> bool(min_word)
    True
    >>> min_word._p_resolveConflict(min_word.value, 'happiness', 'exuberance')
    'exuberance'
    >>> min_word._p_resolveConflict(min_word.value, 'exuberance', 'happiness')
    'exuberance'

As indicated, we don't need to have numbers, just *homegeneous* items.
The homogeneous values are not really inherently required.  However, it
makes no sense to apply min() or max() on, say, one number and one
string.  Simply, the ordering relations do not work at all on
heterogeneous values.
