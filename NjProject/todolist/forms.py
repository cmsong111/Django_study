from django import forms

class todolist_new(forms.Form):
    TodoList_text = forms.CharField(error_messages = {'required':"제목을 입력해주세요"}, label = "제목", max_length=128)
    TodoList_content = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)
    TodoList_when = forms.DateTimeField
    TodoList_where = forms.CharField