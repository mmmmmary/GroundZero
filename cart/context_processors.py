from .models import Cart

def cart_counter(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            count = cart.cartitem_set.count()
        else:
            count = 0
    else:
        count = 0
    return {'cart_count': count}