# from django.contrib import admin
#
# from .models import Question
# from .models import Choice
#
# admin.site.register(Question)
# admin.site.register(Choice)

from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Details', {'fields':['question_text']}),
        ('Date Details', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
