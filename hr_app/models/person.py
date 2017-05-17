from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext as _

from .thing import Planet


class Candidate(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    planet = models.ForeignKey(
        Planet, verbose_name=_('Планета обитания'))
    age = models.PositiveSmallIntegerField(_('Возраст'))
    email = models.EmailField(_('Email'))
    is_padawan = models.BooleanField(
        default=False, editable=False)

    def get_absolute_url(self):
        return reverse('hr:candidate:detail', args=[self.pk])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Кандидат')
        verbose_name_plural = _('Кандидаты')


class Jedi(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    planet = models.ForeignKey(
        Planet, verbose_name=_('Планета'),
        help_text=_('Планета на которой джедай обучает кандидатов'))

    def add_padawan(self, candidate):
        _, created = Padawan.objects.get_or_create(
            jedi=self, candidate=candidate)
        if created:
            candidate.is_padawan = True
            candidate.save()
            send_mail(
                _('Поздравляем!'),
                _('Вы зачислены в падаваны.'),
                settings.FROM_EMAIL,
                [candidate.email])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Джедай')
        verbose_name_plural = _('Джедаи')


class Padawan(models.Model):
    jedi = models.ForeignKey(Jedi, verbose_name=_(''))
    candidate = models.ForeignKey(Candidate)

    def clean(self):
        if self.jedi.padawan_set.count() >= 3:
            raise ValidationError(
                _('У джедая не может быть более 3-х падаванов'))

    def __str__(self):
        return self.candidate.name

    class Meta:
        ordering = ('jedi', )
        verbose_name = _('Падаван')
        verbose_name_plural = _('Падаваны')
