# Generated by Django 4.0 on 2021-12-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_order_alter_product_image_orderitem_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'กำลังเตรียมคำสั่งซื้อ'), ('B', 'กำลังจัดส่ง'), ('C', 'จัดส่งสำเร็จ')], default='A', max_length=255),
        ),
    ]
