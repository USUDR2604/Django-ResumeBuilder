from django.db import models
from django.contrib.auth.models import User
from .Choices import *
 
# Create your models here.
class ContactDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100,help_text='Enter your First Name')
    Last_Name = models.CharField(max_length=100,help_text='Enter your Last Name')
    Email_Id = models.EmailField(max_length=100,help_text='Enter your Email Id')
    Mobile_No = models.CharField(max_length=10, help_text='Enter Your Mobile No')
    Alternate_Mobile_No=models.CharField(max_length=10, help_text='Enter Your Alternate Mobile No')
    Address = models.CharField(max_length=800, help_text='Enter your Address')
    Address_2 = models.CharField(max_length=800, help_text='Enter your Second Address')
    City = models.CharField(max_length=80, help_text='Enter your City Name')
    State = models.CharField(max_length=100, help_text='Enter State Name')
    ZipCode = models.CharField(max_length=6, help_text='Enter your ZipCode')
    Country = models.CharField(max_length=50, help_text='Enter Country Name')
    def __str__(self):
        return str(self.user)

class PersonalDetails(models.Model):
    EXP_INTERN_CHOICES=(('YES',"YES"),("NO","NO"))
    GENDER_CHOICES=(("MALE","MALE"),("FEMALE","FEMALE"),("OTHERS","OTHERS"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Photo = models.ImageField(default='default.jpg',upload_to='Photos/')
    Experience = models.CharField(max_length=100, choices=EXP_INTERN_CHOICES)
    Internship = models.CharField(max_length=100,choices=EXP_INTERN_CHOICES)
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    DOB = models.DateField(help_text='Date Of Birth Details')
    def __str__(self):
        return str(self.user)

class LanguageDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Language_Name = models.CharField(max_length=100,help_text="Language Name")
    Language_Confidence = models.PositiveIntegerField()
    def __str__(self):
        return str(self.user)

class SocialMediaLinks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SocialMedia_Website_Name = models.CharField(max_length=100,help_text='Enter Social Media Website Name')
    SocialMedia_Link = models.URLField(max_length=700,help_text='Enter Social Media Web Link')
    def __str__(self):
        return str(self.user)

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Skill_Name=models.CharField(max_length=300, help_text='Enter your Skill',unique=True)
    Skill_Percentage=models.PositiveIntegerField()
    def __str__(self):
        return str(self.user)

class Interests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Interest_Names = models.CharField(max_length=200,help_text='Enter your Interests')
    def __str__(self):
        return str(self.user)

class SoftSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SoftSkill_Name = models.CharField(max_length=200,help_text='Enter Soft Skill')
    def __str__(self):
        return str(self.user)

class AchievementsOrActivities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ActAchiev_Choice = models.CharField(max_length=200,choices=ACTIVITY_ACHIEVEMENTS,help_text='Choose Either Activity or Achievement')
    Achievement_Name = models.CharField(max_length=200,help_text='Enter Achievement Name')
    Achievement_Description = models.CharField(max_length=800,help_text='Enter Achievement Description')
    def __str__(self):
        return str(self.user)

class EducationDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Organization_Type = models.CharField(max_length=100,choices=EDUCATION_CHOICES,help_text='Organization Type')
    Country_Name=models.CharField(max_length=300,help_text='Country Name')
    State_Name=models.CharField(max_length=300, help_text='Enter State Name')
    City_Name=models.CharField(max_length=150,help_text='City Name')
    ZipCode=models.CharField(max_length=6,help_text='ZipCode')
    Organization_Name=models.CharField(max_length=400, help_text='Organization Name')
    Board_Of_Study=models.CharField(max_length=400,blank=True,help_text='Board Of Study')
    Field_Of_Study=models.CharField(max_length=400, help_text='Enter your Field Study')
    Standard=models.CharField(max_length=120,help_text='Your Standard')
    Year_Passing=models.DateField(help_text='Year Passing')
    Score=models.DecimalField(max_digits = 5,decimal_places = 2)
    def __str__(self):
        return str(self.user)

class ProjectDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Project_Name=models.CharField(max_length=300,help_text='Enter Project Name')
    Project_Url=models.URLField(max_length=400,help_text='Enter project Url')
    Project_Description=models.TextField(max_length=800,help_text='Enter Project Description')
    Project_Position=models.CharField(max_length=500,help_text='Enter your Position')
    def __str__(self):
        return str(self.user)

class TrainingDetails(models.Model):
    TRAINING_CHOICES=(('ONLINE','ONLINE'),('OFFLINE',"OFFLINE"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Training_Type=models.CharField(max_length=100,choices=TRAINING_CHOICES,help_text='Enter Training Type')
    Training_Country=models.CharField(max_length=300,help_text='Enter your Training Country',blank=True)
    Training_State=models.CharField(max_length=200,help_text='Enter Training State',blank=True)
    Training_City=models.CharField(max_length=100,help_text='Enter your Training City',blank=True)
    Training_ZipCode=models.CharField(max_length=6,help_text='Enter Training Place ZipCode')
    Training_Org_Name=models.CharField(max_length=500,help_text='Enter Training organization Name')
    Training_Course_Name=models.CharField(max_length=200,help_text='Enter Training Course')
    Training_startDate=models.DateField(help_text='Training Start Date')
    Training_EndDate=models.DateField(help_text='Training End Date')
    Training_Description=models.TextField(help_text='Enter Training Description')
    def __str__(self):
        return str(self.user)

class ExperienceDetails(models.Model):
    EXPERIENCE_CHOICES=(('WORK FROM HOME','WORK FROM HOME'),('PART TIME','PART TIME'),('FULL TIME','FULL TIME'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Experience_choice=models.CharField(max_length=200,choices=EXPERIENCE_CHOICES,blank=True)
    Country=models.CharField(max_length=150,help_text='Country Name',blank=True)
    State=models.CharField(max_length=300,help_text='State Name',blank=True)
    City=models.CharField(max_length=300,help_text='Enter City Name',blank=True)
    ZipCode=models.CharField(max_length=6,help_text='Enter ZipCode',blank=True)
    Experience_Type=models.CharField(max_length=25,help_text='Enter Experience Type',default='Experience',editable=False)
    Experience_Job_Name = models.CharField(max_length=300,help_text='Enter Company Name')
    Experience_Job_Type=models.CharField(max_length=300,help_text='Experience Job Type',blank=True)
    Experience_Start_Date=models.DateField(help_text='Enter Start Date',blank=True)
    Experience_End_Date=models.DateField(help_text='Enter End Date',blank=True)
    Experience_Job_Description=models.TextField(max_length=800,help_text='Enter Experience Description',blank=True)

    def __str__(self):
        return str(self.user)

class InternshipDetails(models.Model):
    INTERNSHIP_CHOICES=(("OFFLINE",'OFFLINE'),('PART TIME',"PART TIME"),("ONLINE","ONLINE"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Internship_choice=models.CharField(max_length=200,choices=INTERNSHIP_CHOICES,blank=True)
    Country=models.CharField(max_length=150,help_text='Country Name',blank=True)
    State=models.CharField(max_length=300,help_text='State Name',blank=True)
    City=models.CharField(max_length=300,help_text='Enter City Name',blank=True)
    ZipCode=models.CharField(max_length=6,help_text='Enter ZipCode',blank=True)
    Internship_Type=models.CharField(max_length=25,help_text='Enter Internship Type',default='Internship',editable=False)
    Internship_Company_Name=models.CharField(max_length=300,help_text="Enter Company Name")
    Internship_Job_Type=models.CharField(max_length=300,help_text='Experience Job Type',blank=True)
    Internship_Start_Date=models.DateField(help_text='Enter Start Date',blank=True)
    Internship_End_Date=models.DateField(help_text='Enter End Date',blank=True)
    Internship_Job_Description=models.TextField(max_length=800,help_text='Enter Experience Description',blank=True)
    def __str__(self):
        return str(self.user)

class CertificationDetails(models.Model):
    TRAINING_CHOICES=(('ONLINE','ONLINE'),('OFFLINE',"OFFLINE"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Certification_Type=models.CharField(max_length=100,choices=TRAINING_CHOICES,help_text='Enter Training Type')
    Certify_Country=models.CharField(max_length=300,help_text='Enter your Training Country',blank=True)
    Certify_State=models.CharField(max_length=200,help_text='Enter Training State',blank=True)
    Certify_City=models.CharField(max_length=100,help_text='Enter your Training City',blank=True)
    Certify_ZipCode=models.CharField(max_length=100,help_text='Enter ZipCode',blank=True)
    Certify_Org_Name=models.CharField(max_length=500,help_text='Enter Training organization Name')
    Certify_Course_Name=models.CharField(max_length=200,help_text='Enter Training Course')
    Certify_startDate=models.DateField(help_text='Training Start Date')
    Certify_EndDate=models.DateField(help_text='Training End Date')
    Certify_Description=models.TextField(help_text='Enter Training Description')
    def __str__(self):
        return str(self.user)

class StrengthWeakness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Strengths=models.TextField(max_length=600,help_text='Enter your Strengths')
    Weakness=models.TextField(max_length=600,help_text='Enter your Weakness')
    def __str__(self):
        return str(self.user)
 
class HobbieDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Hobbie=models.CharField(max_length=120,help_text='Enter your Hobbie')
    def __str__(self):
        return str(self.user)
    
class SummaryDetails(models.Model):
    aboutme = '''Enthusiastic Creater and Developer with innovative ideas and Well Trained and Certified Student.
     Always Interested in Implementing Creative Ideas.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Your_Position = models.CharField(max_length=200,help_text='enter your position')
    About = models.CharField(max_length=350,help_text='About')
    Summary = models.TextField(max_length=800,help_text='Your Information')
    def __str__(self):
        return str(self.user)


