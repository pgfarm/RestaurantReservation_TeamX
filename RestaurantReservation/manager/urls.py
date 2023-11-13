from django.urls import path
from . import views

urlpatterns = [
    # コンソール画面
    path("", views.Console.as_view(), name="console"),          # B001
    path("console", views.Console.as_view(), name="console"),   # B001

    # 予約確認画面
    path("confirm_reservation/shop_list", views.CRShopList.as_view(), name="confirm_reservation/shop_list"),                            # C001
    path("confirm_reservation/reservation", views.CRReservation.as_view(), name="confirm_reservation/reservation"),                     # C002
    path("confirm_reservation/reservation_detail", views.CRReservationDetail.as_view(), name="confirm_reservation/reservation_detail"), # C003

    # 店舗設定画面
    path("setting_shop/shop_list", views.SSShopList.as_view(), name="setting_shop/shop_list"),                                          # D001
    # path("setting_shop/register_form", views.SSRegisterForm.as_view(), name="setting_shop/register_form"),                              # D002
    # path("setting_shop/register_completed/<int:pk>", views.SSRegisterCompleted.as_view(), name="setting_shop/register_completed"),      # D003
    # path("setting_shop/update_form/<int:pk>", views.SSUpdateForm.as_view(), name="setting_shop/update_form"),                           # D004
    path("setting_shop/update_completed/<int:pk>", views.SSUpdateCompleted.as_view(), name="setting_shop/update_completed"),            # D005
    path("setting_shop/delete_form/<int:pk>", views.SSDeleteForm.as_view(), name="setting_shop/delete_form"),                           # D006
    path("setting_shop/delete_completed", views.SSDeleteCompleted.as_view(), name="setting_shop/delete_completed"),                     # D007
]
