# Generated by Django 3.1.2 on 2020-10-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='image_url',
            field=models.URLField(default='https://www.hungryhowies.com/sites/default/files/styles/menu_item_280x175/public/images/menu-items/thumbnails/buildyourownpizza_0.png?itok=fgzFck86', max_length=225),
            preserve_default=False,
        ),
    ]
