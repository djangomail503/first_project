from django.urls import path, re_path
from . import views

urlpatterns = [

    path('home/', views.app_fn, name='app_home'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<pk>\d{1})/$', views.demo_fn, name='calendar'),

    
    #path('<device>/<dev_name>/',  views.dev_fn, name='device' ),

    #path('<int:year>/<int:month>/',  views.demo_fn, name='calender'),

    #re_path(r'^(?P<year>[0-9]{4})/<int:month>/$',  views.demo_fn, name='calender'),

    ##########

    path('register/',  views.register_view, name='register'),
    path('profile/',  views.user_profile_view, name='profile'),
    path('view_profile/', views.profile_view_fn, name='profile_view'),

    path('user_register/', views.user_create_view, name='user_register'),

    path('user_login/', views.user_login, name='login_user'),

    path('user_logout/', views.user_logout, name='logout_user'),


    ###########

    path('post_create/', views.PostCreateView.as_view(), name='post_create')












] 