from django.db import models

from userapp.models import CustomBaseModel, CustomUser


class ProfessionalRole(CustomBaseModel):
    """" Модель позиции (должности) человека на работе/проекте."""

    name = models.CharField(unique=True, verbose_name='Название должности', max_length=50)  # Название должности

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employment(CustomBaseModel):
    """"Модель вида занятости (стажировка, частичная занятость, полная занятость и другие)."""

    name = models.CharField(unique=True, verbose_name='Вид занятости',
                            max_length=50)  # Название вида занятости

    class Meta:
        verbose_name = 'Вид занятости'
        verbose_name_plural = 'Виды занятости'


class Schedule(CustomBaseModel):
    """"Модель графика работы (полный день, удаленка, гибкий график и другие)."""
    name = models.CharField(unique=True, verbose_name='Тип графика',
                            max_length=50)  # Название вида графика работы

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'


class Skill(CustomBaseModel):
    """"Модель навыков пользователя (Docker, git, Python и другие)."""
    name = models.CharField(unique=True, verbose_name='Название навыка', max_length=25)  # Название навыка

    class Meta:
        verbose_name = 'Ключевые навыки'
        verbose_name_plural = 'Ключевые навыки'


class LanguageLevel(CustomBaseModel):
    """"Модель уровня владения языком (A2, B1, C1, родной и другие)."""
    name = models.CharField(unique=True, verbose_name='Уровень владения',
                            max_length=25)  # Название уровня владения языком

    class Meta:
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровни владения языком'


class Language(CustomBaseModel):
    """"Модель языка (Английский, Русский и другие)."""
    name = models.CharField(unique=True, verbose_name='Язык', max_length=25)  # Название языка
    level = models.ForeignKey(LanguageLevel, verbose_name='Уровень владения',
                              on_delete=models.PROTECT)  # Уровень владения языком

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Resume(CustomBaseModel):
    """"Модель резюме пользователя."""
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)  # Пользователь, подавший резюме
    # Информация о желаемой позиции
    professional_roles = models.ManyToManyField(ProfessionalRole,
                                                verbose_name='Позиция')  # Желаемая позиция (начальник, повар)
    employment = models.ManyToManyField(Employment, verbose_name='Вид занятости')  # Вид занятости (стажировка)
    schedule = models.ManyToManyField(Schedule, verbose_name='График работы')  # График работы (полный день, стажировка)
    # Навыки
    languages = models.ManyToManyField(Language, verbose_name='Язык')  # Язык
    key_skills = models.ManyToManyField(Skill, verbose_name='Клчюевые навыки')  # Навыки
    # Доп информация
    about = models.TextField(verbose_name='Обо мне')  # Доп информация о человеке

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Experience(CustomBaseModel):
    """"Модель опыта работы пользователя. Например места прошлых работ, сделанных проектов"""
    resume = models.ForeignKey(Resume, verbose_name='Резюме', related_name='experiences',
                               on_delete=models.CASCADE)  # Резюме, к которому привязан опыт
    name = models.CharField(verbose_name='Название предыдущего места работы', max_length=50)  # Название работы/проекта
    professional_roles = models.ForeignKey(ProfessionalRole, verbose_name='Должность',
                                           on_delete=models.PROTECT)  # Позиция на работе/проекте
    description = models.TextField(verbose_name='Описание',
                                   blank=True)  # Описание прошлого опыта (что делал на проекте, чем занимался)
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')  # Дата начала работы
    finished_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания',
                                       blank=True)  # Дата окончания работы (либо по текущий момент)

    class Meta:
        verbose_name = 'Предыдущее место работы'
        verbose_name_plural = 'Предыдущие места работы'
