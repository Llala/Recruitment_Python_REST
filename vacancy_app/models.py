from django.db import models

# Модель проекта - здесь задаются поля и их типы

class Vacancy(models.Model):
    #primary_key создается автоматически, если не указан явно
    name = models.CharField(max_length=200)
    salary_level = models.IntegerField()
    experience = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name
