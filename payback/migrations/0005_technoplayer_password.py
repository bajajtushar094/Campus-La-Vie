# Generated by Django 3.0.1 on 2020-10-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payback', '0004_remove_technoplayer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='technoplayer',
            name='password',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
