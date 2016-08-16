from django.conf.urls import url
from meetingsystem.views import UserView, LoginView, MeetingView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^user$', UserView.as_view()),
    url(r'^meeting$', MeetingView.as_view()),
]
