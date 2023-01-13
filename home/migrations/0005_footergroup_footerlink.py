# Generated by Django 4.1.5 on 2023-01-13 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=250)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.footergroup')),
            ],
        ),
    ]
