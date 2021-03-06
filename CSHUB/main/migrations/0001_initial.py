# Generated by Django 3.2.11 on 2022-01-16 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='null', max_length=10)),
                ('last_name', models.CharField(default='null', max_length=10)),
                ('email', models.EmailField(help_text='Enter your email: ', max_length=30)),
                ('password', models.CharField(help_text='Enter your password: ', max_length=23)),
                ('resource_history', models.CharField(max_length=100)),
                ('resources_added', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='general', max_length=100)),
                ('title', models.CharField(default='general', max_length=100)),
                ('description', models.CharField(default='general', max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
