from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    credits = models.IntegerField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.code})"  
    

    
class SubjectTeacher(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.subject.name} - {self.teacher.full_name}"  


class StudentSubject(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.full_name} - {self.subject.name}"      
    



