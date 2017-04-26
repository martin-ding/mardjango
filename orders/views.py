from django.shortcuts import render, render_to_response

# Create your views here.

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from orders.models import Order

def index(request):
    limit = 20  # 每页显示的记录数
    orders = Order.objects.all()
    paginator = Paginator(orders, limit)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    try:
        orders = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        orders = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        orders = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render_to_response('orders/index.html', {'orders': orders})
