from django.urls import path
from . import views


app_name = "borrow"
urlpatterns = [
    path('',views.index, name = 'homepage'),
    path('login',views.login_i,name = 'login'),
    path('register',views.register, name = 'register'),
    path('logout',views.logout_i, name = 'logout'),
    path('history',views.AllHistory,name = 'history'),
    path('history/<int:user_id>',views.PersonalHistory,name = 'userprofile'),
    path('detail/<int:record_id>',views.Detail),
]