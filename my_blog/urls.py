from django.urls import path
from .views import Home, Blogs, Blogg

urlpatterns=[
    path('', Home, name='home'),
    path('/blogs', Blogs, name='blogs'),
    path('/blogs/<int:id>/', Blogg, name='blog')
]