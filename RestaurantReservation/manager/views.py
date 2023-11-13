from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from datetime import datetime, timedelta
from reservation.models import Shop, Reservation

# B001
class Console(TemplateView):
    template_name = "manager/console.html"

# C001
class CRShopList(ListView):
    template_name = "manager/cr_shop_list.html"
    model = Shop

# C002
class CRReservation(TemplateView):
    template_name = "manager/cr_reservation.html"

    # 画面表示時に実行されるメソッド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # リクエストから店舗IDと日付を取得
        shop_id = self.request.GET.get("shop_id")
        date = datetime.strptime(self.request.GET.get("date"), "%Y-%m-%d")

        # 前日と翌日の日付を算出
        tomorrow = date + timedelta(days=1)
        yesterday = date + timedelta(days=-1)

        # 店舗情報を取得
        shop = Shop.objects.get(shop_id=shop_id)

        # 予約数を取得
        reservation_dist = {}
        for time in range(17, 23):
            reservation_num = Reservation.objects.filter(reservation_date=date, reservation_time=time).count()
            reservation_dist[time] = reservation_num

        # テンプレートに値を渡す
        context["reservation_dist"] = reservation_dist
        context["shop"] = shop
        context["date"] = date.strftime("%Y-%m-%d")
        context["tomorrow"] = tomorrow.strftime("%Y-%m-%d")
        context["yesterday"] = yesterday.strftime("%Y-%m-%d")

        return context

# C003
class CRReservationDetail(ListView):
    template_name = "manager/cr_reservation_detail.html"
    model = Reservation

    # 画面表示時に実行されるメソッド
    def get_context_data(self, **kwargs):

        # 予約情報を取得（条件はget_querysetメソッドで指定）
        context = super().get_context_data(**kwargs)

        # リクエストから店舗IDと日付と時間を取得
        shop_id = self.request.GET.get("shop_id")
        date = datetime.strptime(self.request.GET.get("date"), "%Y-%m-%d")
        time = self.request.GET.get("time")

        # 店舗情報を取得
        shop = Shop.objects.get(shop_id=shop_id)

        # テンプレートに値を渡す
        context["shop"] = shop
        context["date"] = date.strftime("%Y-%m-%d")
        context["time"] = time

        return context

    # クエリ実行時に実行されるメソッド
    def get_queryset(self, **kwargs):

        # リクエストから店舗IDと日付と時間を取得
        shop_id = self.request.GET.get("shop_id")
        date = datetime.strptime(self.request.GET.get("date"), "%Y-%m-%d")
        time = self.request.GET.get("time")

        # 検索条件を設定
        queryset = Reservation.objects.filter(reservation_date=date, reservation_time=time)

        return queryset
    
# D001
class SSShopList(ListView):
    template_name = "manager/ss_shop_list.html"
    model = Shop

# D002（未開発）

    
# D003（未開発）


# D004（未開発）

    
# D005
class SSUpdateCompleted(DetailView):
    template_name = "manager/ss_update_completed.html"
    model = Shop

# D006
class SSDeleteForm(DeleteView):
    template_name = "manager/ss_delete_form.html"
    model = Shop
    success_url = "/manager/setting_shop/delete_completed"
    
# D007
class SSDeleteCompleted(TemplateView):
    template_name = "manager/ss_delete_completed.html"
    