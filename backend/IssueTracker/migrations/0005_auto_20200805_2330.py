# Generated by Django 3.0.5 on 2020-08-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IssueTracker', '0004_auto_20200805_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
