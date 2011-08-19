"""
gargoyle.tests
~~~~~~~~~~~~~~

:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

from django.conf import settings

if not getattr(settings, "SKIP_GARGOYLE_TESTS", False):
    from tests import *
