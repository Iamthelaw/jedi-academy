from django.contrib import admin

from .models.thing import Planet

from .models.person import Candidate
from .models.person import Jedi

from .models.quiz import Exam
from .models.quiz import Question
from .models.quiz import Answer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3
    max_num = 3


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Jedi)
class JediAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    readonly_fields = ('code', )


admin.site.register(Planet)
