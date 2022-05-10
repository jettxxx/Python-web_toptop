# Generated by Django 4.0.4 on 2022-05-09 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsrRegModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=500)),
                ('usr_email', models.CharField(blank=True, max_length=500, null=True)),
                ('usr_email_password', models.CharField(blank=True, max_length=10, null=True)),
                ('usr_ph_otp', models.PositiveIntegerField(blank=True, max_length=6, null=True)),
                ('usr_email_otp', models.PositiveIntegerField(blank=True, max_length=6, null=True)),
                ('root_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]