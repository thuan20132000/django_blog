# Generated by Django 4.0.5 on 2022-06-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('status', models.CharField(choices=[
                 ('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=50)),
            ],
        ),
    ]