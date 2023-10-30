
from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('Logout/',views.Logout,name="Logout"),
    path('user_home/',views.user_home,name="user_home"),
    path('view_users/',views.view_users,name="view_users"),
    path('delete_user\<int:pid>/', views.delete_user, name="delete_user"),
    path('add_book/',views.add_book,name="add_book"),
    path('view_book_admin/',views.view_book_admin,name="view_book_admin"),
    path('delete_book/<int:id>/',views.delete_book,name="delete_book"),
    path('edit_book<int:pid>/',views.edit_book,name="edit_book"),
    path('change_bookimage/<int:id>/',views.change_bookimage,name="change_bookimage"),
    path('change_passwordadmin/', views.change_passwordadmin, name="change_passwordadmin"),
    path('view_feedback/',views.view_feedback,name="view_feedback"),
    path('feedback/',views.feedback,name="feedback"),
    path('delete_feedback/<int:id>/',views.delete_feedback,name="delete_feedback"),
    path('view_book_user/',views.view_book_user,name="view_book_user"),
    path('buy_now/<int:pid>/',views.buy_now,name="buy_now"),
    path('rent_book/<int:id>/',views.rent_book,name="rent_book"),
    path('view_booking/',views.view_booking,name="view_booking"),
    path('cancel_booking/<int:id>/', views.cancel_booking, name="cancel_booking"),
    path('change_passworduser/',views.change_passworduser,name="change_passworduser"),
    path('contact/', views.contact, name="contact"),
    path('delete_contact/<int:id>/', views.delete_contact, name="delete_contact"),
    path('view_booking_admin/',views.view_booking_admin,name="view_booking_admin"),
    path('delete_booking/<int:id>/',views.delete_booking,name="delete_booking"),
    path('change_status/<int:id>/', views.change_status, name="change_status"),
    path('search/', views.search, name="search"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
