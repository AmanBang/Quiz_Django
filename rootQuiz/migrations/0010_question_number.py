# Generated by Django 4.1.7 on 2023-03-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootQuiz', '0009_remove_question_option4_alter_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]