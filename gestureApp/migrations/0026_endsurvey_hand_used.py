# Generated by Django 3.1.3 on 2021-05-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestureApp', '0025_auto_20210507_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='endsurvey',
            name='hand_used',
            field=models.CharField(default='left', max_length=15),
            preserve_default=False,
        ),
    ]
