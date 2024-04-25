# Generated by Django 5.0.1 on 2024-04-23 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_complaintmodel_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModelAnother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='resumeapp.regmodel')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='resumeapp.usermodel')),
            ],
        ),
    ]
