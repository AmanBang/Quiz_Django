# Generated by Django 4.1.7 on 2023-03-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootQuiz', '0007_alter_customquiz_total_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customquiz',
            name='total_marks',
            field=models.PositiveIntegerField(default=1),
        ),
    ]