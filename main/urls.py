from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("principal/", views.principal, name="principal"),
    path("padres/", views.padres, name="padres"),
    path("<str:casa_nombre>", views.mostrar_casa, name="casa_id"),
    path("<str:casa_nombre>/mod", views.casa_modificacion, name="casa_mod"),
    path("crear/", views.crear_casa, name="crear_casa"),
    path("disponibles/", views.disponibles_casa, name="disponibles_casa"),
    path("propiedades/", views.propiedades_casa, name="propiedades_casa"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
