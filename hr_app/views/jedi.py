from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from ..forms import JediForm

from ..models.person import Candidate
from ..models.person import Jedi


def select_jedi(request):
    form = JediForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        jedi = form.cleaned_data.get('jedi')
        if jedi:
            request.session['current_jedi_pk'] = jedi.pk
            return redirect('hr:jedi:pre-padawans', jedi_pk=jedi.pk)
    return render(
        request, 'hr_app/jedi/select.html', {'form': form})


def pre_padawans(request, jedi_pk):
    jedi = get_object_or_404(Jedi, pk=jedi_pk)
    objects = Candidate.objects.filter(
        planet=jedi.planet, is_padawan=False)
    return render(
        request, 'hr_app/jedi/pre_padawan.html', {'objects': objects})


def take_candidate(request, jedi_pk, candidate_pk):
    candidate = get_object_or_404(Candidate, pk=candidate_pk)
    jedi = get_object_or_404(Jedi, pk=jedi_pk)
    msg = 'Вы взяли нового падавана %s' % candidate.name
    if jedi.padawan_set.count() < 3:
        jedi.add_padawan(candidate)
    else:
        msg = 'Вы не можете взять более 3-х падаванов для обучения.'
    return render(
        request, 'hr_app/message.html', {'msg': msg})


def all_jedi_listing(request):
    objects = Jedi.objects.annotate(
        Count('padawan')).values_list(
        'name', 'padawan__count').order_by('-padawan__count', 'name')
    return render(
        request, 'hr_app/jedi/listing.html', {'objects': objects})


def active_jedi_listing(request):
    objects = Jedi.objects.annotate(
        Count('padawan')).filter(
        padawan__count__gt=0).values_list(
        'name', 'padawan__count').order_by('-padawan__count', 'name')
    return render(
        request, 'hr_app/jedi/listing.html', {'objects': objects})
