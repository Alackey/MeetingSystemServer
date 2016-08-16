from django.conf.urls import url
from meetingsystem.views import LoginView, UserView, UserAllView, MeetingView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^user$', UserView.as_view()),
    url(r'^user/all$', UserAllView.as_view()),
    url(r'^meeting$', MeetingView.as_view()),
]
