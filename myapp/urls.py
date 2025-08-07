from django.urls import path
from django.conf import settings
# from django.contrib import admin
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),  # The empty path ('') points to the index view
    path('adopt.html', views.adopt, name='adopt'),
    path('food.html', views.food, name='food'),
    path('shop.html', views.shop, name='shop'),
    path('index.html',views.about,name='about'),
    path('login', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/index.html'), name='logout'),
    path('signup.html', views.signup, name='signup'),
    path('admin_home.html', views.admin_home, name='admin_home'),
    path('user_home.html', views.user_home, name='user_home'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)