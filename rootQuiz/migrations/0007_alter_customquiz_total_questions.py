# Generated by Django 4.1.7 on 2023-03-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootQuiz', '0006_rename_course_question_quiz_id_to_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customquiz',
            name='total_Questions',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
