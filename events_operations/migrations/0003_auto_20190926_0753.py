# Generated by Django 2.1.5 on 2019-09-26 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_operations', '0002_auto_20190926_0753'),
        ('events_operations', '0002_auto_20190921_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='event',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees_list',
            field=models.ManyToManyField(to='users_operations.Attendees'),
        ),
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='staff_list',
            field=models.ManyToManyField(to='users_operations.Staff'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(to='events_operations.Tag'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_operations.Organizer'),
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]