# Generated by Django 3.2.8 on 2022-01-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_todolist_todolist_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='TodoList_when',
            field=models.DateTimeField(verbose_name='target time'),
        ),
    ]
