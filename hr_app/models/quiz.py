from __future__ import unicode_literals

from hashlib import md5

from django.db import models
from django.utils.translation import ugettext as _

from .person import Candidate


class Exam(models.Model):
    code = models.CharField(
        _('Код ордена'), max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.code and not self.pk:
            super(Exam, self).save(*args, **kwargs)
            self.code = md5(str(self.pk).encode('utf-8')).hexdigest()[:10]
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code', )
        verbose_name = _('Тестовое испытание')
        verbose_name_plural = _('Тестовые испытания')


class Question(models.Model):
    exam = models.ForeignKey(Exam)
    text = models.CharField(_('Текст вопроса'), max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text', )
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate, verbose_name=_('Кандидат'))
    question = models.ForeignKey(Question, verbose_name=_('Вопрос'))
    answer = models.CharField(_('Ответ'), max_length=100)

    def __str__(self):
        return self.question.text

    class Meta:
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')
