# Generated by Django 4.0.2 on 2022-07-07 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateTimeField(auto_now=True)),
                ('nome_emprestado_anonimo', models.CharField(blank=True, max_length=30, null=True)),
                ('avaliacao', models.CharField(blank=True, choices=[('d', 'Disponivel'), ('a', 'Agendado'), ('s', 'Solicitado'), ('e', 'Emprestado')], max_length=11, null=True)),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='livros.livro')),
                ('nome_emprestado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Avaliacao',
        ),
    ]