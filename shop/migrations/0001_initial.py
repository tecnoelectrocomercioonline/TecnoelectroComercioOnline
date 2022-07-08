# Generated by Django 4.0.6 on 2022-07-08 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('capacity', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('smartphone-1', 'Smartphones'), ('buds-1', 'Buds'), ('watch-1', 'Watch'), ('tablets-1', 'Tablets'), ('laptops-1', 'Laptops'), ('monitores-1', 'Motinotres'), ('electrodomesticos-1', 'Electrodomesticos'), ('muebleria-1', 'Muebleria'), ('lineablanca-1', 'Linea Blanca'), ('herramientas-1', 'Herramientas'), ('bicicletas-1', 'Bicicletas'), ('maquillaje-1', 'Maquillaje')], max_length=20)),
                ('productphoto', models.ImageField(blank=True, null=True, upload_to='shop/catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productos')),
            ],
        ),
    ]
