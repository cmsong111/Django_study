from django.contrib import admin
from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    filedsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Infromation', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]