from .models import *
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    school_ID = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password'
        ]

class BorrowRecordForm(forms.ModelForm):

    class Meta:
        model = BorrowRecord
        fields = [ 
            'StartTime',
            'EndTime',
            'StuffToUse', 
            'OtherRequests',
            'RoomToUse', 
            # 'borrower',
            #is_approved is excluded
        ]

