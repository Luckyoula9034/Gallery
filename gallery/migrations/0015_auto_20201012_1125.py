# Generated by Django 3.1.2 on 2020-10-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gallery.editor'),
        ),
    ]
