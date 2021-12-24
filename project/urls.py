
#Global
from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('category/<slug:category_slug>', views.index, name="product_by_category"),
    path('product/<slug:category_slug>/<slug:product_slug>', views.productPage, name="productDetail"),
    path('cart/add/<int:product_id>', views.addCart, name="addCart"),
    path('cartdetail', views.cartdetail),
    path('cart/remove/<int:product_id>', views.removeCart, name="removeCart"),
    path('account/create', views.signUpView, name="signUp"),
    path('account/login', views.signInView, name="signIn"),
    path('account/logout', views.signOutView, name="signOut"),
    path('search/', views.search, name="search"),
    path('account/', views.account, name="account"),
    path('orderHistory/', views.orderHistory, name="orderHistory"),
    path('order<int:order_id>', views.orderView, name="orderDetails"),

]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)