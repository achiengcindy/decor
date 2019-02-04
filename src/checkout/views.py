from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse #payment

from .models import OrderItem
from .models import Order
from .forms import CheckoutForm
#from cart.forms import CartAddProductForm
from cart.cart import Cart

User = get_user_model()


def order_create(request):
    """ we will obtain the current cart from the session """
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.owner = request.user
            order.status = Order.SUBMITTED
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            # set the order in the session
            # request.session['order_id'] = order.id
            # redirect to the payment
            return render(request, 'orders/order/created.html',{"order": order, 'cart': cart,})
            #return redirect(reverse('orders:order_created',kwargs={"order_id": order.id, 'cart': cart,}))
    else:
        if request.user.is_authenticated:
            profile = request.owner.profile
            form = CheckoutForm(instance=profile)
        else:
            form = CheckoutForm()
    return render(request, 'orders/order_create.html', {'cart': cart,'form':form})

  
@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    # set the order in the session
    request.session['order_id'] = order.id
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render(request,'orders/order_details.html',{'order':order})
    # redirect to the payment
    #return redirect(reverse('payment:payment_lipa', kwargs={"order_id": order.pk}))


