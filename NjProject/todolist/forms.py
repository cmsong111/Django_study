from django import forms
from todolist.models import TodoList

class TodolistForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('TodoList_text','TodoList_content','TodoList_when','TodoList_bool','TodoList_where','user')
