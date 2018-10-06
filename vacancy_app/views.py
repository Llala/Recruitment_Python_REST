from rest_framework import viewsets
from .models import Vacancy
from . import serializers
from rest_framework import permissions
from django.shortcuts import render

# views - здесь описывается визуальное представление проекта,
# так же здесь задется permission класс, позволяющий
# разграничить права доступа admin и viewer

def index(request):
    return render(request,'vacancy_app/index.html')

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer
    permission_classes = (permissions.DjangoModelPermissions,)
