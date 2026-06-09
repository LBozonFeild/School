from django.urls import path
from a import views
from django.contrib import admin
urlpatterns = [
    # combined login/signup page
    path("", views.auth_page, name="auth"),

    # authentication actions
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),

    # main system
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("admin/", admin.site.urls),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)