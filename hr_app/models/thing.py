from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Planet(models.Model):
    name = models.CharField(_('Имя'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Планета')
        verbose_name_plural = _('Планеты')
