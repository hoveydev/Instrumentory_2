# Generated by Django 4.0.2 on 2022-05-23 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_student_delete_teacher_schooldistrict_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolsite',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='api.schooldistrict'),
        ),
    ]
