from django.shortcuts import render,redirect,get_object_or_404
from .models import student

def dashboard(request):
    student_list = student.objects.all()
    return render(request,"students/dashboard.html",{"students":student_list})

def add_student(request):
    if request.method == "POST":
      student_model = student(
            name = request.POST.get("name"),
            roll = request.POST.get("roll"),
            email = request.POST.get("email"),
            department = request.POST.get("department"),
        )
      student_model.save()
    if request.method == "GET":
       return render(request,"students/add_student.html")


    return redirect("dashboard")


def del_student(request, id):
   student_object = get_object_or_404(student, id=id)
   student_object.delete()
   return redirect("dashboard")