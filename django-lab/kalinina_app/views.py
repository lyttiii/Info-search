from django.shortcuts import render

from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import University, Student
from .forms import UniversityForm, StudentForm


def index(request):
    return TemplateResponse(request, "index.html")


def university_list(request):
    universities = University.objects.all()
    data = {"universities": universities}
    return TemplateResponse(request, "university_list.html", data)


def create_university(request):
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/kalinina_app/university/")
        else:
            return TemplateResponse(request, "create_university.html", {"form": form})
    else:
        form = UniversityForm()
        return TemplateResponse(request, "create_university.html", {"form": form})


def edit_university(request, university_id):
    try:
        university = University.objects.get(id=university_id)
        if request.method == "POST":
            form = UniversityForm(request.POST, instance=university)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/kalinina_app/university/")
            else:
                return TemplateResponse(request, "edit_university.html", {"form": form, "university": university})
        else:
            form = UniversityForm(instance=university)
            return TemplateResponse(request, "edit_university.html", {"form": form, "university": university})
    except University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")


def delete_university(request, university_id):
    try:
        university = University.objects.get(id=university_id)
        university.delete()
        return HttpResponseRedirect("/kalinina_app/university/")
    except University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")


def student_list(request):
    students = Student.objects.all()
    data = {"students": students}
    return TemplateResponse(request, "student_list.html", data)


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/kalinina_app/student/")
        else:
            return TemplateResponse(request, "create_student.html", {"form": form})
    else:
        form = StudentForm()
        return TemplateResponse(request, "create_student.html", {"form": form})


def edit_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        if request.method == "POST":
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/kalinina_app/student/")
            else:
                return TemplateResponse(request, "edit_student.html", {"form": form, "student": student})
        else:
            form = StudentForm(instance=student)
            return TemplateResponse(request, "edit_student.html", {"form": form, "student": student})
    except Student.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")


def delete_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        return HttpResponseRedirect("/kalinina_app/student/")
    except Student.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")
