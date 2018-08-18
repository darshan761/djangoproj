from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.login, name='login'),
    path('register',views.register, name='register'),
    path('home',views.home, name='home'),
    path('myhome',views.myhome,name='myhome'),
    path('cart/<int:userid>',views.cart,name='cart'),
    path('aboutUs',views.aboutUs, name='aboutUs'),
    path('personaldet/<int:userid>',views.personaldet,name='personaldet'),
    path('logout',views.logout,name="logout"),
    path('update',views.update,name="update"),
    path('addtocart/<int:userid>',views.addtocart,name="addtocart"),
    path('removefromcart/<int:itemid>',views.removefromcart,name="removefromcart")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
