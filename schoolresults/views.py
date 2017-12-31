from django.shortcuts import render
from django.shortcuts import render_to_response ,render,get_object_or_404,redirect
from .models import *
import webbrowser
import smtplib as p
from django.core.files import File
import random


def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        email = request.POST.get("email" , None)
        password = request.POST.get("password" , None)
        emails_query = student.objects.all()
        emails = []
        for x in emails_query:
            emails.append(x.email)
        if email in emails:
            return render(request,"index.html" , {"msg":"Email already used"})
        
        user = student(name = name , email = email , password = password)
        user.save()
        num = user.semester_set.count()
        semesters = user.semester_set.all()
        
        return render(request,"profile.html" ,{"user":user,"num":num,"semesters":semesters,} )
    else:
        return render(request,"index.html")
    
def show_semester(request,name,user):
    user = student.objects.get(name = user)
    num = user.semester_set.count()
    semesters = user.semester_set.all()
    semester = user.semester_set.get(name = name)
    marks = semester.marks_set.all()
    mark = marks[0]
    return render(request, "profile_show.html",{"user":user,"num":num,"semesters":semesters,"semester":semester,"marks":mark})
def add_semester(request,email):
    user = student.objects.get(email=email)
    return render(request, "add-semester.html",{"user":user})
def add_semester_save(request,email):
    user = student.objects.get(email=email)
    if request.method == "POST":
        sem_name = request.POST.get("sem-name",None)
        eng_class = int(request.POST.get("eng-class-score",None))
        eng_exam = int(request.POST.get("eng-exam-score",None))
        eng_total = float((eng_class+eng_exam)/2)
        soc_class = int(request.POST.get("soc-class-score",None))
        soc_exam = int(request.POST.get("soc-exam-score",None))
        soc_total = float((soc_class+soc_exam)/2)
        science_class = int(request.POST.get("science-class-score",None))
        science_exam = int(request.POST.get("science-exam-score",None))
        science_total = float((science_class+science_exam)/2)
        math_class = int(request.POST.get("math-class-score",None))
        math_exam = int(request.POST.get("math-exam-score",None))
        math_total = float((math_class+math_exam)/2)
        
        semester = user.semester_set.create(name = sem_name)
        
        marks = semester.marks_set.create(
            English_class = eng_class,
            English_exam = eng_exam,
            English_result = eng_total,
            Science_class = science_class,
            Science_exam = science_exam,
            Science_result = science_total,
            social_class = soc_class,
            social_exam = soc_exam,
            social_result = soc_total,
            maths_class = math_class,
            maths_exam = math_exam,
            maths_result = math_total
        )
        marks.save()
        num = user.semester_set.count()
        semesters = user.semester_set.all()
        return render(request, "profile_show.html",{"user":user,"num":num,"semesters":semesters,"semester":semester,"marks":marks})
    else:
        return render(request, "add-semester.html",{"user":user})
        
def show_profile(request,email):
    user= student.objects.get(email = email)
    num = user.semester_set.count()
    semesters = user.semester_set.all()
    return render(request,"profile.html" ,{"user":user,"num":num,"semesters":semesters,} )
    
def login(request):
    if request.method == "POST":
        email = request.POST.get("email",None)
        password = request.POST.get("password",None)
        
        user = student.objects.get(email = email)
        if user.password == password:
            num = user.semester_set.count()
            semesters = user.semester_set.all()
            return render(request,"profile.html" ,{"user":user,"num":num,"semesters":semesters,} )
        else:
            msg = "Password incorrect"
            return render(request,"index.html" , {"log_msg":msg})
    else:
        return render(request,"index.html")
    
