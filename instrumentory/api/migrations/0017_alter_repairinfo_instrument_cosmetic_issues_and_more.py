# Generated by Django 4.0.2 on 2022-07-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_repairinfo_instrument_cosmetic_issues_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairinfo',
            name='instrument_cosmetic_issues',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='repairinfo',
            name='instrument_hardware_issues',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
