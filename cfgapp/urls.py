from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('raise-issue/', views.raiseIssue, name='raiseIssue'),
    path('issue-page/', views.issuePage, name='issuePage'),
    path('logout/', views.logout_user, name='logout'),
    path('water-quality/', views.waterQuality, name='waterQuality'),
    path('quality-measures', views.qualityMeasures, name='qualityMeasures'),
    path('adm/', views.adm, name='adm'),
    path('pumpOperator/', views.pumpOperator, name='pumpOperator'),
    path('base', views.base, name='base'),
]