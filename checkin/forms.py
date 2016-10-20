from django import forms
import re

class CheckinForm(forms.Form):
    student_id = forms.CharField(max_length=10)
    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if re.match('^[0-9]{10}$',student_id):
            return student_id
        else:
            raise forms.ValidationError('请输入有效学号')
