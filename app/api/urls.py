from django.conf.urls import url
from api.views.balance import BalanceResult


urlpatterns = [
    url(r'^balance/$', BalanceResult.as_view(), name='balance'),
]