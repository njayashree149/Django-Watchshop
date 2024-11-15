from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home,name="home"),
    path('about' ,views.About,name="about"),
    path('upload',views.Upload,name="upload"),
    path('login',views.login_user,name="login"),
    path('signup',views.sign_up,name="signup"),
    path('logout',views.log_out,name="logout"),
    path('product/<int:id>',views.show_product,name="product"),
    path('addtowishlist/<int:id>',views.Addtowishlist,name="addtowishlist"),
    path('wishlist',views.show_wishlist,name="show_wishlist"),
    path('removewish/<int:id>',views.removewish,name="removewish"),
    path('addtocart/<int:id>', views.addtocart, name ='addtocart'),
    path('show_cart',views.show_cart,name="show_cart"),
    path('remove_cart/<int:id>',views.removeCart,name="remove_cart")
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)