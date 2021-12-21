from store.models import Category, CartItem, Cart
from store.views import _cart_id

def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)

def counter(request):
    item_count = 0

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter( user = request.user.id )
            cartItem = CartItem.objects.all().filter( cart = cart[:1])

            for item in cartItem:
                item_count += item.quantity
        except Cart.DoesNotExist:
            item_count = 0 

    return dict(item_count = item_count)
