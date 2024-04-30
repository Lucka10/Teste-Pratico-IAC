from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.index, name="index"),
    path("fotos/",views.foto,name='foto'),
    path("fotos/<str:foto>/",views.foto,name='foto')
]