from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('university/', views.university_list, name='university_list'),
    path('university/create', views.create_university, name='create_university'),
    path('university/edit/<int:university_id>', views.edit_university, name='edit_university'),
    path('university/delete/<int:university_id>', views.delete_university, name='delete_university'),
    path('student/', views.student_list, name='student_list'),
    path('student/create', views.create_student, name='create_student'),
    path('student/edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>', views.delete_student, name='delete_student'),
]


