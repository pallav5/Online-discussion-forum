# Generated by Django 2.2.1 on 2019-06-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_remove_comment_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]