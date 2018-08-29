from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = 'name_index'),
    path('login',views.login,name = 'name_login'),
    path('register',views.register, name = 'name_register'),
    path('logout',views.logout, name = 'name_logout'),
    path('admin',views.AllHistory,name = 'name_admin'),
    path('history/<int:user_id>',views.PersonalHistory,name = 'name_personalhistory'),
]