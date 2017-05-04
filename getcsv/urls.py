from django.conf.urls import url

from . import views

urlpatterns = [url(r'^sample_csv$', views.get_csv)]
