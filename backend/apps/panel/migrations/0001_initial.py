# Generated by Django 3.0.7 on 2021-01-11 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('general_settings', models.CharField(blank=True, max_length=2048)),
                ('customization_settings', models.CharField(blank=True, max_length=2048)),
                ('widget_settings', models.CharField(blank=True, max_length=2048)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=253)),
                ('rcon_port', models.IntegerField()),
                ('rcon_password', models.CharField(max_length=128)),
                ('admins', models.ManyToManyField(to='users.User')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Shop')),
            ],
        ),
    ]
