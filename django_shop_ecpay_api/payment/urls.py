from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^process/$', views.payment_process
        , name='process'),
    url(r'^done/$', views.payment_done
        , name='done'),
    url(r'^canceled/$', views.payment_canceled
        , name='canceled'),
    #ECPay
    url(r'^ecpay/$',views.ecpay
        , name='ecpay'),
    url(r'^success/$', views.success_pay
        , name='success'),
    url(r'^fail/$', views.fail_pay
        , name='fail'),
    url(r'^end_page/$', views.end_page
        , name='end_page'),
]
