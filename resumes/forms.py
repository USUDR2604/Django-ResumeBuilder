from django import forms
from django.contrib.auth.models import User
from .models import *

EXP_INTERN_CHOICES=(('YES',"YES"),("NO","NO"))
GENDER_CHOICES=(("MALE","MALE"),("FEMALE","FEMALE"),("OTHERS","OTHERS"))
#from .Choices import *
EXPERIENCE_CHOICES=(("YES","YES"),("NO","NO"))
INTERNSHIP_CHOICES=(("YES","YES"),("NO","NO"))
class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model=ContactDetails
        exclude=['user']

class PersonalDetailForm(forms.ModelForm):
    Gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
    class Meta:
        model=PersonalDetails
        exclude=['user']
        #fields=['Experience','Internship','Gender','DOB','Photo']
        
class LanguageDetailForm(forms.ModelForm):
    class Meta:
        model=LanguageDetails
        exclude=['user']

class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model=SocialMediaLinks
        exclude=['user']

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skills
        fields=['Skill_Name','Skill_Percentage']
    
class InterestDetailForm(forms.ModelForm):
    class Meta:
        model = Interests
        exclude=['user']

class EducationDetailForm(forms.ModelForm):
    class Meta:
        model=EducationDetails
        exclude=['user']
        widgets ={
            'Year_Passing' : forms.DateInput(attrs={'title': 'Passing Date'}),}

class SoftSkillDetailForm(forms.ModelForm):
    class Meta:
        model = SoftSkills
        exclude =['user']

class ActivityAchievementDetailForm(forms.ModelForm):
    class Meta:
        model = AchievementsOrActivities
        exclude=['user']
        labels = {
            'ActAchiev_Choice': 'Activity Or Achievement',
        }

class ProjectDetailForm(forms.ModelForm):
    class Meta:
        model=ProjectDetails
        fields=['Project_Name','Project_Url','Project_Description','Project_Position']

class TrainingDetailForm(forms.ModelForm):
    class Meta:
        model=TrainingDetails
        exclude=['user']

class ExperienceDetailForm(forms.ModelForm):
    class Meta:
        model=ExperienceDetails
        exclude=['user']

class InternshipDetailForm(forms.ModelForm):
    class Meta:
        model=InternshipDetails
        exclude=['user']
class CertificationDetailForm(forms.ModelForm):
    class Meta:
        model=CertificationDetails
        exclude=['user']
class StrengthWeaknessForm(forms.ModelForm):
    class Meta:
        model=StrengthWeakness
        fields=['Strengths','Weakness']

class HobbieDetailForm(forms.ModelForm):
    class Meta:
        model=HobbieDetails
        fields=['Hobbie']

class SummaryDetailForm(forms.ModelForm):
    class Meta:
        model=SummaryDetails
        exclude=['user']