from django.db import models


class App(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Имя приложения',
    )
    qlik_app_id = models.CharField(
        max_length=50,
        unique=True,
        help_text='Уникальный идентификатор приложения в Qlik Sense',
    )

    def __str__(self):
        return self.name


class AppObject(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Имя объекта',
    )
    qlik_object_id = models.CharField(
        max_length=50,
        help_text='Уникальный идентификатор объекта приложения в Qlik Sense',
        unique=True,
    )
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE,
        related_name='app_objects',
    )
    users = models.ManyToManyField(
        'User',
        through='UserAppObject',
        related_name='app_objects',
    )

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Имя отдела',
    )

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(
        max_length=50,
        help_text='Имя пользователя',
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='q_users',
    )
    app_object = models.ManyToManyField(
        AppObject,
        through='UserAppObject',
        related_name='q_users',
    )

    def __str__(self):
        return self.username


class UserAppObject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='qlik_user_app_objects',
    )
    app_object = models.ForeignKey(
        AppObject,
        on_delete=models.CASCADE,
        related_name='qlik_user_app_objects',
    )

    def __str__(self):
        return self.user.username + ' - ' + self.app_object.name
