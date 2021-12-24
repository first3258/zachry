from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from store.models import Category, Product, Cart, CartItem, Order, OrderItem
from store.forms import SignUpForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

# Create your views here.

def index(request, category_slug=None):
   
    products = None
    category_page = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.all().filter(category = category_page)
    else :
        products = Product.objects.all()
    
    
    return render(request, 'index.html', {'products': products, 'category': category_page})

def productPage(request, category_slug, product_slug):
    error = []
    try:
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        category = Product.objects.filter(category__slug = category_slug)

    except Exception as e :
        raise e

    if request.method == 'POST':
            quantity = request.POST['quantiry']


            try:
                # cart = Cart.objects.get(card_id = _cart_id(request))
                cart = Cart.objects.get(user = request.user.id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(card_id =  _cart_id(request), user = request.user.id)
                cart.save()
    

    
            try:
                #ซื้อรายการสิ้นค้าซ้ำ
                cart_item = CartItem.objects.get(product_id = product, cart_id = cart)
                if int(quantity) + cart_item.quantity > product.stock:
                    error.append("จำนวนหนังสือไม่พอ")
                    print(error)
                else:
                    
                    cart_item.quantity += int(quantity)
                    cart_item.save()
            except CartItem.DoesNotExist:
                #ซื้อรายการสิ้นค้าครั้งแรก
                if int(quantity) > product.stock:
                    error.append("จำนวนหนังสือไม่พอ")
                else:
                    cart_item = CartItem.objects.create(
                        product = product,
                        cart = cart,
                        quantity = quantity
                    )
                    cart_item.save()

            return render(request, 'product.html', {'product': product, 'category': category, 'error': error})

    return render(request, 'product.html', {'product': product, 'category': category, 'error': error})


def _cart_id(request):
    cart = request.session.session_key
    
    if not cart:
        cart = request.session.create()

    return cart

@login_required(login_url = 'signIn')
def addCart(request, product_id):
    #ดึง id จาก frontend
    product = Product.objects.get(id = product_id)

    #สร้างตะกร้ามีกับยังไม่เคยมี
    try:
        # cart = Cart.objects.get(card_id = _cart_id(request))
        cart = Cart.objects.get(user = request.user.id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(card_id =  _cart_id(request), user = request.user.id)
        cart.save()
    
    try:
        #ซื้อรายการสิ้นค้าซ้ำ
        cart_item = CartItem.objects.get(product_id = product, cart_id = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        #ซื้อรายการสิ้นค้าครั้งแรก
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()

    return redirect('/')

    

def cartdetail(request):
    total = 0
    counter = 0
    cart_items = None

    try:
        cart = Cart.objects.get(user = request.user.id)
        cart_items = CartItem.objects.filter(cart = cart)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except Exception as e :
        pass

    stripe.api_key = settings.SECRET_KEY
    stripe_total = int(total*100)
    description = "Playment Online"
    data_key = settings.PUBLIC_KEY

    if request.method == 'POST' and 'payment' in request.POST:
        email = request.POST['email']
        name = request.POST['name']
        address = request.POST['address']

        order = Order.objects.create(
                name = name,
                address = address,
                total = total,
                email = email,
                payment_status = 'ชำระเงินปลายทาง'
            )

        order.save()

        for item in cart_items:
                product = Product.objects.get(id = item.product.id)
                order_item = OrderItem.objects.create(
                    product = item.product.name,
                    quantity = item.quantity,
                    price = item.product.price,
                    order = order
                )
                product.stock -= item.quantity

                product.save()  
                order_item.save()
                item.delete()

        return redirect('home')

    elif request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            name = request.POST['stripeBillingName']
            address = request.POST['stripeBillingAddressLine1']
            city = request.POST['stripeBillingAddressCity']
            postcode = request.POST['stripeShippingAddressZip']
            
            customer = stripe.Customer.create(
                email = email,
                source = token
            )
            charge = stripe.Charge.create(
                amount = stripe_total,
                currency = 'thb',
                description = description,
                customer = customer.id
            )

            order = Order.objects.create(
                name = name,
                address = address,
                city = city,
                postcode = postcode,
                total = total,
                email = email,
                token = token,
                payment_status = 'ชำระเงินเรียบร้อย'
            )
            
            order.save()

            for item in cart_items:
                product = Product.objects.get(id = item.product.id)
                order_item = OrderItem.objects.create(
                    product = item.product.name,
                    quantity = item.quantity,
                    price = item.product.price,
                    order = order
                )
                product.stock -= item.quantity

                product.save()  
                order_item.save()
                item.delete()
            return redirect('home')

        except stripe.error.CardError as e :
            return False, e
    return render(request, 'cartdetail.html', {'cart_items': cart_items, 'total': total, 'counter': counter, 
    'data_key': data_key, 'stripe_total':stripe_total, 'description': description })

def removeCart(request, product_id):
    cart = Cart.objects.get(user = request.user.id)

    product = get_object_or_404(Product, id = product_id)

    cartItem = CartItem.objects.get(product = product, cart = cart)
    
    cartItem.delete()
    return redirect('/cartdetail')

def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # แบ่ง group user
            username = form.cleaned_data.get('username')  
            signUpUser = User.objects.get(username=username)
            customer_group = Group.objects.get(name = "Customer")
            customer_group.user_set.add(signUpUser)
            return redirect('signIn')

    else :
        form = SignUpForm()
    return render(request, 'signup.html', { 'form' : form})

def signInView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signUp')
    else: 
        form = AuthenticationForm()


    return render(request, 'signin.html', {'form': form})

def signOutView(request):
    logout(request)
    return redirect('home')

def search(request):
    products = Product.objects.filter(name__contains = request.GET['title'])

    return render(request, 'index.html', {'products': products})


def account(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        return redirect('account')
    return render(request, 'account.html')

def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        orders = Order.objects.filter(email = email)
    return render(request, 'order.html', {'orders': orders})

def orderView(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(email = email, id = order_id)
        orderItem = OrderItem.objects.filter(order = order)

    return render(request, 'orderdetail.html', {'order' : order, 'order_items': orderItem})

