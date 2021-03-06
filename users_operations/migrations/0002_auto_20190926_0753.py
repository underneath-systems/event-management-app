# Generated by Django 2.1.5 on 2019-09-26 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users_operations.User')),
                ('phone', models.CharField(max_length=20)),
            ],
            bases=('users_operations.user',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users_operations.User')),
                ('working_hours', models.IntegerField(default=8)),
            ],
            bases=('users_operations.user',),
        ),
        migrations.RemoveField(
            model_name='attendees',
            name='event',
        ),
        migrations.AddField(
            model_name='attendees',
            name='qr_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendees',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users_operations.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_id',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
