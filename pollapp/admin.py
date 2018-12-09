from django.contrib import admin
from .models import Choice, Question, TakenPoll

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['question_text']}),
                ('Date information', {'fields': ['question_date']}),
                ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(TakenPoll)
