# Generated by Django 3.2.25 on 2024-10-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20241021_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionAsked',
            new_name='Question',
        ),
    ]