from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #cada path associa um padrão de URL para uma view específica
    path('', include('projFuncionarios.url')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('projFuncionarios.url')),
    path('', RedirectView.as_view(url='/funcionarios/')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
