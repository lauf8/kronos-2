from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from .views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("calendarapp.urls")),
    path("routine/", include("routine.urls")),
    path('post/', include('post.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)