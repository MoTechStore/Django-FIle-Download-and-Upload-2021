# Generated by Django 3.1.1 on 2021-02-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='store/covers/')),
            ],
        ),
    ]
