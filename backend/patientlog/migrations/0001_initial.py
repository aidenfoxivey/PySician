# Generated by Django 3.2.5 on 2021-07-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('telnum', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
