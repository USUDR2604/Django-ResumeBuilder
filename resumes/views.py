from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, User
#from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
#from django.contrib import messages
from .forms import *
from .models import *
from django.forms import formset_factory 
from django.views.generic import View
from django.template.loader import get_template,render_to_string
from django.template import Context
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .utils import *
#importing get_template from loader
from django.views.generic import View
import pdfkit
from django.http import HttpResponse
from django.template import loader
import os
import tempfile

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resumes:login')
    else:
        form = UserCreationForm()
    return render(request,'resumes/AllTemplates/Registration.html',{'form':form})
    
def SignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'resumes/AllTemplates/login.html', {'form': form, 'msg': '* Username or Password Incorrect'})
        else:
            login(request, user)
            return redirect('resumes:Home')
    return render(request, 'resumes/AllTemplates/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('resumes:Home')

# Create your views here.
def HomeView(request):
    if request.user.is_authenticated:
        return render(request, 'resumes/AllTemplates/Home.html',{})
    else:
        return redirect('resumes:login')

@login_required(login_url='MyResume/login')
def ProfileDetailView(request):
    return render(request,'resumes/AllTemplates/ProfileDetails.html',{})

def AboutView(request):
    return render(request,'resumes/AllTemplates/About.html',{})

@login_required(login_url='MyResume/login')
def ResumePointView(request):
    return render(request, 'resumes/AllTemplates/AllResumeDetails.html',{})

@login_required(login_url='MyResume/login')
def CheckExperienceDetailView(request):
    return render(request,'resumes/AllTemplates/CheckExperienceDetails.html',{})

# Experience Resumes List
@login_required(login_url='MyResume/login')
def ExperienceResumesListView(request):
    return render(request,'resumes/AllTemplates/ExperienceResumeLists.html',{})

@login_required(login_url='MyResume/login')
def NoExperienceResumesListView(request):
    return render(request,'resumes/AllTemplates/NoExperienceResumeLists.html',{})

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data={
        'contactdet':ContactDetails.objects.filter(user=request.user).all(),
        'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
        'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
        'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
        'Skilldet' : Skills.objects.filter(user=request.user).all(),
        'Interestdet' : Interests.objects.filter(user= request.user).all(),
        'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
        'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
        'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
        'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
        'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
        'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
        'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all(),
        'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
        'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all(),
        'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
        'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
        pdf = render_to_pdf('resumes/ExperienceResumePdfViews/Resume1Pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class GenerateRes3Pdf(View):
    def get(self, request, *args, **kwargs):
        data={
        'contactdet':ContactDetails.objects.filter(user=request.user).all(),
        'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
        'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
        'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
        'Skilldet' : Skills.objects.filter(user=request.user).all(),
        'Interestdet' : Interests.objects.filter(user= request.user).all(),
        'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
        'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
        'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
        'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
        'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
        'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
        'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all(),
        'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
        'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all(),
        'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
        'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
        pdf = render_to_pdf('resumes/ExperienceResumePdfViews/Resume3PDF.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

############################# EXP PDF DETAILS #############################

def GeneratePDF2(request):
    data={ 
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
    'Skilldet' : Skills.objects.filter(user=request.user).all(),
    'Interestdet' : Interests.objects.filter(user= request.user).all(),
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all(),
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all(),
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
    template = get_template('resumes/ExperienceResumes/Resume2.html')
    html = template.render(data)
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ExpResume2.pdf"'
    return response    
   

def ExpResume1PDF(request):
    template_path = 'resumes/ExperienceResumePdfViews/Resume1Pdf.html'
    data={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
    'Skilldet' : Skills.objects.filter(user=request.user).all(),
    'Interestdet' : Interests.objects.filter(user= request.user).all(),
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all(),
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all(),
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ExpResume1.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(data)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

############################# EXP SHOW DETAILS ##############################

@login_required(login_url='MyResume/login')
def ExpShowDetailView(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
    'Skilldet' : Skills.objects.filter(user=request.user).all(),
    'Interestdet' : Interests.objects.filter(user= request.user).all(),
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all(),
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all(),
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
    return render(request,'resumes/AllTemplates/ExpShowDetails.html',context)

@login_required(login_url='MyResume/login')
def NoExpShowDetailView(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all(),
    'Skilldet' : Skills.objects.filter(user=request.user).all(),
    'Interestdet' : Interests.objects.filter(user= request.user).all(),
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all(),
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all(),
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all(),
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all(),
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all(),
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all(),
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all(),
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all(),
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()}
    return render(request,'resumes/AllTemplates/NoExpShowDetails.html',context)




@login_required(login_url='MyResume/login')
def ExperienceResume1view(request):
# Experience Templates
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:4],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:3],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:3],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:2],
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/ExperienceResumes/ExpResume1.html',context)

@login_required(login_url='MyResume/login')
def ExperienceResume2view(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:4],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:1],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:1],
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/ExperienceResumes/Resume2.html',context)

@login_required(login_url='MyResume/login')
def ExperienceResume3view(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:4],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:1],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:2],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:1],
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/ExperienceResumes/Resume3.html',context)

@login_required(login_url='MyResume/login')
def ExperienceResume4view(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:2],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:6],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:2],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:1],
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/ExperienceResumes/Resume4.html',context)

@login_required(login_url='MyResume/login')
def ExperienceResume5view(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:4],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:1],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:1],
    'Internshipdet' :InternshipDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Experiencedet' : ExperienceDetails.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/ExperienceResumes/Resume5.html',context)

# NoExperienceResumes
@login_required(login_url='MyResume/login')
def NoExperienceResume1View(request):
    context={
    'contactdet' : ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:3],
    'SoftSkillDet' : SoftSkills.objects.filter(user=request.user).all()[:4],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'ActAchievdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:3],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:1],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1],}
    return render(request, 'resumes/NoExperienceResumes/NoExpResume1.html',context)
@login_required(login_url='MyResume/login')
def NoExperienceResume2View(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all(),
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'ActAchievdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:2],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1],}
    return render(request,'resumes/NoExperienceResumes/NoExpResume2.html',context)

@login_required(login_url='MyResume/login')
def NoExperienceResume3View(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'ActAchievdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:2],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/NoExperienceResumes/NoExpResume3.html',context)

@login_required(login_url='MyResume/login')
def NoExperienceResume4View(request):
    context={
    'contactdet':ContactDetails.objects.filter(user=request.user).all(),
    'persondet' : PersonalDetails.objects.filter(user=request.user).all(),
    'Languagedet' : LanguageDetails.objects.filter(user=request.user).all()[:5],
    'SocialMediadet' : SocialMediaLinks.objects.filter(user=request.user).all()[:3],
    'Skilldet' : Skills.objects.filter(user=request.user).all()[:8],
    'Interestdet' : Interests.objects.filter(user= request.user).all()[:5],
    'Awardsdet' : AchievementsOrActivities.objects.filter(user=request.user).all()[:2],
    'SoftSkilldet' : SoftSkills.objects.filter(user=request.user).all()[:6],
    'Educationdet' : EducationDetails.objects.filter(user=request.user).all()[:2],
    'Projectdet' : ProjectDetails.objects.filter(user=request.user).all()[:2],
    'Trainingdet' : TrainingDetails.objects.filter(user=request.user).all()[:2],
    'Certifydet' : CertificationDetails.objects.filter(user=request.user).all()[:2],
    'StrengthWeakdet' : StrengthWeakness.objects.filter(user=request.user).all()[:2],
    'Hobbiedet' : HobbieDetails.objects.filter(user=request.user).all()[:3],
    'Summarydet' : SummaryDetails.objects.filter(user=request.user).all()[:1]}
    return render(request,'resumes/NoExperienceResumes/NoExpResume4.html',context)

#########################  EXPERIENCE RESUME TEMPLATE DETAILS  #########################

# Experience Resumes
@login_required(login_url='MyResume/login')
def ExpContactDetailView(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email_Id = request.POST['Email_Id']
        Mobile_No = request.POST['Mobile_No']
        Alternate_Mobile_No = request.POST['Alternate_Mobile_No']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Address = request.POST['Address']
        Address_2 = request.POST['Address_2']
        ContEdu = ContactDetails(user=request.user,First_Name=First_Name,Last_Name=Last_Name,Email_Id=Email_Id,Alternate_Mobile_No=Alternate_Mobile_No,Mobile_No=Mobile_No,Country=Country,State=State,Address_2=Address_2,City=City,ZipCode=ZipCode,Address=Address)
        ContEdu.save()
        return redirect('resumes:Exp-PersonalDetails')
    form=ContactDetailForm()
    return render(request,'resumes/Experience-Templates/ContactDetails.html',{'form':form})
    
@login_required(login_url='MyResume/login')
def ExpPersonalDetailView(request):
    if request.method == "POST":
        Photo = request.FILES['Photo']
        Experience = request.POST['Experience']
        Internship = request.POST['Internship']
        Gender = request.POST['Gender']
        DOB = request.POST['DOB']
        PersonDet=PersonalDetails(user=request.user,Photo=Photo,Experience=Experience,Internship=Internship,Gender=Gender,DOB=DOB)
        PersonDet.save()
        return redirect('resumes:Exp-SocialMediaDetails')
    form=PersonalDetailForm()
    return render(request,'resumes/Experience-Templates/PersonalDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpLanguageDetailView(request):
    if request.method=='POST':
        Language_Name = request.POST['Language_Name']
        Language_Confidence = request.POST['Language_Confidence']
        LanguageDet=LanguageDetails(user=request.user,Language_Name=Language_Name,Language_Confidence=Language_Confidence)
        LanguageDet.save()
        return redirect('resumes:AddExpLanguages')
    form=LanguageDetailForm()
    return render(request,'resumes/Experience-Templates/Languages.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpSocialMediaLinkView(request):
    if request.method=='POST':
        SocialMedia_Website_Name=request.POST['SocialMedia_Website_Name']
        SocialMedia_Link=request.POST['SocialMedia_Link']
        SocialMediaDet=SocialMediaLinks(user=request.user,SocialMedia_Website_Name=SocialMedia_Website_Name,SocialMedia_Link=SocialMedia_Link)
        SocialMediaDet.save()
        return redirect('resumes:AddExpSocialMedia')
    form=SocialMediaLinkForm()
    return render(request,'resumes/Experience-Templates/SocialMediaLinks.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpSkillDetailView(request):
    if request.method=='POST':
        Skill_Name=request.POST['Skill_Name']
        Skill_Percentage=request.POST['Skill_Percentage']
        SkillDet=Skills(user=request.user,Skill_Name=Skill_Name,Skill_Percentage=Skill_Percentage)
        SkillDet.save()
        return redirect('resumes:AddExpSkills')
    form=SkillForm()
    return render(request,'resumes/Experience-Templates/SkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpInterestDetailView(request):
    if request.method=='POST':
        Interest_Names = request.POST['Interest_Names']
        InterestDet = Interests(user=request.user,Interest_Names=Interest_Names)
        InterestDet.save()
        return redirect('resumes:AddExpInterests')
    form=InterestDetailForm()
    return render(request,'resumes/Experience-Templates/InterestDetails.html',{'form':form}) 

@login_required(login_url='MyResume/login')
def ExpSoftSkillDetailView(request):
    if request.method=='POST':
        SoftSkill_Name = request.POST['SoftSkill_Name']
        SoftSkilldet = SoftSkills(user=request.user,SoftSkill_Name=SoftSkill_Name)
        SoftSkilldet.save()
        return redirect('resumes:AddExpSoftSkills')
    form = SoftSkillDetailForm()
    return render(request,'resumes/Experience-Templates/SoftSkillDetails.html',{'form':form}) 

@login_required(login_url='MyResume/login')
def ExpAchievementsOrActivitiesDetailView(request):
    if request.method=='POST':
        Achievement_Name = request.POST['Achievement_Name']
        ActAchiev_Choice = request.POST['ActAchiev_Choice']
        Achievement_Description = request.POST['Achievement_Description']
        Achievementdet = AchievementsOrActivities(user=request.user,Achievement_Name=Achievement_Name,ActAchiev_Choice=ActAchiev_Choice,Achievement_Description=Achievement_Description)
        Achievementdet.save()
        return redirect('resumes:AddExpActivityAchievements')
    form = ActivityAchievementDetailForm()
    return render(request,'resumes/Experience-Templates/Achievements.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpStrengthWeaknessDetailView(request):
    if request.method=='POST':
        Strengths = request.POST['Strengths']
        Weakness = request.POST['Weakness']
        StrWeakDet=StrengthWeakness(user=request.user,Strengths=Strengths,Weakness=Weakness) 
        StrWeakDet.save()
        return redirect('resumes:AddExpStrengthWeakness')
    form=StrengthWeaknessForm()
    return render(request,'resumes/Experience-Templates/StrengthWeaknessDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpHobbieDetailView(request):
    if request.method=='POST':
        Hobbie = request.POST['Hobbie']
        HobDet = HobbieDetails(user=request.user,Hobbie=Hobbie)
        HobDet.save()
        return redirect('resumes:AddExpHobbies')
    form=HobbieDetailForm()
    return render(request,'resumes/Experience-Templates/HobbieDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpEducationDetailView(request):
    if request.method=='POST':
        Organization_Type = request.POST['Organization_Type']
        Country_Name = request.POST['Country_Name']
        State_Name = request.POST['State_Name']
        City_Name = request.POST['City_Name']
        ZipCode = request.POST['ZipCode']
        Organization_Name = request.POST['Organization_Name']
        Board_Of_Study = request.POST['Board_Of_Study']
        Field_Of_Study = request.POST['Field_Of_Study']
        Standard = request.POST['Standard']
        Year_Passing = request.POST['Year_Passing']
        Score = request.POST['Score']
        EduDet=EducationDetails(user=request.user,Organization_Type=Organization_Type,Country_Name=Country_Name,State_Name=State_Name,City_Name=City_Name,ZipCode=ZipCode,Organization_Name=Organization_Name,Board_Of_Study=Board_Of_Study,Field_Of_Study=Field_Of_Study,Standard=Standard,Year_Passing=Year_Passing,Score=Score)
        EduDet.save()
        return redirect('resumes:AddExpEducation')
    form=EducationDetailForm()
    return render(request,'resumes/Experience-Templates/EducationDetails.html',{'form':form})


@login_required(login_url='MyResume/login')
def ExpProjectDetailView(request):
    if request.method=='POST':
        Project_Name = request.POST['Project_Name']
        Project_Url = request.POST['Project_Url']
        Project_Description = request.POST['Project_Description']
        Project_Position = request.POST['Project_Position']
        projdet=ProjectDetails(user=request.user,Project_Name=Project_Name,Project_Url=Project_Url,Project_Description=Project_Description,Project_Position=Project_Position)
        projdet.save()
        return redirect('resumes:AddExpProjects')
    form=ProjectDetailForm()
    return render(request,'resumes/Experience-Templates/ProjectDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpTrainingDetailView(request):
    if request.method=='POST':
        Training_Type = request.POST['Training_Type']
        Training_Country = request.POST['Training_Country']
        Training_State = request.POST['Training_State']
        Training_City = request.POST['Training_City']
        Training_ZipCode = request.POST['Training_ZipCode']
        Training_Org_Name = request.POST['Training_Org_Name']
        Training_Course_Name = request.POST['Training_Course_Name']
        Training_startDate = request.POST['Training_startDate']
        Training_EndDate = request.POST['Training_EndDate']
        Training_Description = request.POST['Training_Description']
        TrainDet=TrainingDetails(user=request.user,Training_Type=Training_Type,Training_ZipCode=Training_ZipCode,Training_Country=Training_Country,Training_State=Training_State,Training_City=Training_City,Training_Org_Name=Training_Org_Name,Training_Course_Name=Training_Course_Name,Training_startDate=Training_startDate,Training_EndDate=Training_EndDate,Training_Description=Training_Description)
        TrainDet.save()
        return redirect('resumes:AddExpTrainingDetails')
    form=TrainingDetailForm()
    return render(request,'resumes/Experience-Templates/TrainingDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpCertificationDetailView(request):
    if request.method=='POST':
        Certification_Type = request.POST['Certification_Type']
        Certify_Country = request.POST['Certify_Country']
        Certify_State = request.POST['Certify_State']
        Certify_City = request.POST['Certify_City']
        Certify_Org_Name = request.POST['Certify_Org_Name']
        Certify_ZipCode = request.POST['Certify_ZipCode']
        Certify_Course_Name = request.POST['Certify_Course_Name']
        Certify_startDate = request.POST['Certify_startDate']
        Certify_EndDate = request.POST['Certify_EndDate']
        Certify_Description = request.POST['Certify_Description']
        CertDet=CertificationDetails(user=request.user,Certification_Type=Certification_Type,Certify_Country=Certify_Country,Certify_State=Certify_State,Certify_ZipCode=Certify_ZipCode,Certify_City=Certify_City,Certify_Org_Name=Certify_Org_Name,Certify_Course_Name=Certify_Course_Name,Certify_startDate=Certify_startDate,Certify_EndDate=Certify_EndDate,Certify_Description=Certify_Description)
        CertDet.save()
        return redirect('resumes:AddExpCertifications')
    form=CertificationDetailForm()
    return render(request,'resumes/Experience-Templates/CertificationDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpSummaryDetailView(request):
    if request.method=='POST':
        Summary = request.POST['Summary']
        Your_Position = request.POST['Your_Position']
        SummaryDet=SummaryDetails(user=request.user,Summary=Summary,Your_Position=Your_Position)
        SummaryDet.save()
        return redirect('resumes:Exp-ShowDetails')
    form=SummaryDetailForm()
    return render(request,'resumes/Experience-Templates/SummaryDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpExperienceDetailView(request):
    if request.method=='POST':
        Experience_choice = request.POST['Experience_choice']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Experience_Job_Name = request.POST['Experience_Job_Name']
        Experience_Job_Type = request.POST['Experience_Job_Type']
        Experience_Start_Date = request.POST['Experience_Start_Date']
        Experience_End_Date = request.POST['Experience_End_Date']
        Experience_Job_Description = request.POST['Experience_Job_Description']
        ExpDet=ExperienceDetails(user=request.user,Experience_choice=Experience_choice,Country=Country,State=State,City=City,ZipCode=ZipCode,Experience_Job_Name=Experience_Job_Name,Experience_Job_Type=Experience_Job_Type,Experience_Start_Date=Experience_Start_Date,Experience_End_Date=Experience_End_Date,Experience_Job_Description=Experience_Job_Description)
        ExpDet.save()
        return redirect('resumes:AddExpExperiences')
    form = ExperienceDetailForm()
    return render(request,'resumes/Experience-Templates/ExperienceDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def ExpInternshipDetailView(request):
    if request.method=='POST':
        Internship_choice = request.POST['Internship_choice']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Internship_Job_Type = request.POST['Internship_Job_Type']
        Internship_Company_Name = request.POST['Internship_Company_Name']
        Internship_Start_Date = request.POST['Internship_Start_Date']
        Internship_End_Date = request.POST['Internship_End_Date']
        Internship_Job_Description = request.POST['Internship_Job_Description']
        InternDet=InternshipDetails(user=request.user,Internship_choice=Internship_choice,Country=Country,State=State,City=City,Internship_Company_Name=Internship_Company_Name,ZipCode=ZipCode,Internship_Job_Type=Internship_Job_Type,Internship_Start_Date=Internship_Start_Date,Internship_End_Date=Internship_End_Date,Internship_Job_Description=Internship_Job_Description)
        InternDet.save()
        return redirect('resumes:AddExpInternships')
    form=InternshipDetailForm()
    return render(request, 'resumes/Experience-Templates/InternshipDetails.html',{'form':form})

#########################  ADD EXPERIENCE RESUME TEMPLATE DETAILS  #########################

# Add Experience Templates
@login_required(login_url='MyResume/login')
def ExpAddEducationDetailView(request):
    edudetail = EducationDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Organization_Type = request.POST['Organization_Type']
        Country_Name = request.POST['Country_Name']
        State_Name = request.POST['State_Name']
        City_Name = request.POST['City_Name']
        ZipCode = request.POST['ZipCode']
        Organization_Name = request.POST['Organization_Name']
        Board_Of_Study = request.POST['Board_Of_Study']
        Field_Of_Study = request.POST['Field_Of_Study']
        Standard = request.POST['Standard']
        Year_Passing = request.POST['Year_Passing']
        Score = request.POST['Score']
        EduDet=EducationDetails(user=request.user,Organization_Type=Organization_Type,Country_Name=Country_Name,State_Name=State_Name,City_Name=City_Name,ZipCode=ZipCode,Organization_Name=Organization_Name,Board_Of_Study=Board_Of_Study,Field_Of_Study=Field_Of_Study,Standard=Standard,Year_Passing=Year_Passing,Score=Score)
        EduDet.save()
        return redirect('resumes:AddExpEducation')
    form=EducationDetailForm()
    return render(request,'resumes/AddExpDetails/AddEducationDetails.html',{'edudetail':edudetail,'form':form})

@login_required(login_url='MyResume/login') 
def ExpAddSkillDetailView(request):
    SkillDetails=Skills.objects.filter(user=request.user).all()
    if request.method=='POST':
        Skill_Name=request.POST['Skill_Name']
        Skill_Percentage=request.POST['Skill_Percentage']
        SkillDet=Skills(user=request.user,Skill_Name=Skill_Name,Skill_Percentage=Skill_Percentage)
        SkillDet.save()
        return redirect('resumes:AddExpSkills')
    form=SkillForm()
    return render(request,'resumes/AddExpDetails/AddSkillDetails.html',{'SkillDetails':SkillDetails,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddSoftSkillDetailView(request):
    SoftSkillDetail=SoftSkills.objects.filter(user=request.user).all()
    if request.method=='POST':
        SoftSkill_Name = request.POST['SoftSkill_Name']
        SoftSkilldet = SoftSkills(user=request.user,SoftSkill_Name=SoftSkill_Name)
        SoftSkilldet.save()
        return redirect('resumes:AddExpSoftSkills')
    form = SoftSkillDetailForm()
    return render(request,'resumes/AddExpDetails/AddSoftSkillDetails.html',{'SoftSkillDetail':SoftSkillDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddHobbieDetailView(request):
    HobDetail=HobbieDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Hobbie = request.POST['Hobbie']
        HobDet = HobbieDetails(user=request.user,Hobbie=Hobbie)
        HobDet.save()
        return redirect('resumes:AddExpHobbies')
    form=HobbieDetailForm()
    return render(request,'resumes/AddExpDetails/AddHobbieDetails.html',{'HobDetail':HobDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddSocialMediaDetailView(request):
    SocialMediaDetail=SocialMediaLinks.objects.filter(user=request.user).all()
    if request.method=='POST':
        SocialMedia_Website_Name=request.POST['SocialMedia_Website_Name']
        SocialMedia_Link=request.POST['SocialMedia_Link']
        SocialMediaDet=SocialMediaLinks(user=request.user,SocialMedia_Website_Name=SocialMedia_Website_Name,SocialMedia_Link=SocialMedia_Link)
        SocialMediaDet.save()
        return redirect('resumes:AddExpSocialMedia')
    form=SocialMediaLinkForm()
    return render(request,'resumes/AddExpDetails/AddSocialMediaDetails.html',{'SocialMediaDetail':SocialMediaDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddLanguageDetailView(request):
    LangDetail=LanguageDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Language_Name = request.POST['Language_Name']
        Language_Confidence = request.POST['Language_Confidence']
        LanguageDet=LanguageDetails(user=request.user,Language_Name=Language_Name,Language_Confidence=Language_Confidence)
        LanguageDet.save()
        return redirect('resumes:AddExpLanguages')
    form=LanguageDetailForm()
    return render(request,'resumes/AddExpDetails/AddLanguageDetails.html',{'LangDetail':LangDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddActivityAchievementDetailView(request):
    ActivityAchievementDetail=AchievementsOrActivities.objects.filter(user=request.user).all()
    if request.method=='POST':
        Achievement_Name = request.POST['Achievement_Name']
        ActAchiev_Choice = request.POST['ActAchiev_Choice']
        Achievement_Description = request.POST['Achievement_Description']
        Achievementdet = AchievementsOrActivities(user=request.user,Achievement_Name=Achievement_Name,ActAchiev_Choice=ActAchiev_Choice,Achievement_Description=Achievement_Description)
        Achievementdet.save()
        return redirect('resumes:AddExpActivityAchievements')
    form = ActivityAchievementDetailForm()
    return render(request,'resumes/AddExpDetails/AddActivityAchievementDetails.html',{'ActivityAchievementDetail':ActivityAchievementDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddInterestDetailView(request):
    Intdet=Interests.objects.filter(user=request.user).all()
    if request.method=='POST':
        Interest_Names = request.POST['Interest_Names']
        InterestDet = Interests(user=request.user,Interest_Names=Interest_Names)
        InterestDet.save()
        return redirect('resumes:AddExpInterests')
    form=InterestDetailForm()
    return render(request, 'resumes/AddExpDetails/AddInterestDetails.html',{'Intdet':Intdet,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddStrengthWeaknessDetailView(request):
    StrengthWeakdet=StrengthWeakness.objects.filter(user=request.user).all()
    if request.method=='POST':
        Strengths = request.POST['Strengths']
        Weakness = request.POST['Weakness']
        StrWeakDet=StrengthWeakness(user=request.user,Strengths=Strengths,Weakness=Weakness) 
        StrWeakDet.save()
        return redirect('resumes:AddExpStrengthWeakness')
    form=StrengthWeaknessForm()
    return render(request,'resumes/AddExpDetails/AddStrengthWeaknessDetails.html',{'StrengthWeakdet':StrengthWeakdet,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddProjectDetailView(request):
    Projectdet=ProjectDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Project_Name = request.POST['Project_Name']
        Project_Url = request.POST['Project_Url']
        Project_Description = request.POST['Project_Description']
        Project_Position = request.POST['Project_Position']
        projdet=ProjectDetails(user=request.user,Project_Name=Project_Name,Project_Url=Project_Url,Project_Description=Project_Description,Project_Position=Project_Position)
        projdet.save()
        return redirect('resumes:AddExpProjects')
    form=ProjectDetailForm()
    return render(request,'resumes/AddExpDetails/AddProjectDetails.html',{'Projectdet':Projectdet,'form':form})

@login_required(login_url='MyResume/login') 
def ExpAddTrainingDetailView(request):
    TrainDetail=TrainingDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Training_Type = request.POST['Training_Type']
        Training_Country = request.POST['Training_Country']
        Training_State = request.POST['Training_State']
        Training_City = request.POST['Training_City']
        Training_ZipCode = request.POST['Training_ZipCode']
        Training_Org_Name = request.POST['Training_Org_Name']
        Training_Course_Name = request.POST['Training_Course_Name']
        Training_startDate = request.POST['Training_startDate']
        Training_EndDate = request.POST['Training_EndDate']
        Training_Description = request.POST['Training_Description']
        TrainDet=TrainingDetails(user=request.user,Training_Type=Training_Type,Training_ZipCode=Training_ZipCode,Training_Country=Training_Country,Training_State=Training_State,Training_City=Training_City,Training_Org_Name=Training_Org_Name,Training_Course_Name=Training_Course_Name,Training_startDate=Training_startDate,Training_EndDate=Training_EndDate,Training_Description=Training_Description)
        TrainDet.save()
        return redirect('resumes:AddExpTrainingDetails')
    form=TrainingDetailForm()
    return render(request, 'resumes/AddExpDetails/AddTrainingDetails.html',{'TrainDetail':TrainDetail,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddCertificationDetailView(request):
    CertifyDet=CertificationDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Certification_Type = request.POST['Certification_Type']
        Certify_Country = request.POST['Certify_Country']
        Certify_State = request.POST['Certify_State']
        Certify_City = request.POST['Certify_City']
        Certify_Org_Name = request.POST['Certify_Org_Name']
        Certify_ZipCode = request.POST['Certify_ZipCode']
        Certify_Course_Name = request.POST['Certify_Course_Name']
        Certify_startDate = request.POST['Certify_startDate']
        Certify_EndDate = request.POST['Certify_EndDate']
        Certify_Description = request.POST['Certify_Description']
        CertDet=CertificationDetails(user=request.user,Certification_Type=Certification_Type,Certify_Country=Certify_Country,Certify_State=Certify_State,Certify_ZipCode=Certify_ZipCode,Certify_City=Certify_City,Certify_Org_Name=Certify_Org_Name,Certify_Course_Name=Certify_Course_Name,Certify_startDate=Certify_startDate,Certify_EndDate=Certify_EndDate,Certify_Description=Certify_Description)
        CertDet.save()
        return redirect('resumes:AddExpCertifications')
    form=CertificationDetailForm()
    return render(request, 'resumes/AddExpDetails/AddCertificationDetails.html',{'CertifyDet':CertifyDet,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddExperienceDetailView(request):
    Expdet=ExperienceDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Experience_choice = request.POST['Experience_choice']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Experience_Job_Name = request.POST['Experience_Job_Name']
        Experience_Job_Type = request.POST['Experience_Job_Type']
        Experience_Start_Date = request.POST['Experience_Start_Date']
        Experience_End_Date = request.POST['Experience_End_Date']
        Experience_Job_Description = request.POST['Experience_Job_Description']
        ExpDet=ExperienceDetails(user=request.user,Experience_choice=Experience_choice,Country=Country,State=State,City=City,ZipCode=ZipCode,Experience_Job_Name=Experience_Job_Name,Experience_Job_Type=Experience_Job_Type,Experience_Start_Date=Experience_Start_Date,Experience_End_Date=Experience_End_Date,Experience_Job_Description=Experience_Job_Description)
        ExpDet.save()
        return redirect('resumes:AddExpExperiences')
    form = ExperienceDetailForm()
    return render(request,'resumes/AddExpDetails/AddExperienceDetails.html',{'Expdet':Expdet,'form':form})

@login_required(login_url='MyResume/login')
def ExpAddInternshipDetailView(request):
    InternDetail=InternshipDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Internship_choice = request.POST['Internship_choice']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Internship_Job_Type = request.POST['Internship_Job_Type']
        Internship_Company_Name = request.POST['Internship_Company_Name']
        Internship_Start_Date = request.POST['Internship_Start_Date']
        Internship_End_Date = request.POST['Internship_End_Date']
        Internship_Job_Description = request.POST['Internship_Job_Description']
        InternDet=InternshipDetails(user=request.user,Internship_choice=Internship_choice,Country=Country,State=State,City=City,Internship_Company_Name=Internship_Company_Name,ZipCode=ZipCode,Internship_Job_Type=Internship_Job_Type,Internship_Start_Date=Internship_Start_Date,Internship_End_Date=Internship_End_Date,Internship_Job_Description=Internship_Job_Description)
        InternDet.save()
        return redirect('resumes:AddExpInternships')
    form=InternshipDetailForm()
    return render(request, 'resumes/AddExpDetails/AddInternshipDetails.html',{'InternDetail':InternDetail,'form':form})

#########################  NO EXPERIENCE RESUME TEMPLATE DETAILS  #########################

# NoExperience Resumes
@login_required(login_url='MyResume/login')
def NoExpContactDetailView(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email_Id = request.POST['Email_Id']
        Mobile_No = request.POST['Mobile_No']
        Alternate_Mobile_No = request.POST['Alternate_Mobile_No']
        Country = request.POST['Country']
        State = request.POST['State']
        City = request.POST['City']
        ZipCode = request.POST['ZipCode']
        Address = request.POST['Address']
        Address_2 = request.POST['Address_2']
        ContEdu = ContactDetails(user=request.user,First_Name=First_Name,Last_Name=Last_Name,Email_Id=Email_Id,Alternate_Mobile_No=Alternate_Mobile_No,Mobile_No=Mobile_No,Country=Country,State=State,Address_2=Address_2,City=City,ZipCode=ZipCode,Address=Address)
        ContEdu.save()
        return redirect('resumes:NoExp-PersonalDetails')
    form=ContactDetailForm()
    return render(request,'resumes/NoExperience-Templates/ContactDetails.html',{'form':form})
    
@login_required(login_url='MyResume/login')
def NoExpPersonalDetailView(request):
    if request.method == "POST":
        Photo = request.FILES['Photo']
        Experience = request.POST['Experience']
        Internship = request.POST['Internship']
        Gender = request.POST['Gender']
        DOB = request.POST['DOB']
        PersonDet=PersonalDetails(user=request.user,Photo=Photo,Experience=Experience,Internship=Internship,Gender=Gender,DOB=DOB)
        PersonDet.save()
        return redirect('resumes:NoExp-SocialMediaDetails')
    form=PersonalDetailForm()
    return render(request,'resumes/NoExperience-Templates/PersonalDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpLanguageDetailView(request):
    if request.method=='POST':
        Language_Name = request.POST['Language_Name']
        Language_Confidence = request.POST['Language_Confidence']
        LanguageDet=LanguageDetails(user=request.user,Language_Name=Language_Name,Language_Confidence=Language_Confidence)
        LanguageDet.save()
        return redirect('resumes:AddNoExpLanguages')
    form=LanguageDetailForm()
    return render(request,'resumes/NoExperience-Templates/Languages.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpSocialMediaLinkView(request):
    if request.method=='POST':
        SocialMedia_Website_Name=request.POST['SocialMedia_Website_Name']
        SocialMedia_Link=request.POST['SocialMedia_Link']
        SocialMediaDet=SocialMediaLinks(user=request.user,SocialMedia_Website_Name=SocialMedia_Website_Name,SocialMedia_Link=SocialMedia_Link)
        SocialMediaDet.save()
        return redirect('resumes:AddNoExpSocialMedia')
    form=SocialMediaLinkForm()
    return render(request,'resumes/NoExperience-Templates/SocialMediaLinks.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpSkillDetailView(request):
    if request.method=='POST':
        Skill_Name=request.POST['Skill_Name']
        Skill_Percentage=request.POST['Skill_Percentage']
        SkillDet=Skills(user=request.user,Skill_Name=Skill_Name,Skill_Percentage=Skill_Percentage)
        SkillDet.save()
        return redirect('resumes:AddNoExpSkills')
    form=SkillForm()
    return render(request,'resumes/NoExperience-Templates/SkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpInterestDetailView(request):
    if request.method=='POST':
        Interest_Names = request.POST['Interest_Names']
        InterestDet = Interests(user=request.user,Interest_Names=Interest_Names)
        InterestDet.save()
        return redirect('resumes:AddNoExpInterests')
    form=InterestDetailForm()
    return render(request,'resumes/NoExperience-Templates/InterestDetails.html',{'form':form}) 

@login_required(login_url='MyResume/login')
def NoExpSoftSkillDetailView(request):
    if request.method=='POST':
        SoftSkill_Name = request.POST['SoftSkill_Name']
        SoftSkilldet = SoftSkills(user=request.user,SoftSkill_Name=SoftSkill_Name)
        SoftSkilldet.save()
        return redirect('resumes:AddNoExpSoftSkills')
    form = SoftSkillDetailForm()
    return render(request,'resumes/NoExperience-Templates/SoftSkillDetails.html',{'form':form}) 

@login_required(login_url='MyResume/login')
def NoExpAchievementsOrActivitiesDetailView(request):
    if request.method=='POST':
        Achievement_Name = request.POST['Achievement_Name']
        ActAchiev_Choice = request.POST['ActAchiev_Choice']
        Achievement_Description = request.POST['Achievement_Description']
        Achievementdet = AchievementsOrActivities(user=request.user,Achievement_Name=Achievement_Name,ActAchiev_Choice=ActAchiev_Choice,Achievement_Description=Achievement_Description)
        Achievementdet.save()
        return redirect('resumes:AddNoExpActivityAchievements')
    form = ActivityAchievementDetailForm()
    return render(request,'resumes/NoExperience-Templates/Achievements.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpStrengthWeaknessDetailView(request):
    if request.method=='POST':
        Strengths = request.POST['Strengths']
        Weakness = request.POST['Weakness']
        StrWeakDet=StrengthWeakness(user=request.user,Strengths=Strengths,Weakness=Weakness) 
        StrWeakDet.save()
        return redirect('resumes:AddNoExpStrengthWeakness')
    form=StrengthWeaknessForm()
    return render(request,'resumes/NoExperience-Templates/StrengthWeaknessDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpHobbieDetailView(request):
    if request.method=='POST':
        Hobbie = request.POST['Hobbie']
        HobDet = HobbieDetails(user=request.user,Hobbie=Hobbie)
        HobDet.save()
        return redirect('resumes:AddNoExpHobbies')
    form=HobbieDetailForm()
    return render(request,'resumes/NoExperience-Templates/HobbieDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpEducationDetailView(request):
    if request.method=='POST':
        Organization_Type = request.POST['Organization_Type']
        Country_Name = request.POST['Country_Name']
        State_Name = request.POST['State_Name']
        City_Name = request.POST['City_Name']
        ZipCode = request.POST['ZipCode']
        Organization_Name = request.POST['Organization_Name']
        Board_Of_Study = request.POST['Board_Of_Study']
        Field_Of_Study = request.POST['Field_Of_Study']
        Standard = request.POST['Standard']
        Year_Passing = request.POST['Year_Passing']
        Score = request.POST['Score']
        EduDet=EducationDetails(user=request.user,Organization_Type=Organization_Type,Country_Name=Country_Name,State_Name=State_Name,City_Name=City_Name,ZipCode=ZipCode,Organization_Name=Organization_Name,Board_Of_Study=Board_Of_Study,Field_Of_Study=Field_Of_Study,Standard=Standard,Year_Passing=Year_Passing,Score=Score)
        EduDet.save()
        return redirect('resumes:AddNoExpEducation')
    form=EducationDetailForm()
    return render(request,'resumes/NoExperience-Templates/EducationDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpProjectDetailView(request):
    if request.method=='POST':
        Project_Name = request.POST['Project_Name']
        Project_Url = request.POST['Project_Url']
        Project_Description = request.POST['Project_Description']
        Project_Position = request.POST['Project_Position']
        projdet=ProjectDetails(user=request.user,Project_Name=Project_Name,Project_Url=Project_Url,Project_Description=Project_Description,Project_Position=Project_Position)
        projdet.save()
        return redirect('resumes:AddNoExpProjects')
    form=ProjectDetailForm()
    return render(request,'resumes/NoExperience-Templates/ProjectDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpTrainingDetailView(request):
    if request.method=='POST':
        Training_Type = request.POST['Training_Type']
        Training_Country = request.POST['Training_Country']
        Training_State = request.POST['Training_State']
        Training_City = request.POST['Training_City']
        Training_ZipCode = request.POST['Training_ZipCode']
        Training_Org_Name = request.POST['Training_Org_Name']
        Training_Course_Name = request.POST['Training_Course_Name']
        Training_startDate = request.POST['Training_startDate']
        Training_EndDate = request.POST['Training_EndDate']
        Training_Description = request.POST['Training_Description']
        TrainDet=TrainingDetails(user=request.user,Training_Type=Training_Type,Training_ZipCode=Training_ZipCode,Training_Country=Training_Country,Training_State=Training_State,Training_City=Training_City,Training_Org_Name=Training_Org_Name,Training_Course_Name=Training_Course_Name,Training_startDate=Training_startDate,Training_EndDate=Training_EndDate,Training_Description=Training_Description)
        TrainDet.save()
        return redirect('resumes:AddNoExpTrainingDetails')
    form=TrainingDetailForm()
    return render(request,'resumes/NoExperience-Templates/TrainingDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpCertificationDetailView(request):
    if request.method=='POST':
        Certification_Type = request.POST['Certification_Type']
        Certify_Country = request.POST['Certify_Country']
        Certify_State = request.POST['Certify_State']
        Certify_City = request.POST['Certify_City']
        Certify_Org_Name = request.POST['Certify_Org_Name']
        Certify_ZipCode = request.POST['Certify_ZipCode']
        Certify_Course_Name = request.POST['Certify_Course_Name']
        Certify_startDate = request.POST['Certify_startDate']
        Certify_EndDate = request.POST['Certify_EndDate']
        Certify_Description = request.POST['Certify_Description']
        CertDet=CertificationDetails(user=request.user,Certification_Type=Certification_Type,Certify_Country=Certify_Country,Certify_State=Certify_State,Certify_ZipCode=Certify_ZipCode,Certify_City=Certify_City,Certify_Org_Name=Certify_Org_Name,Certify_Course_Name=Certify_Course_Name,Certify_startDate=Certify_startDate,Certify_EndDate=Certify_EndDate,Certify_Description=Certify_Description)
        CertDet.save()
        return redirect('resumes:AddNoExpCertifications')
    form=CertificationDetailForm()
    return render(request,'resumes/NoExperience-Templates/CertificationDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def NoExpSummaryDetailView(request):
    if request.method=='POST':
        Summary = request.POST['Summary']
        Your_Position = request.POST['Your_Position']
        SummaryDet=SummaryDetails(user=request.user,Summary=Summary,Your_Position=Your_Position)
        SummaryDet.save()
        return redirect('resumes:NoExp-ShowDetails')
    form=SummaryDetailForm()
    return render(request,'resumes/NoExperience-Templates/SummaryDetails.html',{'form':form})

######################### ADD NO EXPERIENCE RESUME TEMPLATE DETAILS  #########################

# Add NoExperience Views
@login_required(login_url='MyResume/login')
def NoExpAddEducationDetailView(request):
    edudetail = EducationDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Organization_Type = request.POST['Organization_Type']
        Country_Name = request.POST['Country_Name']
        State_Name = request.POST['State_Name']
        City_Name = request.POST['City_Name']
        ZipCode = request.POST['ZipCode']
        Organization_Name = request.POST['Organization_Name']
        Board_Of_Study = request.POST['Board_Of_Study']
        Field_Of_Study = request.POST['Field_Of_Study']
        Standard = request.POST['Standard']
        Year_Passing = request.POST['Year_Passing']
        Score = request.POST['Score']
        EduDet=EducationDetails(user=request.user,Organization_Type=Organization_Type,Country_Name=Country_Name,State_Name=State_Name,City_Name=City_Name,ZipCode=ZipCode,Organization_Name=Organization_Name,Board_Of_Study=Board_Of_Study,Field_Of_Study=Field_Of_Study,Standard=Standard,Year_Passing=Year_Passing,Score=Score)
        EduDet.save()
        return redirect('resumes:AddNoExpEducation')
    form=EducationDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddEducationDetails.html',{'edudetail':edudetail,'form':form})

@login_required(login_url='MyResume/login') 
def NoExpAddSkillDetailView(request):
    SkillDetails=Skills.objects.filter(user=request.user).all()
    if request.method=='POST':
        Skill_Name=request.POST['Skill_Name']
        Skill_Percentage=request.POST['Skill_Percentage']
        SkillDet=Skills(user=request.user,Skill_Name=Skill_Name,Skill_Percentage=Skill_Percentage)
        SkillDet.save()
        return redirect('resumes:AddNoExpSkills')
    form=SkillForm()
    return render(request,'resumes/AddNoExpDetails/AddSkillDetails.html',{'SkillDetails':SkillDetails,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddSoftSkillDetailView(request):
    SoftSkillDetail=SoftSkills.objects.filter(user=request.user).all()
    if request.method=='POST':
        SoftSkill_Name = request.POST['SoftSkill_Name']
        SoftSkilldet = SoftSkills(user=request.user,SoftSkill_Name=SoftSkill_Name)
        SoftSkilldet.save()
        return redirect('resumes:AddNoExpSoftSkills')
    form = SoftSkillDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddSoftSkillDetails.html',{'SoftSkillDetail':SoftSkillDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddHobbieDetailView(request):
    HobDetail=HobbieDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Hobbie = request.POST['Hobbie']
        HobDet = HobbieDetails(user=request.user,Hobbie=Hobbie)
        HobDet.save()
        return redirect('resumes:AddNoExpHobbies')
    form=HobbieDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddHobbieDetails.html',{'HobDetail':HobDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddSocialMediaDetailView(request):
    SocialMediaDetail=SocialMediaLinks.objects.filter(user=request.user).all()
    if request.method=='POST':
        SocialMedia_Website_Name=request.POST['SocialMedia_Website_Name']
        SocialMedia_Link=request.POST['SocialMedia_Link']
        SocialMediaDet=SocialMediaLinks(user=request.user,SocialMedia_Website_Name=SocialMedia_Website_Name,SocialMedia_Link=SocialMedia_Link)
        SocialMediaDet.save()
        return redirect('resumes:AddNoExpSocialMedia')
    form=SocialMediaLinkForm()
    return render(request,'resumes/AddNoExpDetails/AddSocialMediaDetails.html',{'SocialMediaDetail':SocialMediaDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddLanguageDetailView(request):
    LangDetail=LanguageDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Language_Name = request.POST['Language_Name']
        Language_Confidence = request.POST['Language_Confidence']
        LanguageDet=LanguageDetails(user=request.user,Language_Name=Language_Name,Language_Confidence=Language_Confidence)
        LanguageDet.save()
        return redirect('resumes:AddNoExpLanguages')
    form=LanguageDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddLanguageDetails.html',{'LangDetail':LangDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddActivityAchievementDetailView(request):
    ActivityAchievementDetail=AchievementsOrActivities.objects.filter(user=request.user).all()
    if request.method=='POST':
        Achievement_Name = request.POST['Achievement_Name']
        Achievement_Description = request.POST['Achievement_Description']
        ActAchiev_Choice = request.POST['ActAchiev_Choice']
        Achievementdet = AchievementsOrActivities(user=request.user,Achievement_Name=Achievement_Name,ActAchiev_Choice=ActAchiev_Choice,Achievement_Description=Achievement_Description)
        Achievementdet.save()
        return redirect('resumes:AddNoExpActivityAchievements')
    form = ActivityAchievementDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddActivityAchievementDetails.html',{'ActivityAchievementDetail':ActivityAchievementDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddInterestDetailView(request):
    Intdet=Interests.objects.filter(user=request.user).all()
    if request.method=='POST':
        Interest_Names = request.POST['Interest_Names']
        InterestDet = Interests(user=request.user,Interest_Names=Interest_Names)
        InterestDet.save()
        return redirect('resumes:AddNoExpInterests')
    form=InterestDetailForm()
    return render(request, 'resumes/AddNoExpDetails/AddInterestDetails.html',{'Intdet':Intdet,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddStrengthWeaknessDetailView(request):
    StrengthWeakdet=StrengthWeakness.objects.filter(user=request.user).all()
    if request.method=='POST':
        Strengths = request.POST['Strengths']
        Weakness = request.POST['Weakness']
        StrWeakDet=StrengthWeakness(user=request.user,Strengths=Strengths,Weakness=Weakness) 
        StrWeakDet.save()
        return redirect('resumes:AddNoExpStrengthWeakness')
    form=StrengthWeaknessForm()
    return render(request,'resumes/AddNoExpDetails/AddStrengthWeaknessDetails.html',{'StrengthWeakdet':StrengthWeakdet,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddProjectDetailView(request):
    Projectdet=ProjectDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Project_Name = request.POST['Project_Name']
        Project_Url = request.POST['Project_Url']
        Project_Description = request.POST['Project_Description']
        Project_Position = request.POST['Project_Position']
        projdet=ProjectDetails(user=request.user,Project_Name=Project_Name,Project_Url=Project_Url,Project_Description=Project_Description,Project_Position=Project_Position)
        projdet.save()
        return redirect('resumes:AddNoExpProjects')
    form=ProjectDetailForm()
    return render(request,'resumes/AddNoExpDetails/AddProjectDetails.html',{'Projectdet':Projectdet,'form':form})

@login_required(login_url='MyResume/login') 
def NoExpAddTrainingDetailView(request):
    TrainDetail=TrainingDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Training_Type = request.POST['Training_Type']
        Training_Country = request.POST['Training_Country']
        Training_State = request.POST['Training_State']
        Training_City = request.POST['Training_City']
        Training_ZipCode = request.POST['Training_ZipCode']
        Training_Org_Name = request.POST['Training_Org_Name']
        Training_Course_Name = request.POST['Training_Course_Name']
        Training_startDate = request.POST['Training_startDate']
        Training_EndDate = request.POST['Training_EndDate']
        Training_Description = request.POST['Training_Description']
        TrainDet=TrainingDetails(user=request.user,Training_Type=Training_Type,Training_ZipCode=Training_ZipCode,Training_Country=Training_Country,Training_State=Training_State,Training_City=Training_City,Training_Org_Name=Training_Org_Name,Training_Course_Name=Training_Course_Name,Training_startDate=Training_startDate,Training_EndDate=Training_EndDate,Training_Description=Training_Description)
        TrainDet.save()
        return redirect('resumes:AddNoExpTrainingDetails')
    form=TrainingDetailForm()
    return render(request, 'resumes/AddNoExpDetails/AddTrainingDetails.html',{'TrainDetail':TrainDetail,'form':form})

@login_required(login_url='MyResume/login')
def NoExpAddCertificationDetailView(request):
    CertifyDet=CertificationDetails.objects.filter(user=request.user).all()
    if request.method=='POST':
        Certification_Type = request.POST['Certification_Type']
        Certify_Country = request.POST['Certify_Country']
        Certify_State = request.POST['Certify_State']
        Certify_City = request.POST['Certify_City']
        Certify_Org_Name = request.POST['Certify_Org_Name']
        Certify_ZipCode = request.POST['Certify_ZipCode']
        Certify_Course_Name = request.POST['Certify_Course_Name']
        Certify_startDate = request.POST['Certify_startDate']
        Certify_EndDate = request.POST['Certify_EndDate']
        Certify_Description = request.POST['Certify_Description']
        CertDet=CertificationDetails(user=request.user,Certification_Type=Certification_Type,Certify_Country=Certify_Country,Certify_State=Certify_State,Certify_ZipCode=Certify_ZipCode,Certify_City=Certify_City,Certify_Org_Name=Certify_Org_Name,Certify_Course_Name=Certify_Course_Name,Certify_startDate=Certify_startDate,Certify_EndDate=Certify_EndDate,Certify_Description=Certify_Description)
        CertDet.save()
        return redirect('resumes:AddNoExpCertifications')
    form=CertificationDetailForm()
    return render(request, 'resumes/AddNoExpDetails/AddCertificationDetails.html',{'CertifyDet':CertifyDet,'form':form})

#########################  EDIT EXPERIENCE DETAILS VIEW  #########################

# Get Details or Update
@login_required(login_url='MyResume/login')
def EditExpContactDetailView(request,c_id):
    cdet = ContactDetails.objects.get(user=request.user, id=c_id)
    if request.method == 'POST':
        form = ContactDetailForm(request.POST, instance=cdet)
        if form.is_valid():
            form.save()
            #return redirect('resumes:Home')
    form = ContactDetailForm(instance=cdet)
    return render(request, 'resumes/ExpEditDetails/EditContactDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpPersonalDetailView(request,p_id):
    pdet = PersonalDetails.objects.get(user=request.user,id=p_id)
    if request.method=='POST':
        form = PersonalDetailForm(request.POST, instance=pdet)
        if form.is_valid():
            form.save()
    form=PersonalDetailForm(instance=pdet)
    return render(request,'resumes/ExpEditDetails/EditPersonalDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpEducationDetailView(request,e_id):
    edet = EducationDetails.objects.get(user=request.user,id=e_id)
    if request.method=='POST':
        form = EducationDetailForm(request.POST, instance=edet)
        if form.is_valid():
            form.save()
    form = EducationDetailForm(instance=edet)
    context={'form':form}
    return render(request,'resumes/ExpEditDetails/EditEducationDetails.html',context)

@login_required(login_url='MyResume/login')
def EditExpLanguageDetailView(request,l_id):
    ldet = LanguageDetails.objects.get(user=request.user,id=l_id)
    if request.method=='POST':
        form = LanguageDetailForm(request.POST, instance=ldet)
        if form.is_valid():
            form.save()
    form = LanguageDetailForm(instance=ldet)
    return render(request, 'resumes/ExpEditDetails/EditLanguageDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpSocialMediaDetailView(request,sm_id):
    smdet = SocialMediaLinks.objects.get(user=request.user,id=sm_id)
    if request.method=='POST':
        form = SocialMediaLinkForm(request.POST, instance=smdet)
        if form.is_valid():
            form.save()
    form = SocialMediaLinkForm(instance=smdet)
    return render(request, 'resumes/ExpEditDetails/EditSocialMediaDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpActivityAchievementDetailView(request,aa_id):
    aadet = AchievementsOrActivities.objects.get(user=request.user,id=aa_id)
    if request.method=='POST':
        form = ActivityAchievementDetailForm(request.POST, instance=aadet)
        if form.is_valid():
            form.save()
    form = ActivityAchievementDetailForm(instance=aadet)
    return render(request,'resumes/ExpEditDetails/EditActivityAchievementDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpSkillDetailView(request,sk_id):
    skdet=Skills.objects.get(user=request.user,id=sk_id)
    if request.method=='POST':
        form = SkillForm(request.POST, instance=skdet)
        if form.is_valid():
            form.save()
    form=SkillForm(instance=skdet)
    return render(request, 'resumes/ExpEditDetails/EditSkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpInterestDetailView(request,i_id):
    indet=Interests.objects.get(user=request.user,id=i_id)
    if request.method=='POST':
        form = InterestDetailForm(request.POST, instance=indet)
        if form.is_valid():
            form.save()
    form = InterestDetailForm(instance=indet)
    return render(request, 'resumes/ExpEditDetails/EditInterestDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpSoftSkillDetailView(request,ss_id):
    ssdet=SoftSkills.objects.get(user=request.user,id=ss_id)
    if request.method=='POST':
        form = SoftSkillDetailForm(request.POST, instance=ssdet)
        if form.is_valid():
            form.save()
    form = SoftSkillDetailForm(instance=ssdet)
    return render(request, 'resumes/ExpEditDetails/EditSoftSkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpStrengthWeaknessDetailView(request,sw_id):
    swdet = StrengthWeakness.objects.get(user=request.user,id=sw_id)
    if request.method=='POST':
        form= StrengthWeaknessForm(request.POST, instance=swdet)
        if form.is_valid():
            form.save()
    form = StrengthWeaknessForm(instance=swdet)
    return render(request, 'resumes/ExpEditDetails/EditStrengthWeaknessDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpHobbieDetailView(request,h_id):
    hdet = HobbieDetails.objects.get(user=request.user,id=h_id)
    if request.method=='POST':
        form = HobbieDetailForm(request.POST, instance=hdet)
        if form.is_valid():
            form.save()
    form = HobbieDetailForm(instance=hdet)
    return render(request,'resumes/ExpEditDetails/EditHobbieDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpProjectDetailView(request,p_id):
    pdet=ProjectDetails.objects.get(user=request.user,id=p_id)
    if request.method=='POST':
        form = ProjectDetailForm(request.POST, instance=pdet)
        if form.is_valid():
            form.save()
    form = ProjectDetailForm(instance=pdet)
    return render(request, 'resumes/ExpEditDetails/EditProjectDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpSummaryDetailView(request,s_id):
    sdet = SummaryDetails.objects.get(user=request.user,id=s_id)
    if request.method=='POST':
        form = SummaryDetailForm(request.POST, instance=sdet)
        if form.is_valid():
            form.save()
    form = SummaryDetailForm(instance=sdet)
    return render(request, 'resumes/ExpEditDetails/EditSummaryDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpTrainingDetailView(request,t_id):
    tdet = TrainingDetails.objects.get(user=request.user,id=t_id)
    if request.method=='POST':
        form = TrainingDetailForm(request.POST, instance=tdet)
        if form.is_valid():
            form.save()
    form = TrainingDetailForm(instance=tdet)
    return render(request, 'resumes/ExpEditDetails/EditTrainingDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpCertificationDetailView(request,c_id):
    cdet = CertificationDetails.objects.get(user=request.user,id=c_id)
    if request.method=='POST':
        form = CertificationDetailForm(request.POST, instance=cdet)
        if form.is_valid():
            form.save()
    form = CertificationDetailForm(instance=cdet)
    return render(request, 'resumes/ExpEditDetails/EditCertificationdetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpInternshipDetailView(request, in_id):
    intdet= InternshipDetails.objects.get(user=request.user,id=in_id)
    if request.method=='POST':
        form = InternshipDetailForm(request.POST, instance=intdet)
        if form.is_valid():
            form.save()
    form = InternshipDetailForm(instance=intdet)
    return render(request, 'resumes/ExpEditDetails/EditInternshipDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditExpExperienceDetailView(request,exp_id):
    expdet = ExperienceDetails.objects.get(user=request.user, id=exp_id)
    if request.method=='POST':
        form=ExperienceDetailForm(request.POST, instance=expdet)
        if form.is_valid():
            form.save()
    form = ExperienceDetailForm(instance=expdet)
    return render(request, 'resumes/ExpEditdetails/EditExperienceDetails.html',{'form':form})

#########################  EDIT NO EXPERIENCE DETAILS VIEW  #########################

# Get Details or Update
@login_required(login_url='MyResume/login')
def EditNoExpContactDetailView(request,c_id):
    cdet = ContactDetails.objects.get(user=request.user, id=c_id)
    if request.method == 'POST':
        form = ContactDetailForm(request.POST, instance=cdet)
        if form.is_valid():
            form.save()
            #return redirect('resumes:Home')
    form = ContactDetailForm(instance=cdet)
    return render(request, 'resumes/NoExpEditDetails/EditContactDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpPersonalDetailView(request,p_id):
    pdet = PersonalDetails.objects.get(user=request.user,id=p_id)
    if request.method=='POST':
        form = PersonalDetailForm(request.POST, instance=pdet)
        if form.is_valid():
            form.save()
    form=PersonalDetailForm(instance=pdet)
    return render(request,'resumes/NoExpEditDetails/EditPersonalDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpEducationDetailView(request,e_id):
    edet = EducationDetails.objects.get(user=request.user,id=e_id)
    if request.method=='POST':
        form = EducationDetailForm(request.POST, instance=edet)
        if form.is_valid():
            form.save()
    form = EducationDetailForm(instance=edet)
    context={'form':form}
    return render(request,'resumes/NoExpEditDetails/EditEducationDetails.html',context)

@login_required(login_url='MyResume/login')
def EditNoExpLanguageDetailView(request,l_id):
    ldet = LanguageDetails.objects.get(user=request.user,id=l_id)
    if request.method=='POST':
        form = LanguageDetailForm(request.POST, instance=ldet)
        if form.is_valid():
            form.save()
    form = LanguageDetailForm(instance=ldet)
    return render(request, 'resumes/NoExpEditDetails/EditLanguageDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpSocialMediaDetailView(request,sm_id):
    smdet = SocialMediaLinks.objects.get(user=request.user,id=sm_id)
    if request.method=='POST':
        form = SocialMediaLinkForm(request.POST, instance=smdet)
        if form.is_valid():
            form.save()
    form = SocialMediaLinkForm(instance=smdet)
    return render(request, 'resumes/NoExpEditDetails/EditSocialMediaDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpActivityAchievementDetailView(request,aa_id):
    aadet = AchievementsOrActivities.objects.get(user=request.user,id=aa_id)
    if request.method=='POST':
        form = ActivityAchievementDetailForm(request.POST, instance=aadet)
        if form.is_valid():
            form.save()
    form = ActivityAchievementDetailForm(instance=aadet)
    return render(request,'resumes/NoExpEditDetails/EditActivityAchievementDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpSkillDetailView(request,sk_id):
    skdet=Skills.objects.get(user=request.user,id=sk_id)
    if request.method=='POST':
        form = SkillForm(request.POST, instance=skdet)
        if form.is_valid():
            form.save()
    form=SkillForm(instance=skdet)
    return render(request, 'resumes/NoExpEditDetails/EditSkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpInterestDetailView(request,i_id):
    indet=Interests.objects.get(user=request.user,id=i_id)
    if request.method=='POST':
        form = InterestDetailForm(request.POST, instance=indet)
        if form.is_valid():
            form.save()
    form = InterestDetailForm(instance=indet)
    return render(request, 'resumes/NoExpEditDetails/EditInterestDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpSoftSkillDetailView(request,ss_id):
    ssdet=SoftSkills.objects.get(user=request.user,id=ss_id)
    if request.method=='POST':
        form = SoftSkillDetailForm(request.POST, instance=ssdet)
        if form.is_valid():
            form.save()
    form = SoftSkillDetailForm(instance=ssdet)
    return render(request, 'resumes/NoExpEditDetails/EditSoftSkillDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpStrengthWeaknessDetailView(request,sw_id):
    swdet = StrengthWeakness.objects.get(user=request.user,id=sw_id)
    if request.method=='POST':
        form= StrengthWeaknessForm(request.POST, instance=swdet)
        if form.is_valid():
            form.save()
    form = StrengthWeaknessForm(instance=swdet)
    return render(request, 'resumes/NoExpEditDetails/EditStrengthWeaknessDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpHobbieDetailView(request,h_id):
    hdet = HobbieDetails.objects.get(user=request.user,id=h_id)
    if request.method=='POST':
        form = HobbieDetailForm(request.POST, instance=hdet)
        if form.is_valid():
            form.save()
    form = HobbieDetailForm(instance=hdet)
    return render(request,'resumes/NoExpEditDetails/EditHobbieDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpProjectDetailView(request,p_id):
    pdet=ProjectDetails.objects.get(user=request.user,id=p_id)
    if request.method=='POST':
        form = ProjectDetailForm(request.POST, instance=pdet)
        if form.is_valid():
            form.save()
    form = ProjectDetailForm(instance=pdet)
    return render(request, 'resumes/NoExpEditDetails/EditProjectDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpSummaryDetailView(request,s_id):
    sdet = SummaryDetails.objects.get(user=request.user,id=s_id)
    if request.method=='POST':
        form = SummaryDetailForm(request.POST, instance=sdet)
        if form.is_valid():
            form.save()
    form = SummaryDetailForm(instance=sdet)
    return render(request, 'resumes/NoExpEditDetails/EditSummaryDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpTrainingDetailView(request,t_id):
    tdet = TrainingDetails.objects.get(user=request.user,id=t_id)
    if request.method=='POST':
        form = TrainingDetailForm(request.POST, instance=tdet)
        if form.is_valid():
            form.save()
    form = TrainingDetailForm(instance=tdet)
    return render(request, 'resumes/NoExpEditDetails/EditTrainingDetails.html',{'form':form})

@login_required(login_url='MyResume/login')
def EditNoExpCertificationDetailView(request,c_id):
    cdet = CertificationDetails.objects.get(user=request.user,id=c_id)
    if request.method=='POST':
        form = CertificationDetailForm(request.POST, instance=cdet)
        if form.is_valid():
            form.save()
    form = CertificationDetailForm(instance=cdet)
    return render(request, 'resumes/NoExpEditDetails/EditCertificationdetails.html',{'form':form})

########################## DELETE EXP DETAILS #########################
@login_required(login_url='MyResume/login')
def ExpDeleteContactDetailView(request,c_id):
    ContactDetails.objects.filter(id=c_id).delete()
    return redirect('resumes:Exp-ContactDetails')

@login_required(login_url='MyResume/login')
def ExpDeletePersonalDetailView(request,p_id):
    PersonalDetails.objects.filter(id=p_id).delete()
    return redirect('resumes:Exp-PersonalDetails')

@login_required(login_url='MyResume/login')
def ExpDeleteLanguageDetailView(request,l_id):
    LanguageDetails.objects.filter(id=l_id).delete()
    return redirect('resumes:AddExpLanguages')

@login_required(login_url='MyResume/login')
def ExpDeleteSocialMediaDetailView(request, sm_id):
    SocialMediaLinks.objects.filter(id=sm_id).delete()
    return redirect('resumes:AddExpSocialMedia')

@login_required(login_url='MyResume/login')
def ExpDeleteActivityAchievementDetailView(request, aa_id):
    AchievementsOrActivities.objects.filter(id=aa_id).delete()
    return redirect('resumes:AddExpActivityAchievements')

@login_required(login_url='MyResume/login')
def ExpDeleteSkillDetailView(request, sd_id):
    Skills.objects.filter(id=sd_id).delete()
    return redirect('resumes:AddExpSkills')

@login_required(login_url='MyResume/login')
def ExpDeleteInterestDetailView(request,i_id):
    Interests.objects.filter(id=i_id).delete()
    return redirect('resumes:AddExpInterests')

@login_required(login_url='MyResume/login')
def ExpDeleteSoftSkillDetailView(request, ss_id):
    SoftSkills.objects.filter(id=ss_id).delete()
    return redirect('resumes:AddExpSoftSkills')

@login_required(login_url='MyResume/login')
def ExpDeleteStrengthWeaknessDetailView(request,sw_id):
    StrengthWeakness.objects.filter(id=sw_id).delete()
    return redirect('resumes:AddExpStrengthWeakness')

@login_required(login_url='MyResume/login')
def ExpDeleteEducationDetailView(request,e_id):
    EducationDetails.objects.filter(id=e_id).delete()
    return redirect('resumes:AddExpEducation')

@login_required(login_url='MyResume/login')
def ExpDeleteHobbieDetailView(request,h_id):
    HobbieDetails.objects.filter(id=h_id).delete()
    return redirect('resumes:AddExpHobbies')

@login_required(login_url='MyResume/login')
def ExpDeleteProjectDetailView(request, p_id):
    ProjectDetails.objects.filter(id=p_id).delete()
    return redirect('resumes:AddExpProjects')

@login_required(login_url='MyResume/login')
def ExpDeleteTrainingDetailView(request,t_id):
    TrainingDetails.objects.filter(id=t_id).delete()
    return redirect('resumes:AddExpTrainingDetails')

@login_required(login_url='MyResume/login')
def ExpDeleteCertificationDetailView(request,c_id):
    CertificationDetails.objects.filter(id=c_id).delete()
    return redirect('resumes:AddExpCertifications')

@login_required(login_url='MyResume/login')
def ExpDeleteInternshipDetailView(request,in_id):
    InternshipDetails.objects.filter(id=in_id).delete()
    return redirect('resumes:AddExpInternships')

@login_required(login_url='MyResume/login')
def ExpDeleteExperienceDetailView(request, e_id):
    ExperienceDetails.objects.filter(id=e_id).delete()
    return redirect('resumes:AddExpExperiences')

@login_required(login_url='MyResume/login')
def ExpDeleteSummaryDetailView(request,s_id):
    SummaryDetails.objects.filter(id=s_id).delete()
    return redirect('resumes:Exp-SummaryDetails')

########################## DELETE NOEXP DETAILS #########################

@login_required(login_url='MyResume/login')
def NoExpDeleteContactDetailView(request,c_id):
    ContactDetails.objects.filter(id=c_id).delete()
    return redirect('resumes:NoExp-ContactDetails')

@login_required(login_url='MyResume/login')
def NoExpDeletePersonalDetailView(request,p_id):
    PersonalDetails.objects.filter(id=p_id).delete()
    return redirect('resumes:NoExp-PersonalDetails')

@login_required(login_url='MyResume/login')
def NoExpDeleteLanguageDetailView(request,l_id):
    LanguageDetails.objects.filter(id=l_id).delete()
    return redirect('resumes:AddNoExpLanguages')

@login_required(login_url='MyResume/login')
def NoExpDeleteSocialMediaDetailView(request, sm_id):
    SocialMediaLinks.objects.filter(id=sm_id).delete()
    return redirect('resumes:AddNoExpSocialMedia')

@login_required(login_url='MyResume/login')
def NoExpDeleteActivityAchievementDetailView(request, aa_id):
    AchievementsOrActivities.objects.filter(id=aa_id).delete()
    return redirect('resumes:AddNoExpActivityAchievements')

@login_required(login_url='MyResume/login')
def NoExpDeleteSkillDetailView(request, sd_id):
    Skills.objects.filter(id=sd_id).delete()
    return redirect('resumes:AddNoExpSkills')

@login_required(login_url='MyResume/login')
def NoExpDeleteInterestDetailView(request,i_id):
    Interests.objects.filter(id=i_id).delete()
    return redirect('resumes:AddNoExpInterests')

@login_required(login_url='MyResume/login')
def NoExpDeleteSoftSkillDetailView(request, ss_id):
    SoftSkills.objects.filter(id=ss_id).delete()
    return redirect('resumes:AddNoExpSoftSkills')

@login_required(login_url='MyResume/login')
def NoExpDeleteStrengthWeaknessDetailView(request,sw_id):
    StrengthWeakness.objects.filter(id=sw_id).delete()
    return redirect('resumes:AddNoExpStrengthWeakness')

@login_required(login_url='MyResume/login')
def NoExpDeleteEducationDetailView(request,e_id):
    EducationDetails.objects.filter(id=e_id).delete()
    return redirect('resumes:AddNoExpEducation')

@login_required(login_url='MyResume/login')
def NoExpDeleteHobbieDetailView(request,h_id):
    HobbieDetails.objects.filter(id=h_id).delete()
    return redirect('resumes:AddNoExpHobbies')

@login_required(login_url='MyResume/login')
def NoExpDeleteProjectDetailView(request, p_id):
    ProjectDetails.objects.filter(id=p_id).delete()
    return redirect('resumes:AddNoExpProjects')

@login_required(login_url='MyResume/login')
def NoExpDeleteTrainingDetailView(request,t_id):
    TrainingDetails.objects.filter(id=t_id).delete()
    return redirect('resumes:AddNoExpTrainingDetails')

@login_required(login_url='MyResume/login')
def NoExpDeleteCertificationDetailView(request,c_id):
    CertificationDetails.objects.filter(id=c_id).delete()
    return redirect('resumes:AddNoExpCertifications')

@login_required(login_url='MyResume/login')
def NoExpDeleteSummaryDetailView(request,s_id):
    SummaryDetails.objects.filter(id=s_id).delete()
    return redirect('resumes:NoExp-SummaryDetails')

