from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('about/', views.AboutPage.as_view(), name="about"),
    path('question/<int:question_id>/',views.detail,name="detail"),
    path('question/<int:question_id>/vote',views.vote,name='vote'),
    path('home',views.homey,name='homey'),
    path('recentquestions',views.GetRescentQuestions.as_view(),name="rescentquestions"),
]