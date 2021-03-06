# Generated by Django 3.1.7 on 2021-04-08 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_sessionregister_registered_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionregister',
            name='registered_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrants', to='core.session'),
        ),
    ]
