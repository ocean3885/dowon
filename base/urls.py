from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sub-intro/', views.sub_intro, name="sub-intro"),
    path('submit-jm/', views.submit_jm, name="submit-jm"),
    path('edit-submit/', views.edit_submit, name="edit-submit"),
    path('edit-submit-sj/', views.edit_submit_sj, name="edit-submit-sj"),
    path('submit-gm/', views.submit_gm, name="submit-gm"),
    path('submit-sj/', views.submit_sj, name="submit-sj"),
    path('find-submit/', views.find_submit, name="find-submit"),
    path('submit/delete/', views.delete_submit, name="delete-submit"),
    path('submit-info/', views.submit_info, name="submit-info"),
    path('about-saju/', views.about_saju, name="about-saju"),
    path('about-naming/', views.about_naming, name="about-naming"),
    path('certification/', views.certification, name="certification"),
    path('about-jm/', views.about_jm, name="about-jm"),

]
