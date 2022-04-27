from django.urls import include, path, re_path
from .views import (
    CheckoutView,
    OrderSummaryView,
    PaymentView,
    HomeView,
    ItemDetailView,
    IngredientView,
    CategoryView,
    TagsView,
    loginuser,signupuser,logoutuser,
    add_to_cart,
    remove_from_cart,
    remove_singe_item_from_cart,

)
from django.contrib import admin
# admin.autodiscover()
app_name = 'core'

urlpatterns = [
    path('signup/', signupuser, name='signupuser'),
    path('login/', loginuser, name='loginuser'),
    path('logout/',logoutuser, name='logoutuser'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    re_path(r'^add-to-cart/(?P<recipe_name>[A-Za-z_\-0-9]+)/(?P<slug>[A-Za-z_\-0-9]+)$', add_to_cart, name='add-to-cart'),
    re_path(r'^remove-from-cart/(?P<recipe_name>[A-Za-z_\-0-9]+)/(?P<slug>[A-Za-z_\-0-9]+)$', remove_from_cart, name='remove-from-cart'),
    re_path(r'^recipe/(?P<recipe_name>[A-Za-z_\-0-9]+)/(?P<slug>[A-Za-z_\-0-9]+)$',
            ItemDetailView.as_view(), name='recipes_recipe'),
    re_path(r'^ingredient/(?P<ingredient_name>[\s\w_\-0-9%\(\)]+)/(?P<slug>[A-Za-z_\-0-9]+)/$',
            IngredientView.as_view(), name='recipes_ingredient'),
    re_path(r'^category/(?P<category_name>[\s\w_\-0-9]+)$',
            CategoryView.as_view(), name='recipes_category'),
    re_path(r'^category/(?P<category_name>[\s\w_\-0-9]+)/(?P<page>\d+)/$',
            CategoryView.as_view(), name='recipes_category_page'),
    re_path(r'^tags/(?P<tags>[\s\w\,_\-0-9]+)$',
            TagsView.as_view(), name='recipes_tags'),
    re_path(r'^tags/(?P<tags>[\s\w\,_\-0-9]+)/(?P<page>\d+)/$',
            TagsView.as_view(), name='recipes_tags_page'),
    path('order_summary/',OrderSummaryView.as_view(),name='order_summary'),
    re_path(r'^remove-single-item-from-cart/(?P<recipe_name>[A-Za-z_\-0-9]+)/(?P<slug>[A-Za-z_\-0-9]+)$',remove_singe_item_from_cart,
            name = 'remove-single-item-from-cart'),
    path('payment/<payment_option>/',PaymentView.as_view(),name='payment'),
]
