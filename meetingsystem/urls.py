from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view()),
    url(r'^user$', views.UserView.as_view()),
    url(r'^user/new$', views.UserNewView.as_view()),
    url(r'^user/all$', views.UserAllView.as_view()),
    url(r'^meeting$', views.MeetingView.as_view()),
]
