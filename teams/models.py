from django.db import models
from django.contrib.auth.models import User

category_choices = (
    ('marketing', 'Marketing'),
    ('sales', 'Sales'),
    ('development', 'Development'),
    ('creative_designing', 'Creative Designing'),
    ('social_media_handling', 'Social Media Handling'),
)


class Team(models.Model):
    team_lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=40, choices=category_choices)

    @property
    def team_id(self):
        return "Team " + str(self.id)

    def __str__(self):
        return self.team_id
