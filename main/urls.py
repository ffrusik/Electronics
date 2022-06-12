from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>', views.ItemsDetailView.as_view(), name='items_detail'),
    path('<pk>/buy', views.buy, name='buy'),
    path('categories/notebooks_and_accessories', views.notebooks_and_accessories, name='notebooks_and_accessories'),
    path('categories/smartphones_tv_electronics', views.smartphones_tv_electronics, name='smartphones_tv_electronics'),
    path('search', views.search_results, name='search'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('trash', views.trash, name='trash'),
    path('buy_all', views.buy_all, name='buy_all'),
    path('bought_all', views.bought_all, name='bought_all'),
    path('favorite', views.favorite, name='favorite'),
    path('trash_favorite', views.trash_favorite, name='trash_favorite'),
    path('profile', views.profile, name='profile')
]
