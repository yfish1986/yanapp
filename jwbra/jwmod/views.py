# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.shortcuts import render,render_to_response
from .models import JwBra,JwStockList, JwColour, JwStyle, JwSize, JwCustomer, JwSalesBill
from django.contrib.auth import authenticate, login
from django.contrib import auth
import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse




import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

# Create your views here.

def IndexView(request):
    return render(request, 'jwmod2/index.html')

#@login_required
class JwBraList(generic.ListView):
    template_name = 'jwmod2/Bra_list.html'
    context_object_name = 'jwbra_list'
    jwlist = JwBra.objects.all().order_by('style_name','colour_name','size_name')
    print(jwlist)

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        jwlist = JwBra.objects.all().order_by('style_name', 'colour_name', 'size_name')
        #return JwBra.objects.all().order_by('style_name','colour_name','size_name')
        return jwlist

#添加货物
#@login_required
def jwBraAdd(request):
    logging.debug("JwBraAdd %s" %(request.method))
    if request.method == 'GET':
        jwcolours = JwColour.objects.all().order_by('colour_name')
        jwstyles  = JwStyle.objects.all()
        jwsizes   = JwSize.objects.all().order_by('size_name')
        jwstocks = JwStockList.objects.all()

        return render(request, 'jwmod2/Bra_add.html',
                      {'jwstocks': jwstocks, 'jwcolours': jwcolours, 'jwstyles': jwstyles, 'jwsizes': jwsizes})
    if request.method == 'POST':
        logging.debug('stock_add_post start')
        jwcolour_id = request.POST['jwcolour_id']
        jwstyle_id = request.POST['jwstyle_id']
        jwsize_id = request.POST['jwsize_id']
        logging.debug('jwcolour_id=%s, jwstyle_id=%s, jwsize_id=%s' % (jwcolour_id, jwstyle_id, jwsize_id))
        colour_name = JwColour.objects.get(id=int(jwcolour_id))
        style_name = JwStyle.objects.get(id=int(jwstyle_id))
        size_name = JwSize.objects.get(id=int(jwsize_id))
        num = int(request.POST['jwstocknum'])
        price = float(request.POST['jwstockprice'])
        total = price * num
        jwstockelement = JwStockList(colour_name=colour_name,
                                     style_name=style_name, size_name=size_name, num=num, price=price, total=total)
        jwstockelement.save()
        # 添加数据到库存
        jwbra = JwBra.objects.get_or_create(style_name=style_name, colour_name=colour_name, size_name=size_name)

        jwbra[0].num = jwbra[0].num + int(num)
        jwbra[0].price = price
        jwbra[0].total = jwbra[0].price * jwbra[0].num
        jwbra[0].save()
        jwstocks = JwStockList.objects.all()
        jwcolours = JwColour.objects.all()
        jwstyles = JwStyle.objects.all()
        jwsizes = JwSize.objects.all()
        logging.debug('stock_add_post end')
        #return render(request, 'jwmod2/jwbra_list')
        return redirect( reverse("views.JwBraList.as_view",args=[]))




@login_required
def stock_delete_post(request):
    logging.debug('stock_delete_post start')
    jwstock = JwStockList.objects.get(id=int(request.POST['jwstock_id']))
    jwbra = JwBra.objects.get(style_name=jwstock.style_name, colour_name=jwstock.colour_name, size_name=jwstock.size_name)
    logging.debug('stock_delete_post jwbra.num=%d jwstock.num=%d'%(jwbra.num,jwstock.num))
    jwbra.num = jwbra.num - jwstock.num
    jwbra.total = jwbra.price * jwbra.num
    jwbra.save()
    jwstock.delete()
    jwstocks = JwStockList.objects.all()
    logging.debug('stock_delete_post end')
    return render(request, 'Bra_list.html',{'jwstocks': jwstocks,})
#货物清单
@login_required
def stock_list(request):
    logging.debug('stock_list start')
    jwstocks=JwStockList.objects.all().order_by('id')
    logging.debug('stock_list end')
    return render(request, 'Bra_list.html', {'jwstocks': jwstocks,})

#货物销售
@login_required
def stock_sell(request):
    logging.debug('stock_sell start')
    jwbar = JwBra.objects.get(id=int(request.POST['jwbar_id']))
    jwcustomers = JwCustomer.objects.all()
    logging.debug('stock_sell end')
    return render(request, 'stock_sell.html', {'jwbar':jwbar,'jwcustomers':jwcustomers})

#货物销售
@login_required
def stock_sell_post(request):
    jwbar = JwBra.objects.get(id=int(request.POST['jwbar_id']))
    jwbar_num = request.POST['jwbar_num']
    price = request.POST['price']
    jwbar.num = jwbar.num - int(jwbar_num)
    jwbar.save()
    total = int(jwbar_num) * int(price)
    jwcustomer = JwCustomer.objects.get(id=int(request.POST['customer_id']))

    jwsalesbill = JwSalesBill(customer_name=jwcustomer, jwbra=jwbar, sale_num=jwbar_num, sale_price = price, total = total,)
    jwsalesbill.save()

    jwSalesBills = JwSalesBill.objects.all()
    return render(request, 'stock_sell_list.html', {'jwSalesBills':jwSalesBills,})

#删除销售清单
@login_required
def stock_sell_delete_post(request):
    jwsale = JwSalesBill.objects.get(id=int(request.POST['jwstock_id']))
    jwbra = jwsale.jwbra

    jwbra.num = jwbra.num + jwsale.sale_num
    jwbra.save()
    jwsale.delete()
    jwSalesBills = JwSalesBill.objects.all()
    return render(request, 'stock_sell_list.html', {'jwSalesBills':jwSalesBills,})

#销售清单
@login_required
def stock_sell_list(request):
    jwSalesBills = JwSalesBill.objects.all()
    return render(request, 'stock_sell_list.html', {'jwSalesBills': jwSalesBills, })

#添加客户
@login_required
def customer_add(request):
    return render(request, 'customer_add.html')

#修改客户资源
@login_required
def customer_update(request):
    customer_id = request.POST['customer_id']
    customer = JwCustomer.objects.get(id=int(customer_id))
    return render(request, 'customer_update.html', {'customer':customer,})

#添加客户
@login_required
def customer_add_post(request):
    logging.debug('customer_add_post start')
    customer_name = request.POST['customer_name']
    customer_phone = request.POST['customer_phone']
    customer_addr = request.POST['customer_addr']
    logging.debug('customer_add_post customer_name=%s,customer_phone=%s,customer_addr=%s' %(customer_name,customer_phone,customer_addr))
    jwcustomer = JwCustomer(customer_name=customer_name,customer_phone = customer_phone, customer_addr= customer_addr)
    jwcustomer.save()
    jwcustomers = JwCustomer.objects.all()
    logging.debug('customer_add_post end')
    return render(request, 'customer_list.html',{'jwcustomers':jwcustomers,})

#客户清单
@login_required
def customer_list(request):
    logging.debug('customer_list1 start')
    jwcustomers = JwCustomer.objects.all()
    logging.debug('customer_list1 end')
    return render(request, 'customer_list.html',{'jwcustomers':jwcustomers,})

#修改客户资料
@login_required
def customer_update_post(request):
    logging.debug('customer_update_post start')
    customer_id = request.POST['customer_id']
    jwcustomer = JwCustomer.objects.get(id=customer_id)
    jwcustomer.customer_name = request.POST['customer_name']
    jwcustomer.customer_phone = request.POST['customer_phone']
    jwcustomer.customer_addr = request.POST['customer_addr']
    jwcustomer.save()
    jwcustomers = JwCustomer.objects.all()
    logging.debug('customer_update_post end')
    return render(request, 'customer_list.html', {'jwcustomers': jwcustomers, })

#删除客户资料
@login_required
def customer_delete(request):
    logging.debug('customer_delete start')
    customer_id = request.POST['customer_id']
    jwcustomer = JwCustomer.objects.get(id=customer_id)
    jwcustomer.delete()
    jwcustomers = JwCustomer.objects.all()
    logging.debug('customer_delete end ')
    return render(request, 'jwmod/customer_list.html', {'jwcustomers': jwcustomers, })

def myLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('passwd')
        print('username[%s] pwd[%s]' %(uname,pwd))
        user = authenticate(username=uname, password=pwd)
        res = {'status':False,'msg':None}
        if user is not None:
            auth.login(request, user)
            # 更新最后登录时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login = now_time
            user.save()
            res['status'] = True
            res['msg'] = '登录成功！！！'
            #return render(request,'jwmod/',res)
            return stock_list(request)
        else:
            res['status'] = True
            res['msg'] = '登录失败！！！'
            return render(request,'jwmod/login.html',res)
    else:
        return render(request,'jwmod2/login.html', {})

def myLogout(request):
    auth.logout(request)
    return render(request,'jwmod/login.html', {})

