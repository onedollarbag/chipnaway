from django.shortcuts import render
from django.utils import timezone

from .forms import DonationForm, VolunteerForm
from .models import Event


def home_view(request):
    return render(request, "donations/home.html")


def donation_view(request):
    success = False
    donated_amount = None

    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            success = True
            donated_amount = form.cleaned_data.get("amount")
            form = DonationForm()
    else:
        form = DonationForm()

    context = {
        "form": form,
        "success": success,
        "donated_amount": donated_amount,
    }
    return render(request, "donations/donation_page.html", context)


def volunteer_view(request):
    success = False

    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            success = True
            form = VolunteerForm()
    else:
        form = VolunteerForm()

    context = {
        "form": form,
        "success": success,
    }
    return render(request, "donations/volunteer.html", context)


def events_view(request):
    today = timezone.localdate()
    events = Event.objects.filter(date__gte=today).order_by("date", "time")
    return render(request, "donations/events.html", {"events": events})


def about_view(request):
    return render(request, "donations/about.html")

