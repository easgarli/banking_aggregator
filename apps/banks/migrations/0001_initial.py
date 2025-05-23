# Generated by Django 5.2 on 2025-04-29 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='bank_logos/')),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('loan_type', models.CharField(max_length=50)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_loan_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('loan_term_months', models.IntegerField()),
                ('fees', models.TextField(blank=True)),
                ('special_offers', models.TextField(blank=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_products', to='banks.bank')),
            ],
        ),
    ]
