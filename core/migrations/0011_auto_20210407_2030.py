# Generated by Django 3.1.7 on 2021-04-07 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_session_registrant'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionregister',
            name='sessionId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='core.session'),
        ),
        migrations.AlterField(
            model_name='session',
            name='registrant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session', to='core.sessionregister'),
        ),
    ]