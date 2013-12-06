from django.conf.urls import patterns, url
from landing import views

urlpatterns = patterns("",
    url(r"^test/(?P<inp>\d+)/?$", views.test, name="test"),
    url(r"^test/?$", views.empty, name="empty"),
    url(r"^$", views.index, name="index")
)