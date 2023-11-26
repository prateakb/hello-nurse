# Generated by Django 4.2.4 on 2023-11-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='slot',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('pending', 'Pending Approval'), ('approved', 'Approved'), ('taken', 'Taken')], default='available', max_length=10),
        ),
    ]
