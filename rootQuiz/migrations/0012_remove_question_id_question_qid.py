# Generated by Django 4.1.7 on 2023-03-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootQuiz', '0011_update_question_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='question',
            name='qID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
