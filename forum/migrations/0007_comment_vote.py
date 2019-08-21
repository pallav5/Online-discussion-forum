# Generated by Django 2.2.1 on 2019-06-16 16:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_auto_20190613_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
