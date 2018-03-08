from django.urls import include, path
from django.contrib import admin
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='voting'),
    path('admin/', admin.site.urls),
]