from django.db import models

# Create your models here.
class User(models.Model):
    F = "Female"
    M = "Male"
    O = "Other"
    Admin = "Admin"
    Student = "Student"
    Teacher = "Teacher"
    Finance = "Finance" 

    GENDER_CHOICES = [(F, "Female"), (M, "Male"), (O, "Other")]
    ROLE_CHOICES = [(Admin, "Admin"), (Student, "Student"), (Teacher, "Teacher"), (Finance, "Finance")]
    full_name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=O)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=Student)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=20, unique=True)
    intake = models.CharField(max_length=20)
    faculty = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    

    def __str__(self):
        return f"{self.user.full_name} - {self.reg_number}"    