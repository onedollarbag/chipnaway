from django.urls import path

from .views import about_view, donation_view, events_view, home_view, volunteer_view

app_name = "donations"

urlpatterns = [
    path("", home_view, name="home"),
    path("donate/", donation_view, name="donate"),
    path("volunteer/", volunteer_view, name="volunteer"),
    path("events/", events_view, name="events"),
    path("about/", about_view, name="about"),
]

