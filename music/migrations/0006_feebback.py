# Generated by Django 2.2.3 on 2019-08-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_customuser_nick_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeebBack',
            fields=[
                ('feedback_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
                ('mobile_no', models.CharField(default=None, max_length=20)),
                ('tmessage', models.TextField(default=None)),
            ],
        ),
    ]
