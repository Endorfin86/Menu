# Generated by Django 4.2 on 2023-04-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_paragraphs_parent_remove_paragraphs_selfitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraphs',
            name='selfitem',
            field=models.ManyToManyField(blank=True, null=True, to='main.paragraphs', verbose_name='Дочерние пункты'),
        ),
    ]
