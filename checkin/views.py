from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CheckinForm
from .models import Student,Checkin
from django.utils import timezone
import datetime

TIPS = [
    'tip1 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip2 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip3 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip4 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip5 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip6 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip7 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'tip8 Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
]

FIRST_DAY = datetime.date(2016, 10, 19)

def index(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            try:
                student = Student.objects.get(student_id = student_id)
                if student.lastcheckintime != datetime.date.today():
                    student.checkintimes = student.checkintimes+1
                    student.lastcheckintime = datetme.date.today()
                    student.save()
                    checkinrecord = Checkin(student = student)
                    checkinrecord.save()
            except:
                student = Student(student_id = student_id, checkintimes = 1)
                student.save()
                checkinrecord = Checkin(student = student)
                checkinrecord.save()
            return render(request, 'checkin/checkin_success.html',
                          {'student': student, 'tip': get_tip()})
    else:
        form = CheckinForm()

    return render(request, 'checkin/index.html',
                  {'form': form, 'checkinlist': get_today_checkinlist()})

def search(request):
    student_id = request.GET.get('student_id','')
    return HttpResponseRedirect("/{0}/".format(student_id))

def today(request):
    return render(request, 'checkin/today.html',
                  {'checkinlist': get_today_checkinlist()})

def summary(request):
    try:
        students = Student.objects.order_by('-checkintimes', 'student_id')
    except:
        students = []
    return render(request, 'checkin/summary.html', {'students': students})

def detail(request,student_id):
    try:
        student = Student.objects.get(student_id = student_id)
    except:
        student = Student(student_id=student_id, checkintimes=0)

    return render(request,'checkin/detail.html',{'student':student})

def get_today_checkinlist():
    try:
        return Checkin.objects.filter(time__startswith = datetime.date.today()).order_by('time')
    except:
        return []

def get_tip():
    k_day = (datetime.date.today() - FIRST_DAY).days
    return TIPS[k_day % len(TIPS)]
