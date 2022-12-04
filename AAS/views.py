from ast import Not
from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as logout1
from django.contrib.auth import login



from multiprocessing import context
from os import name
from django.shortcuts  import render
from django.http import HttpResponse  
from django.contrib import messages
from django.contrib import messages
from pathlib import Path
from django.contrib.auth.decorators import login_required
from AAS.models import Contactus
from AAS.models import Course
from AAS.models import AttendanceImage


import os
import pandas as pd
import io
import csv

from datetime import datetime
from datetime import time
g=datetime.now().strftime("%b %d %Y")
current_time = datetime.now().strftime('%I:%M %p')  

# Create your views here.

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


@login_required(login_url='login')
def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form , 'date': g ,'time': current_time}

    return render(request, 'AAS/index.html', context )


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')


# Create your views here.
def contactus(request):
        if request.method == "POST":

            name = request.POST.get('name')
            email = request.POST.get('email')
            utype = request.POST.get('utype')
            message = request.POST.get('message')
            contactus =Contactus( name= name, email= email, utype=utype,  message=message, date=datetime.today() )
            contactus.save()
            messages.success(request, 'Message sent sucessfully our team get in touch soon.')
            return render(request, 'AAS/index.html')
        else:
            return render(request, 'AAS/contactus.html')

# def sendmail(request):
#      if request.method == "POST":
        
#         name = request.POST['name']
#         email = request.POST['email']
#         utype = request.POST['utype']
#         message = request.POST['message']

#         send_mail(
#             name,
#             message,
#             'sp19-bcs-040@cuiwah.edu.pk',
#             ['us4m4.27@gmail.com'],
#             fail_silently=False,
#             )   
#         return render(request, 'AAS/contactus.html')

def landingpage(request):

    return render(request, 'AAS/homee.html')
def dashboard(request):

    return render(request, 'AAS/draft.html' , {'date': g ,'time': current_time})


def attn(request):
    
    return render(request, 'AAS/attendance.html' , {'date': g ,'time': current_time})

def login(request):
    
    

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password  )
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Profile Login Successfully.')
            return redirect('index')    

        else:
           messages.info(request, 'Either Username or Password in incorrect')
    return render(request, 'AAS/login_register.html')




def logout(request):
    logout1(request)

    return redirect('landingpage')

def register(request):
    
    return render(request, 'AAS/login_register.html' )


# base bath
BASE_DIR = Path(__file__).resolve().parent.parent





# all present student will show here 
@login_required(login_url='login')
def present_student(request):
    path = os.path.join(BASE_DIR, "AAS", 'ImagesAttendance')
    images = []
    classNames = []
    myList = os.listdir(path)
    myimg =os.listdir(path)
    for cl in myList:
        classNames.append(os.path.splitext(cl)[0])
    mylist = zip(classNames, myList)
    context = {
                'mylist': mylist,
            }
    my_csv = os.path.join(BASE_DIR, "AAS", 'Attendance.csv')
    reader = pd.read_csv(my_csv)
    csv_fp = open(f'{my_csv}', 'r+')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    student_data =[]
    for x in out:
        # print(x)
        student_data.append({"name": x['Name'], "time":x['Time'] , "date":x['Date']})
    return render(request, 'AAS/present_student.html',  {'data' : student_data, 'headers' : headers, 'clsimg':mylist ,'date': g ,'time': current_time})


@login_required(login_url='login')
def searcha(request):
    path = os.path.join(BASE_DIR, "AAS", 'ImagesAttendance')
    images = []
    classNames = []
    myList = os.listdir(path)
    myimg =os.listdir(path)
    for cl in myList:
        classNames.append(os.path.splitext(cl)[0])
    mylist = zip(classNames, myList)
    context = {
                'mylist': mylist,
            }
    my_csv = os.path.join(BASE_DIR, "AAS", 'Attendance.csv')
    reader = pd.read_csv(my_csv)
    csv_fp = open(f'{my_csv}', 'r+')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    student_data =[]
    for x in out:
        # print(x)
        student_data.append({"name": x['Name'], "time":x['Time'] , "date":x['Date']})
    
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            products = student_data.object.filter(name__icontains=q)
            return render(request, 'AAS/present_student.html',  {'data' : student_data, 'headers' : headers, 'clsimg':mylist ,'date': g ,'time': current_time})

        else :
            return render(request, 'AAS/present_student.html',  {'data' : student_data, 'headers' : headers, 'clsimg':mylist ,'date': g ,'time': current_time})


    return render(request, 'AAS/present_student.html',  {'data' : student_data, 'headers' : headers, 'clsimg':mylist ,'date': g ,'time': current_time})


# ================ Attendance page and ML Model depolyment  =================== 
@login_required(login_url='login')
def Attendance(request):

    

    from fileinput import filename
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    import face_recognition
    import os
    from base64 import encode
    from datetime import datetime
    from datetime import date
    from django.shortcuts import redirect
    
    



    my_csv = os.path.join(BASE_DIR, "AAS", 'Attendance.csv')
    path = os.path.join(BASE_DIR, "AAS", 'ImagesAttendance')
    # print(csv path: ', my_csv)

    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print('these are the name ================>',  classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        # with open('Attendance.csv','r+') as f:
        with open(my_csv,'r+') as f:
            myDataList = f.readlines()
            nameList = []

            print('======================== name:  ', nameList)

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                today = date.today()
                dtString = now.strftime('%H:%M:%S')
                dtStrings = today.strftime("%b-%d-%Y")
                f.writelines(f'\n{name},{dtString},{dtStrings}')
                


    encodeListKnown = findEncodings(images)
    print(len(encodeListKnown))

    cap = cv2.VideoCapture(0)
    
    while True:
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis) 
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,255),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,255),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                markAttendance(name)
                # return redirect('present_student') 
                #redirect('present_student')
                # def my_function():
                #     print("Hello from a function")
                #     return redirect('present_student') 

                
        


        flip_image = cv2.flip(img, flipCode=1)
        cv2.imshow('Webcam',flip_image)
        cv2.waitKey(1)
        # return render(request, 'AAS/attendance.html')
       
# Attendanceimgs_____________________________________________
@login_required(login_url='login')
def class_room(request):
    my_csv = os.path.join(BASE_DIR, "AAS", 'Attendance.csv')
    # reader = pd.read_csv(my_csv['name'][0])

    my_csv = os.path.join(BASE_DIR, "AAS", 'Attendance.csv')
    path = os.path.join(BASE_DIR, "AAS", 'ImagesAttendance')
    # print(csv path: ', my_csv)

    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        classNames.append(os.path.splitext(cl)[0])

    mylist = zip(classNames, myList)
    context = {
                'mylist': mylist,
                'date': g,
                'time': current_time,
            }

    return render(request, 'AAS/', context )
    # return render(req, 'home.html', context)




# ============= CRUD =============================

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from AAS.models import Student
import os



# ===================== show all student data =============================== 




@login_required(login_url='login')
def searchc(request):

    products = Student.objects.all()
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            products = Student.objects.filter(name__icontains=q)
            context = { 'products':products,'date': g ,'time': current_time}
            return render(request, 'AAS/searchc.html', context)
        else :
            products = Student.objects.all()
            context = { 'products':products,'date': g ,'time': current_time}
            return render(request, 'AAS/class_room.html', context)

@login_required(login_url='login')
def searchm(request):

    products = Student.objects.all()
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            products = Student.objects.filter(name__icontains=q)
            context = { 'products':products,'date': g ,'time': current_time}
            return render(request, 'AAS/searchm.html', context)
        else :
            products = Student.objects.all()
            context = { 'products':products,'date': g ,'time': current_time}
            return render(request, 'AAS/students/index.html', context)




@login_required(login_url='login')
def class_room(request):
    products = Student.objects.all()
    context = {'products':products
    , 'date': g ,'time': current_time}
    return render(request, 'AAS/class_room.html', context)

@login_required(login_url='login')
def students(request):
    products = Student.objects.all()
    context = {'products':products
    , 'date': g ,'time': current_time}
    return render(request, 'AAS/students/index.html', context)



# ===================== add student =============================== 
@login_required(login_url='login')
def add_student(request):
    if request.method == "POST":
        prod = Student()
        prod.name = request.POST.get('name')
        prod.father_name = request.POST.get('father_name')
        prod.dob = request.POST.get('dob')
        prod.Reg = request.POST.get('reg')
        prod.gender = request.POST.get('gender')
        prod.ph = request.POST.get('ph')
        prod.email = request.POST.get('email')
        prod.cnic = request.POST.get('cnic')
        prod.nationality = request.POST.get('nationality')
        prod.status = request.POST.get('status')
        prod.bgroup = request.POST.get('bgroup')
        prod.address = request.POST.get('address')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Student Added Successfully")
        return redirect('/students')
    return render(request, 'AAS/students/add_student.html',{'date': g ,'time': current_time})



# ===================== Edit student page =============================== 
@login_required(login_url='login')
def editProduct(request, pk):
    prod = Student.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.father_name = request.POST.get('father_name')
        prod.dob = request.POST.get('dob')
        prod.Reg = request.POST.get('reg')
        prod.gender = request.POST.get('gender')
        prod.ph = request.POST.get('ph')
        prod.email = request.POST.get('email')
        prod.cnic = request.POST.get('cnic')
        prod.nationality = request.POST.get('nationality')
        prod.status = request.POST.get('status')
        prod.bgroup = request.POST.get('bgroup')
        prod.address = request.POST.get('address')
        prod.save()
        messages.success(request, "Student Updated Successfully")
        return redirect('/students')

    context = {'prod':prod
    ,'date': g ,'time': current_time}
    return render(request, 'AAS/students/edit.html', context )


# ===================== Delete student =============================== 
@login_required(login_url='login')
def deleteProduct(request, pk):
    prod = Student.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request,"Student Deleted Successfuly")
    return redirect('/students')  


# ===================== show student details =============================== 
@login_required(login_url='login')
def view_student(request, pk):
    prod = Student.objects.get(id=pk)
    context = {'prod':prod, 'date': g ,'time': current_time}
    return render(request, 'AAS/students/view.html', context)

    




