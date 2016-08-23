from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view()),
    url(r'^users/(?P<employeeID>.+)$', views.UsersGetView.as_view()),
    url(r'^users$', views.UsersView.as_view()),
    url(r'^rooms$', views.RoomsView.as_view()),
    url(r'^meetings$', views.MeetingsView.as_view()),
    url(r'^meetings/overlap$', views.MeetingsOverlapView.as_view()),
    url(r'^timeblocks$', views.TimeBlocksView.as_view()),
    url(r'^invites/(?P<employeeID>.+)$', views.InvitesView.as_view()),
]
