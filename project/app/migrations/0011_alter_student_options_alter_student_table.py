# Generated by Django 5.0.3 on 2024-04-01 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name'], 'verbose_name': 'stu'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='stu_table',
        ),
    ]
