from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CheckinForm
from .models import Student,Checkin
from django.utils import timezone
import datetime

def index(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
        try:
            student = Student.objects.get(student_id = student_id)
            if (student.lastcheckintime == datetime.date.today()):
                return HttpResponse("你今天已经签过到！")
            student.checkintimes = student.checkintimes+1
            student.lastcheckintime = datetme.date.today()
            student.save()
            checkinrecord = Checkin(student = student)
            checkinrecord.save()
        except:
            student = Student(student_id = student_id,checkintimes = 1)
            student.save()
            checkinrecord = Checkin(student = student)
            checkinrecord.save()
        return HttpResponse("签到成功")
    else:
        form = CheckinForm()
    try:
        checkinlist = Checkin.objects.filter(time__startswith = datetime.date.today()).order_by('time')
    except:
        checkinlist = []
    return render(request,'checkin/index.html',{'form':form,'checkinlist':checkinlist})

def search(request):
    student_id = request.GET.get('student_id','')
    return HttpResponseRedirect("/{0}/".format(student_id))

def detail(request,student_id):
    try:
        student = Student.objects.get(student_id = student_id)
        #result = True
    except:
        #result = False
        return HttpResponse("还未签到过！")
    return render(request,'checkin/detail.html',{'student':student})
