# Generated by Django 4.1.7 on 2023-03-31 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="App",
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
                ("name", models.CharField(help_text="Имя приложения", max_length=50)),
                (
                    "qlik_app_id",
                    models.CharField(
                        help_text="Уникальный идентификатор приложения в Qlik Sense",
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AppObject",
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
                ("name", models.CharField(help_text="Имя объекта", max_length=50)),
                (
                    "qlik_object_id",
                    models.CharField(
                        help_text="Уникальный идентификатор объекта приложения в Qlik Sense",
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="app_objects",
                        to="directories.app",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(help_text="Имя отдела", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                (
                    "username",
                    models.CharField(help_text="Имя пользователя", max_length=50),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAppObject",
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
                (
                    "app_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qlik_user_app_objects",
                        to="directories.appobject",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qlik_user_app_objects",
                        to="directories.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="app_object",
            field=models.ManyToManyField(
                related_name="q_users",
                through="directories.UserAppObject",
                to="directories.appobject",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="q_users",
                to="directories.department",
            ),
        ),
        migrations.AddField(
            model_name="appobject",
            name="users",
            field=models.ManyToManyField(
                related_name="app_objects",
                through="directories.UserAppObject",
                to="directories.user",
            ),
        ),
    ]
