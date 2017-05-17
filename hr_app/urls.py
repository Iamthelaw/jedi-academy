from django.conf.urls import url
from django.conf.urls import include

from .views.base import index

from .views import candidate as candidate_views
from .views import jedi as jedi_views
from .views import quiz as quiz_views


candidate_patterns = [
    url(r'new/$', candidate_views.new_candidate, name='new'),
    url(
        r'(?P<candidate_pk>[0-9]+)/$',
        candidate_views.candidate_detail, name='detail'),
    url(
        r'(?P<candidate_pk>[0-9]+)/quiz/$',
        quiz_views.quiz, name='quiz'),
]

quiz_patterns = [
    url(r'thank-you/$', quiz_views.thank_you, name='thank_you'),
]

jedi_patterns = [
    url(r'all/$', jedi_views.all_jedi_listing, name='all'),
    url(
        r'active/$',
        jedi_views.active_jedi_listing, name='active'),
    url(
        r'(?P<jedi_pk>[0-9]+)/pre-padawans/$',
        jedi_views.pre_padawans, name='pre-padawans'),
    url(
        r'(?P<jedi_pk>[0-9]+)/candidate/(?P<candidate_pk>[0-9]+)/$',
        jedi_views.take_candidate, name='take'),
    url(r'$', jedi_views.select_jedi, name='select'),
]


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^candidate/', include(candidate_patterns, namespace='candidate')),
    url(r'^jedi/', include(jedi_patterns, namespace='jedi')),
    url(r'^quiz/', include(quiz_patterns, namespace='quiz')),
]
