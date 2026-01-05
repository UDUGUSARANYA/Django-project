from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Application(models.Model):
#     STATUS_CHOICES = [
#         ('Applied', 'Applied'),
#         ('Shortlisted', 'Shortlisted'),
#         ('Rejected', 'Rejected'),
#     ]

#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     applicant = models.ForeignKey(User, on_delete=models.CASCADE)
#     resume = models.FileField(upload_to='resumes/')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
#     applied_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.applicant.username
class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
