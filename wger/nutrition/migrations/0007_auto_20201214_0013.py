# Generated by Django 3.1.4 on 2020-12-13 23:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0006_auto_20201201_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Ingredient Categories',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True,
                                   verbose_name='Brand name of product'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='common_name',
            field=models.CharField(blank=True, max_length=200, null=True,
                                   verbose_name='Common name of product'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='last_imported',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='source_name',
            field=models.CharField(blank=True, max_length=200, null=True,
                                   verbose_name='Source Name'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='source_url',
            field=models.URLField(blank=True, help_text='Link to product', null=True,
                                  verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200,
                                   validators=[django.core.validators.MinLengthValidator(3)],
                                   verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='nutrition.ingredientcategory', verbose_name='Category'),
        ),
    ]
