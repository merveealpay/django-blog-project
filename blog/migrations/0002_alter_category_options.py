# Generated by Django 3.2.5 on 2021-07-20 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_blog_categor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
