# Generated by Django 4.0.1 on 2022-01-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_remove_game_is_completed_alter_game_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='game',
            name='last_modified',
        ),
    ]