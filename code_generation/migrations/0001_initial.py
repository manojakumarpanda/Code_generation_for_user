# Generated by Django 2.1.7 on 2020-04-11 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('mobile_num', models.BigIntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('employee', 'Emp'), ('super', 'Super_user')], default='employee', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='User_codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codes', models.CharField(max_length=17, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
                ('is_used', models.BooleanField(default=False, verbose_name='active status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_code', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'codes',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='pid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='code_generation.User_codes'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
