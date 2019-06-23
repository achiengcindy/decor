def payment_lipa(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    #print(order)
    #print(order.paid)
    if (order.paid == True):
        return render(request,'payment/lipa.html', {'order':order})
    else:
        return redirect('orders:order_created', order.id)
      