from django.urls import path
from . import views

urlpatterns = [
    path('runcommand/', views.BashView.as_view()),
]
