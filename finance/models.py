from django.db import models

# Create your models here.
class Fee_Payment(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_payment = models.DateField()
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Overdue', 'Overdue')], default='Pending')

    def __str__(self):
        return f"{self.student.user.full_name} - {self.amount} on {self.date}"
