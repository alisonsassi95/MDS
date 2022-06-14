from django.contrib import admin
from django.urls import path
from patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    path('records/', views.db_record, name='records')
]
