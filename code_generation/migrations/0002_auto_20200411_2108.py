# Generated by Django 2.1.7 on 2020-04-11 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_generation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_codes',
            options={'ordering': ['-codes']},
        ),
    ]
