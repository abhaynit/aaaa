# Generated by Django 3.2.4 on 2021-10-01 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20211001_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='recrd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.BigIntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('student_branch', models.CharField(choices=[('CSE', 'CSE'), ('CIVIL', 'CIVIL'), ('EEE', 'EEE'), ('EIE', 'EIE'), ('ECE', 'ECE'), ('MECH', 'MECH')], max_length=10)),
                ('purpose', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('exit_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('entry_time', models.DateTimeField(blank=True, null=True)),
                ('is_late', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='recoord',
        ),
    ]