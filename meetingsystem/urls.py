from django.conf.urls import url
from meetingsystem.views import UserView, LoginView

urlpatterns = [
    url(r'^user$', UserView.as_view()),
    url(r'^login$', LoginView.as_view()),
]
