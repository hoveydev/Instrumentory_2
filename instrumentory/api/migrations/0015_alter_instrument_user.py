# Generated by Django 4.0.2 on 2022-06-09 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_schooldistrict_verify_district_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instrument', to=settings.AUTH_USER_MODEL),
        ),
    ]
