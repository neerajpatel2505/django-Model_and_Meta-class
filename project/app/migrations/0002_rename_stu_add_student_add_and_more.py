# Generated by Django 5.0.3 on 2024-04-01 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Stu_add',
            new_name='Add',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Stu_contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Stu_Email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Stu_Name',
            new_name='Name',
        ),
    ]
