# Generated by Django 3.0.4 on 2020-03-07 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(blank=True, max_length=150)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('contact', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('bio', models.TextField()),
                ('baptism', models.BooleanField(default=False)),
                ('eucharist', models.BooleanField(default=False)),
                ('confirmation', models.BooleanField(default=False)),
                ('reconciliation', models.BooleanField(default=False)),
                ('anointing_of_the_sick', models.BooleanField(default=False)),
                ('marriage', models.BooleanField(default=False)),
                ('holy_orders', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Family')),
                ('scc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Community')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
