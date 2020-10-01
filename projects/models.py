from django.db import models
from teams.models import Team

category_choices = (
    ('digital_marketing', 'Digital Marketing'),
    ('social_media', 'Social Media Marketing'),
    ('web_designing', 'Web Designing'),
    ('graphic_designing', 'Graphic Designing'),
    ('identity_designing', 'Identity Designing'),
    ('web_development', 'Web Development'),
    ('mobile_development', 'Mobile App Development'),
)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=40, choices=category_choices)
    team_alloted = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    project_id = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='status')
    description = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
