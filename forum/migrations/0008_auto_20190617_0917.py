# Generated by Django 2.2.1 on 2019-06-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_comment_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='vote',
        ),
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
