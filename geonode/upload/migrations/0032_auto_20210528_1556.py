# Generated by Django 3.2 on 2021-05-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_resourcebase_files'),
        ('upload', '0031_auto_20210527_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='layer',
        ),
        migrations.AddField(
            model_name='upload',
            name='resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.resourcebase'),
        ),
    ]