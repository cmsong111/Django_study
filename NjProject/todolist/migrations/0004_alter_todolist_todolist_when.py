# Generated by Django 3.2.8 on 2022-01-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_todolist_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='TodoList_when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='target time'),
        ),
    ]