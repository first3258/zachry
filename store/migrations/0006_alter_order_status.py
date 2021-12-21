# Generated by Django 4.0 on 2021-12-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('กำลังเตรียมคำสั่งซื้อ', 'กำลังเตรียมคำสั่งซื้อ'), ('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งสำเร็จ', 'จัดส่งสำเร็จ')], default='กำลังเตรียมคำสั่งซื้อ', max_length=255),
        ),
    ]
