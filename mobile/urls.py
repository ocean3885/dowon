from django.urls import path,include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.m_home, name="m-home"),
    path('m-submit-jm/', views.m_submit_jm, name="m-submit-jm"),
    path('m-submit-gm/', views.m_submit_gm, name="m-submit-gm"),
    path('m-submit-sj/', views.m_submit_sj, name="m-submit-sj"),
    path('m-edit-submit/', views.m_edit_submit, name="m-edit-submit"),
    path('m-edit-submit-sj/', views.m_edit_submit_sj, name="m-edit-submit-sj"),
    path('m-delete-submit/', views.m_delete_submit, name="m-delete-submit"),
    path('m-find-submit/', views.m_find_submit, name="m-find-submit"),
    path('m-submit-detail/<int:pk>', views.m_submit_detail, name="m-submit-detail"),
    path('m-sub-intro/', views.m_sub_intro, name="m-sub-intro"),
    path('m-about-jm/', views.m_about_jm, name="m-about-jm"),
    path('m-about-naming/', views.m_about_naming, name="m-about-naming"),
    path('m-about-sj/', views.m_about_sj, name="m-about-saju"),
    path('m-about-way/', views.m_about_way, name="m-about-way"),
    path('m-certification/', views.m_certification, name="m-certification"),
    path('m-submit-info/', views.m_submit_info, name="m-submit-info"),
    path('m-board/', views.m_board, name="m-board"),
]
