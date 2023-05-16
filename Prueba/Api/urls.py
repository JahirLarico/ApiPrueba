from django.urls import path
from . import views

app_name = 'Api'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('colegios/',views.ColegiosList.as_view(),name='colegios'),
    path('colegio/',views.ColegioDetail.as_view(),name='colegio'),
    path('estudiantes/',views.EstudiantesList.as_view(),name='estudiantes'),
    path('estudiantes/<int:Idcolegio>',views.EstudiantesByColegio.as_view(),name='estudiantePorColegio')
]