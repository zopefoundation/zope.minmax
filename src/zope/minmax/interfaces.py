from persistent.interfaces import IPersistent
from zope.interface import Attribute


class IAbstractValue(IPersistent):
    """A persistent value with the conflict resolution.

    The values are expected to be homogeneous.
    """

    value = Attribute('The initial value')

    def __bool__():
        """Return Boolean cast of the value as True or False."""
