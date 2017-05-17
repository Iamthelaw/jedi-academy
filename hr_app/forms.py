from __future__ import unicode_literals

from django import forms

from .models.person import Candidate
from .models.person import Jedi
from .models.quiz import Answer


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('slug', )


class JediForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.objects.all())


class QuizForm(forms.Form):
    def __init__(self, data, questions, *args, **kwargs):
        self.questions = questions
        super(QuizForm, self).__init__(data, *args, **kwargs)
        for question in questions:
            field_name = 'question_%s' % question.pk
            self.fields[field_name] = forms.CharField(
                label=question.text, required=True)

    def save(self, candidate_pk):
        data = self.cleaned_data
        for key, value in data.items():
            answer, _ = Answer.objects.get_or_create(
                candidate_id=int(candidate_pk),
                question_id=int(key.replace('question_', '')))
            answer.answer = value
            answer.save()
