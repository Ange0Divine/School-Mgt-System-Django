from django.db import models

# Create your models here.
Present = 'Present'
Absent = 'Absent'   
Late = 'Late'
Excused = 'Excused'
ATTENDANCE_STATUS_CHOICES = [
    (Present, 'Present'),
    (Absent, 'Absent'),
    (Late, 'Late'),
    (Excused, 'Excused')
]

class Grades(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.user.full_name} - {self.subject.name}: {self.grade}"

class Attendance(models.Model):
    student = models.ForeignKey('academics.StudentSubject', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS_CHOICES, default=Present)
    def __str__(self):
        return f"{self.student.user.full_name} - {self.student.Subject.name} {self.date}: {self.status}"