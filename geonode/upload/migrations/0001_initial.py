# Generated by Django 3.2.13 on 2022-07-19 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base", "0081_alter_resourcebase_alternate"),
        ("upload", "0039_auto_20220506_0833")
    ]

    operations = [
        migrations.CreateModel(
            name="ResourceHandlerInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("handler_module_path", models.CharField(max_length=250)),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.resourcebase",
                    ),
                ),
            ],
        )
    ]
