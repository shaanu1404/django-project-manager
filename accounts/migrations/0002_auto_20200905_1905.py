# Generated by Django 3.1.1 on 2020-09-05 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='team_id',
            new_name='team',
        ),
    ]