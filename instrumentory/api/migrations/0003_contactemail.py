# Generated by Django 4.0.2 on 2022-05-11 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customuser_is_validated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
