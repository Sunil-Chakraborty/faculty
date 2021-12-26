from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('',views.faculty, name='faculty'),
    path('add-faculty/',views.add_faculty, name='add-faculty'),
    path('view-faculty/<str:pk>', views.viewFaculty, name='view-faculty'), 
    path('update-faculty/<str:pk>', views.updateFaculty, name='update-faculty'),
    path('delete-faculty/<str:pk>', views.deleteFaculty, name='delete-faculty'),             
    # path('seminers/',views.seminer, name='seminer'),
]
