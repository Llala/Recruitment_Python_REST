from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

#Внутренние url-адреса, подключаются к внешним url-адресам проекта

router = DefaultRouter()
router.register(r'vacancies', views.VacancyViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
