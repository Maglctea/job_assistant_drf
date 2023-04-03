from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email', max_length=50)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.name