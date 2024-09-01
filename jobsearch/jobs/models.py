from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    experience_needed = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    last_date = models.DateField()
    company = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Link to the User model

    def __str__(self):
        return self.title

    @property
    def company_id(self):
        return self.company.id  # Returns the ID of the user (company)

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)  # Candidate represented by User
    applied_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(blank=True, null=True, upload_to='applicants')
    cover = models.TextField(max_length=2048, null=True, blank=True)

    @property
    def candidate_name(self):
        # This dynamically returns the candidate's username
        return self.candidate.username

    def __str__(self):
        # Use the candidate_name property in the __str__ method
        return f"{self.candidate_name} applied for {self.job.title}"
