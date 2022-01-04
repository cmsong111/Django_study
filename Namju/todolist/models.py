from django.db import models
from django.db.models.base import Model

# Create your models here.
class TodoList(models.Model):
    #TodoList 제목
    TodoList_text = models.CharField(max_length=200)
    #TodoList 내용
    TodoList_content = models.TextField()
    #TodoList 언제 해야 하는건지
    Whenyoushould = models.DateTimeField('target time')
    #TodoList 했는지 안했는지 체크
    TodoList_checkbox = models.BooleanField(default=False)

    #todoList 제목으로 출력
    def __str__(self):
        return self.TodoList_text