"""
gargoyle.tests.models
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""
from django.db import models
from django.contrib.auth.models import User

class InterestingInfo(models.Model):
    interesting = models.BooleanField(default=False)
    username = models.CharField(max_length=10)