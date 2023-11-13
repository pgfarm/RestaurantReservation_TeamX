from django.urls import path
from . import views

urlpatterns = [
    # 予約画面
    path("", views.ShopList.as_view(), name="shop_list"),                                                           # A001
    path("shop_list", views.ShopList.as_view(), name="shop_list"),                                                  # A001
    path("shop_detail/<int:pk>", views.ShopDetail.as_view(), name="shop_detail"),                                   # A002
    # path("availability", views.Availability.as_view(), name="availability"),                                        # A003
    # path("reservation_form", views.ReservationForm.as_view(), name="reservation_form"),                             # A004
    # path("reservation_completed/<int:pk>", views.ReservationCompleted.as_view(), name="reservation_completed"),     # A005
]
