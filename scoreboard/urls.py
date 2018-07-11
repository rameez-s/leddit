from django.conf.urls import url
from . import views

urlpatterns = [
    # /score/
    url(r'^$', views.index, name = "index"),
    # /score/{user_id}/upvote
    url(r'^(?P<id>\S+)/upvote/$', views.upvote, name='upvote'),
    # /score/{user_id}/downvote
    url(r'^(?P<id>\S+)/downvote/$', views.downvote, name='downvote'),
    # /score/getAuth
    url(r'^getAuth/$', views.getAuth, name = "getAuth"),
    # /score/main
    url(r'^main/$', views.main, name = "main")

]
