# Generated by Django 3.0.7 on 2020-06-20 15:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='banner_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
