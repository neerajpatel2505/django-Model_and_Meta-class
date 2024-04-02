# Generated by Django 5.0.3 on 2024-04-02 08:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name'], 'verbose_name': 'stu'},
        ),
        migrations.AddField(
            model_name='student',
            name='New_Slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='Name', unique=True),
        ),
    ]
