# Generated by Django 3.1.3 on 2020-11-30 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_post_main_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='new_main_content',
            new_name='main_content',
        ),
    ]