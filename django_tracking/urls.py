from django.conf.urls import url

from django_tracking.views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name='tracking-dashboard'),
]
