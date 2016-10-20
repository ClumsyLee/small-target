from django.contrib import admin
from .models import Student,Checkin

# Register your models here.

class CheckinInline(admin.StackedInline):
    model = Checkin
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    fields = ['student_id','lastcheckintime','checkintimes']
    inlines = [CheckinInline]

admin.site.register(Student,StudentAdmin)
