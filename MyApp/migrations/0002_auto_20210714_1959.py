# Generated by Django 2.2.5 on 2021-07-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('made_on', models.DateField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischarge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40)),
                ('assignedDoctorName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('admitDate', models.DateField()),
                ('releaseDate', models.DateField()),
                ('daySpent', models.PositiveIntegerField()),
                ('roomCharge', models.PositiveIntegerField()),
                ('medicineCost', models.PositiveIntegerField()),
                ('doctorFee', models.PositiveIntegerField()),
                ('OtherCharge', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='date',
            new_name='admitDate',
        ),
    ]
