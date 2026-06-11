from django.urls import path
from a import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.auth_page),
    path("login/", views.login_view),
    path("register/", views.register_view),
    path("dashboard/", views.dashboard),
    path("logout/", views.logout_view),
    path("admin/", admin.site.urls),
]

