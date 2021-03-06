# Generated by Django 2.1.7 on 2019-03-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20190324_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='num',
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='poste',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.Categorie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='open', max_length=10),
        ),
    ]
