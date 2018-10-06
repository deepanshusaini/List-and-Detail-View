from django.urls import path
from app_one import views
app_name = 'app_one'
urlpatterns = [
    path('',views.List.as_view(),name='list'),
    path('<int:pk>/', views.Detail.as_view(), name='student_details'),

]
