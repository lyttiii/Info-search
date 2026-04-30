from django.contrib import admin
from .models import University, Student
from .forms import UniversityForm, StudentForm


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name', 'creation_date')
    form = UniversityForm

admin.site.register(University, UniversityAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'university', 'enrollment_year')
    form = StudentForm

admin.site.register(Student, StudentAdmin)

