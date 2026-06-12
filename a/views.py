from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Student, Resource


def auth_page(request):
    # just renders the combined login/signup page
    return render(request, "auth.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(
                username=username,
                password=password
            )

            request.session["student_id"] = student.id
            return redirect("dashboard")

        except Student.DoesNotExist:
            return redirect("auth")

    return redirect("auth")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # prevent duplicate usernames
        if not Student.objects.filter(username=username).exists():
            Student.objects.create(
                username=username,
                password=password
            )

        return redirect("auth")

    return redirect("auth")

def dashboard(request):

    if "student_id" not in request.session:
        return redirect("auth")

    now = timezone.now()

    available_files = Resource.objects.filter(release_time__lte=now)
    upcoming_files = Resource.objects.filter(release_time__gt=now)

    return render(request, "dashboard.html", {
        "available_files": available_files,
        "upcoming_files": upcoming_files
    })

from django.http import HttpResponse
from django.core.files.storage import default_storage

def test(request):
    print(HttpResponse(str(type(default_storage))))

def logout_view(request):
    request.session.flush()
    return redirect("auth")