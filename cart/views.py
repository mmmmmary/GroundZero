from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from Myapp.models import Obra
# Create your views here.


def add_to_cart(request, product_id):
    product = get_object_or_404(Obra, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart = None  # Implementa la lógica para obtener el carrito
    return render(request, 'cart/cart.html', {'cart': cart})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')