from django.urls import path

from cursos.views import cursos, curso

app_name = "cursos"
urlpatterns = [
    path("", cursos, name ="lista"),
    path("<str:sigla>/", curso, name="curso")
]