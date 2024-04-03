from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup),
    path('signin',views.signin),
    path('dashboard/<uname>',views.dashboard,name='dashboard'),
    path('logout',views.logout),
    path('write/<uname>',views.write),
    path('fullblog/<int:id>',views.full_blog,name='full_blog'),
    path('category',views.category),
    path('type/<cat>',views.type),
    path('like/<uname>/<int:id>',views.like,name='like'),
    path('cmnt/<int:id>',views.comment,name='comment'), #It is important to write the "name" while we are using the redirect function.
    path('add_cmnt/<int:id>',views.add_comment),
    path('bookmark/<uname>/<int:id>',views.bookmark),
    path('add_review/<uname>',views.review),
]