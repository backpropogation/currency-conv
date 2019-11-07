from django.contrib import admin
from django.urls import include, path

from apps.api.routers import router
from apps.currency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('rate/update', views.update_rate)
]


