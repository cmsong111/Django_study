from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    #TodoList 제목
    TodoList_text = models.CharField(max_length=200)
    #TodoList 내용
    TodoList_content = models.TextField()
    #TodoList 언제 해야 하는건지
    TodoList_when = models.DateTimeField('target time')
    #TodoList 했는지 안했는지 체크
    TodoList_bool = models.BooleanField(default=False)
    #todoList 위치
    TodoList_where = models.TextField(blank=True)

    #사용자 확인
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    #todoList 제목으로 출력
    def __str__(self):
        return self.TodoList_text