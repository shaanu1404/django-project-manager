from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save

from teams.models import Team
from projects.models import Project
from datetime import date


class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="employee")
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='images/profile-image/%Y/%m/%d/', null=True, blank=True)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.email

    def get_all_projects(self):
        return Project.objects.filter(team_alloted=self.team).order_by('-created_at')

"""
When an user is saved its profile must be created.
A post_save is used for creating a profile.
"""


def employee_profile_create_reviever(sender, instance, created, *args, **kwargs):
    if created:
        try:
            employee, employee_created = EmployeeProfile.objects.get_or_create(
                user=instance)
        except:
            print('Error in profile creation.')


post_save.connect(employee_profile_create_reviever, sender=User)


"""
Calculating age from date of birth
"""


def employee_age_pre_save(sender, instance, *args, **kwargs):
    if instance.dob:
        dob = instance.dob
        diff = date.today() - dob
        age = diff.days // 365.2425
        instance.age = age


pre_save.connect(employee_age_pre_save, sender=EmployeeProfile)



"""
Save employee's team as lead.
"""

def team_lead_post_save(sender, instance, created, *args, **kwargs):
    user = instance.team_lead
    if user:
        try:
            employee = EmployeeProfile.objects.get(user=user)
            employee.team = instance
            employee.save(update_fields=['team'])
        except:
            raise ValueError("Employee not found.")

post_save.connect(team_lead_post_save, sender=Team)