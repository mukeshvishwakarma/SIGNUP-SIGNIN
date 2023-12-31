# Generated by Django 4.0.4 on 2023-10-04 03:30

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('location', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'usermodel',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mobile_no', models.IntegerField(unique=True)),
                ('alternate_mob_no', models.IntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField(max_length=20)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('address_line3', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('basic_qualification', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField(max_length=20)),
                ('department', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('reporting_to', models.CharField(max_length=255)),
                ('linit_email', models.CharField(max_length=255)),
                ('linit_cell_no', models.CharField(max_length=255)),
                ('linit_extension', models.CharField(max_length=255)),
                ('insurance_policy_no', models.CharField(max_length=255)),
                ('sl_per_month_annum', models.CharField(max_length=255)),
                ('pl_per_monh_annum', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
