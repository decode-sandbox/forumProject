# Generated by Django 2.2 on 2019-04-11 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_auto_20190411_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='poste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
    ]
