# Generated by Django 5.0.3 on 2024-04-01 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_student_options_alter_student_table_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Student'},
        ),
    ]
