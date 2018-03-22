from django.urls import path

from . import views

app_name = 'extract'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('', views.index, name='index'),
    # # ex: /extract/5/
    # path('<int:topic_id>/', views.details, name='details'),
]