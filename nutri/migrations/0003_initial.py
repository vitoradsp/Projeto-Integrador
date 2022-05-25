# Generated by Django 4.0.4 on 2022-05-23 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutri', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('idade', models.IntegerField()),
                ('genero', models.CharField(max_length=255)),
                ('nivel_atividade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nutri.nivelatividade')),
                ('objetivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nutri.objetivo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]