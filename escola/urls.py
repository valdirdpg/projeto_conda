from django.urls import path
from escola import views

urlpatterns = [

    path('professor/', views.ProfessorViews, name='professor'),

]