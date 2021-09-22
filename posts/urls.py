from django.urls import path

from .views import HomePageView, CreatePostView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', CreatePostView.as_view(), name='add_post')
]
