# Generated by Django 2.2 on 2021-08-12 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentrequest',
            name='receiver',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointmentrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointmentlist',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointmentlist',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
    ]
