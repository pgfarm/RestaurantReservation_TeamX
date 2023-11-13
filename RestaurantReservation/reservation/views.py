from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Shop, Reservation

# A001
class ShopList(ListView):
    template_name = "reservation/shop_list.html"
    model = Shop

# A002
class ShopDetail(DetailView):
    template_name = "reservation/shop_detail.html"
    model = Shop

# A003（未開発）
# いまからコーディングします
# 追加開発
# 追加開発

# A004（未開発）
# ここも編集します

# A005（未開発）
