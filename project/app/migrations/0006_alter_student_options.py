# Generated by Django 5.0.3 on 2024-04-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'get_latest_by': 'Name', 'ordering': ['-Name'], 'verbose_name': 'stu'},
        ),
    ]
