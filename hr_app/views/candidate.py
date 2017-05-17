from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from ..forms import CandidateForm
from ..models.person import Candidate


def new_candidate(request):
    form = CandidateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            candidate = form.save()
            return redirect(
                'hr:candidate:quiz', candidate_pk=candidate.pk)
    return render(
        request, 'hr_app/candidate/new.html', {'form': form})


def candidate_detail(request, candidate_pk):
    candidate = get_object_or_404(Candidate, pk=candidate_pk)
    jedi_pk = request.session.get('current_jedi_pk')
    return render(
        request, 'hr_app/candidate/detail.html',
        {'object': candidate, 'jedi_pk': jedi_pk})
