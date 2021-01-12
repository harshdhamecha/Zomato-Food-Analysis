# Generated by Django 2.1.5 on 2020-06-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='slider_heading',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
