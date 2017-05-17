from __future__ import unicode_literals

from django.shortcuts import redirect
from django.shortcuts import render

from ..forms import QuizForm
from ..models.quiz import Exam


def thank_you(request):
    msg = 'Ваши ответы для тестового испытания сохранены'
    return render(
        request, 'hr_app/message.html', {'msg': msg})


def quiz(request, candidate_pk):
    exam = Exam.objects.last()
    form = QuizForm(
        request.POST or None, questions=exam.question_set.all())
    if request.method == 'POST':
        if form.is_valid():
            form.save(candidate_pk)
            return redirect('hr:quiz:thank_you')
    return render(
        request, 'hr_app/candidate/quiz.html',
        {'form': form, 'candidate_pk': candidate_pk})
