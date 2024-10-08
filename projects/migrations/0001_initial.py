# Generated by Django 5.1 on 2024-08-08 10:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('external_id', models.UUIDField()),
                ('comment', models.TextField()),
                ('type', models.CharField(choices=[('comment', 'comment'), ('problem', 'problem')], max_length=150)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=200)),
                ('blog', models.CharField(choices=[('Biznes Blok', 'Biznes Blok'), ('Boshqaruv Raisi', 'Boshqaruv Raisi'), ("Boshqaruv Raisi Birinchi O'rinbosari", "Boshqaruv Raisi Birinchi O'rinbosari"), ('Ijtimoiy Dasturlarni Amalgamgiritish', 'Ijtimoiy Dasturlarni Amalgamgiritish'), ('IT Kompleks', 'IT Kompleks'), ('Kuzatuv Kengashi', 'Kuzatuv Kengashi'), ('Moliyaviy Blok', 'Moliyaviy Blok'), ('Muammoli Aktivlar Bilan Ishlash Kompleksi', 'Muammoli Aktivlar Bilan Ishlash Kompleksi'), ('Operatsiyalar Kompleksi', 'Operatsiyalar Kompleksi'), ('Tranzaksion Xizmatlar Kompleksi', 'Tranzaksion Xizmatlar Kompleksi')], max_length=250)),
                ('departments', models.CharField(choices=[('Alternativ Kanallar Departamenti', 'Alternativ Kanallar Departamenti'), ('Bank Brendi va Axborot Xizmati', 'Bank Brendi va Axborot Xizmati'), ('Bank Tarmoqlarini Boshqarish Departamenti', 'Bank Tarmoqlarini Boshqarish Departamenti'), ('Chakana Biznes Departamenti', 'Chakana Biznes Departamenti'), ('Kichik va O`rta Biznes Departamenti', 'Kichik va O`rta Biznes Departamenti'), ('Ijro Nazorati Departamenti', 'Ijro Nazorati Departamenti'), ('Murojaatlar Bilan Ishlash Departamenti', 'Murojaatlar Bilan Ishlash Departamenti'), ('Strategiya Departamenti', 'Strategiya Departamenti'), ('Xavfsizlik va Axborotlarni Muhofaza Qilish', 'Xavfsizlik va Axborotlarni Muhofaza Qilish'), ('Xodimlarni Boshqarish Departamenti', 'Xodimlarni Boshqarish Departamenti'), ('Yuridik Departamenti', 'Yuridik Departamenti'), ('Kreditlar Monitoringi Departamenti', 'Kreditlar Monitoringi Departamenti'), ('Ijtimoiy Dasturlarni Amalgamgiritish Departamenti', 'Ijtimoiy Dasturlarni Amalgamgiritish Departamenti'), ('Informatsion Texnologiyalari Departamenti', 'Informatsion Texnologiyalari Departamenti'), ('Ichki Audit Departamenti', 'Ichki Audit Departamenti'), ('Ichki Nazorat va Komplayens Departamenti', 'Ichki Nazorat va Komplayens Departamenti'), ('Risk Menejment Departamenti', 'Risk Menejment Departamenti'), ("G'aznachilik Departamenti", "G'aznachilik Departamenti"), ('Ma’muriy-xo‘jalik Departamenti', 'Ma’muriy-xo‘jalik Departamenti'), ('Moliyaviy Hisobotlar va Nazorat Departamenti', 'Moliyaviy Hisobotlar va Nazorat Departamenti'), ('Muddati o`tgan Kreditlar Tahlili va Ularni Rejalashtirish Departamenti', 'Muddati o`tgan Kreditlar Tahlili va Ularni Rejalashtirish Departamenti'), ('Soft Collection Boshqarmasi', 'Soft Collection Boshqarmasi'), ('Bank Kartalari Tizimlarini Qo‘llab-quvvatlash Departamenti', 'Bank Kartalari Tizimlarini Qo‘llab-quvvatlash Departamenti'), ('Operatsiyalar Departamenti', 'Operatsiyalar Departamenti'), ('Jamg`arib Boriladigan Pensiya Ta`minoti Tizimini Qo`llab-quvvatlash Departamenti', 'Jamg`arib Boriladigan Pensiya Ta`minoti Tizimini Qo`llab-quvvatlash Departamenti'), ('Naqd Pullarni Boshqarish va Kassa Amaliyotlari Departamenti', 'Naqd Pullarni Boshqarish va Kassa Amaliyotlari Departamenti'), ('Tranzaksion Banking Departamenti', 'Tranzaksion Banking Departamenti'), ('Inson Resurslarini Boshqarish', 'Inson Resurslarini Boshqarish')], max_length=250)),
                ('size', models.CharField(choices=[('Multi', 'Multi'), ('Mono', 'Mono'), ('Mega', 'Mega')], max_length=200)),
                ('level', models.CharField(choices=[('Past', 'Past'), ("O'rta", "O'rta"), ('Yuqori', 'Yuqori'), ("O'ta yuqori", "O'ta yuqori")], max_length=200)),
                ('speed', models.CharField(choices=[("O'rta", "O'rta"), ('Qisqa', 'Qisqa'), ('Uzoq', 'Uzoq')], max_length=200)),
                ('type', models.CharField(choices=[('Aralash', 'Aralash'), ('Iqtisodiy', 'Iqtisodiy'), ('Raqamlashtirish', 'Raqamlashtirish'), ('Strategik', 'Strategik'), ('Tashkiliy', 'Tashkiliy'), ('Texnologik', 'Texnologik')], max_length=200)),
                ('description', models.TextField()),
                ('termination', models.CharField(default=0, max_length=20)),
                ('start_date', models.DateTimeField()),
                ('deadline', models.DateField()),
                ('budget', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('Jarayonda', 'Jarayonda'), ('Tugatilgan', 'Tugatilgan')], default='Yangi', max_length=150)),
                ('spent_money', models.CharField(default=0, max_length=150)),
                ('author', models.ManyToManyField(related_name='author', to=settings.AUTH_USER_MODEL)),
                ('team', models.ManyToManyField(related_name='team', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('termination', models.CharField(default=0, max_length=20)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('Jarayonda', 'Jarayonda'), ('Tugatilgan', 'Tugatilgan')], default='Yangi', max_length=30)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField()),
                ('document', models.FileField(blank=True, max_length=500, upload_to='')),
                ('related', models.CharField(choices=[('project_related', 'project_related'), ('phase_related', 'phase_related'), ('task_related', 'task_related')], max_length=150)),
                ('created_at', models.DateField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assigned_to', models.CharField(max_length=250)),
                ('deadline', models.DateField()),
                ('name', models.CharField(max_length=250)),
                ('termination', models.CharField(default=0, max_length=20)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ('Jarayonda', 'Jarayonda'), ('Tugatilgan', 'Tugatilgan')], default='Yangi', max_length=150)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.phase')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
