"""
Mocks for the courseware.access_response Open edX module.
"""

from __future__ import absolute_import, unicode_literals


class AccessResponse(object):
    """
    Minimal mock class for `courseware.access_response.AccessResponse` in Open edX.
    """

    has_access = False

    def __init__(self, has_access, *_args, **_kwargs):
        self.has_access = has_access

    def __nonzero__(self):
        """
        Overrides bool() to allow quick conversion to bool.
        """
        return self.has_access
