from django.conf.urls import url
from meetingsystem.views import UserView

urlpatterns = [
    url(r'^user/$', UserView.as_view()),
]
