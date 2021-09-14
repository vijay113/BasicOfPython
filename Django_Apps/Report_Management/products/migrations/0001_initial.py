# Generated by Django 3.2.7 on 2021-09-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(default='no_image.png', upload_to='products')),
                ('price', models.FloatField(help_text='in US dollars $')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
