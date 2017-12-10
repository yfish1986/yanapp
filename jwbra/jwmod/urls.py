from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib.auth.views import login, logout_then_login

from . import views

urlpatterns = [
    url(r'^$', views.IndexView),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/jwmod/img/favicon.ico')),
    url(r'^jwbra_list$', views.JwBraList.as_view(), name='JwBraList'),
    url(r'^login$', views.myLogin, name='mylogin'),
    url(r'^logout$', views.myLogout, name='mylogout'),

    url(r'^accounts/login$',  views.myLogin, name='mylogin2'),

    url(r'^jwbra_add$', views.jwBraAdd, name='jwBraAdd'),

    url(r'^stock_list$', views.stock_list, name='stock_list'),
    url(r'^stock_delete_post$', views.stock_delete_post, name='stock_delete_post'),
    url(r'^stock_sell$', views.stock_sell, name='stock_sell'),
    url(r'^stock_sell_post$', views.stock_sell_post, name='stock_sell_post'),
    url(r'^stock_sell_list$', views.stock_sell_list, name='stock_sell_list'),
    url(r'^stock_sell_delete_post$', views.stock_sell_delete_post, name='stock_sell_delete_post'),


    url(r'^customer_list$', views.customer_list, name='customer_list'),
    url(r'^customer_add$', views.customer_add, name='customer_add'),
    url(r'^customer_add_post$', views.customer_add_post, name='customer_add_post'),
    url(r'^customer_update$', views.customer_update, name='customer_update'),
    url(r'^customer_update_post$', views.customer_update_post, name='customer_update_post'),
    url(r'^customer_delete$', views.customer_delete, name='customer_delete'),
]