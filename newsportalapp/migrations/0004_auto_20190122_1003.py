# Generated by Django 2.1.4 on 2019-01-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportalapp', '0003_auto_20190107_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='newscategory',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
