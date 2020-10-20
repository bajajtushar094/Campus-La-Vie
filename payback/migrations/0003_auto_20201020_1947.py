# Generated by Django 3.0.1 on 2020-10-20 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payback', '0002_technoplayer_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='technoplayer',
            name='rollno',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='technoplayer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
