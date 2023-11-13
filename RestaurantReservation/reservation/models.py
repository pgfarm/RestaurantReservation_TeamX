from django.db import models

# 店舗情報を管理するテーブル
class Shop(models.Model):
    shop_id     = models.AutoField(primary_key=True)
    name        = models.TextField()
    tel         = models.TextField()
    post_code   = models.TextField()
    address     = models.TextField()
    seat_num    = models.IntegerField()

# 予約情報を管理するテーブル
class Reservation(models.Model):
    reservation_id      = models.AutoField(primary_key=True)
    shop_id             = models.IntegerField()
    reservation_date    = models.DateField()
    reservation_time    = models.IntegerField()
    reserver_name       = models.TextField()
    reserver_tel        = models.TextField()
    reserver_num        = models.IntegerField()
    reserver_allergy    = models.TextField(null=True, blank=True)
