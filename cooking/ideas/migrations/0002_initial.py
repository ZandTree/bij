# Generated by Django 3.2.4 on 2021-08-24 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='useridearelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='categ',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ideas', to='ideas.category'),
        ),
        migrations.AddField(
            model_name='idea',
            name='fans',
            field=models.ManyToManyField(related_name='idea_fans', through='ideas.UserIdeaRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Tags should be separated by comma', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ideas.category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'slug')},
        ),
    ]