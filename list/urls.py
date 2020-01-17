from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete, name='delete'),
    path('task_done/<list_id>',views.task_done, name='task_done'),
    path('task_notdone/<list_id>',views.task_notdone, name='task_notdone'),
    path('edit/<list_id>',views.edit, name='edit')



]