# Generated by Django 4.2.10 on 2024-04-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.TextField(max_length=16)),
            ],
        ),
    ]