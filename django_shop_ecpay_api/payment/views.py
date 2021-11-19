from decimal import Decimal

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'TWD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request,
                  'payment/process.html',
                  {'order': order, 'form': form})


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
#########################ECPay##########################
from .ecpay import main
from django.http import HttpResponseRedirect

@csrf_exempt
def ecpay(request):
    order_id = request.session.get('order_id')
    return HttpResponse(main(order_id))

def success_pay(request):
    return render(request, 'payment/success.html')

def fail_pay(request):
    return render(request, 'payment/fail.html')

@csrf_exempt
def end_page(request):
    print("to user server")
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('payment:fail'))

    if request.method == 'POST':
        result = request.POST.get('RtnMsg')
        print(result)
        if result == 'Succeeded':
            print("#######")
            print(request.POST.get('TradeNo') )
            print(request.POST.get('TradeAmt'))
            print(request.POST.get('TradeDate'))
            check = request.POST.get('CheckMacValue')
            print(check)
            print("#######")
            
            return HttpResponseRedirect(reverse('payment:success'))
        # 判斷失敗
        else:
            return HttpResponseRedirect(reverse('payment:fail'))

def end_return(request):
    if request.method == 'POST':
        return '1|OK'