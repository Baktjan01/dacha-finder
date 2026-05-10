from django.db import models
from decimal import Decimal
from dachas.models import Dacha


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает оплаты'),
        ('partial', 'Оплачено 50%'),
        ('paid', 'Полностью оплачено'),
        ('cancelled', 'Отменено'),
    ]

    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name='bookings')
    telegram_id = models.BigIntegerField()
    telegram_username = models.CharField(max_length=100, blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        days = (self.date_to - self.date_from).days
        self.total_price = days * self.dacha.price_per_day
        self.deposit_amount = self.total_price * Decimal('0.5')  # 50%
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dacha.name} | {self.date_from} - {self.date_to}"
