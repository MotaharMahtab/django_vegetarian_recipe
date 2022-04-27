from distutils import log
from re import L
from django.contrib import messages
from venv import create
from django.shortcuts import redirect,render, get_object_or_404
from .models import BillingAddress, Recipe, Category, Tag, Ingredient, OrderItem,Order
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic.base import View, TemplateView
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse,reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

from . import appsettings
from .models import *


def products(request):
    context = {
        'items': Recipe.objects.all()
    }
    return render(request, "products.html", context)


class CheckoutView(View):
    def get(self,*args,**kwargs):
        form = CheckoutForm()
        
        context = {'form':form}
        return render(self.request,'checkout.html',context)

    def post(self,*args,**kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user = self.request.user,ordered=False)
            if form.is_valid():
            # print(form.cleaned_data)
            # print('Form is valid')
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                
                #to do
                # same_shipping_address = form.cleaned_data.get('same_shipping_address')
                # save_info = form.cleaned_data.get('save_info')

                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(user = self.request.user,
                                                street_address=street_address,apartment_address=apartment_address,
                                                country=country,zip=zip)
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # redirect to payment

                return redirect('core:checkout')           
        except ObjectDoesNotExist:
            messages.error(self.request,'You do ot have an acitve order')
            return redirect('core:order_summary')
        print(self.request.POST)
        
        messages.warning(self.request,'Failed Checkout')
        return redirect('core:checkout')

class PaymentView(View):
    def get(self,*args,**kwargs):
        return render(self.request,'payment.html')


class HomeView(ListView):
    model = Recipe
    template_name = 'home.html'
    paginate_by=4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('All recipes')
        context['seo_description'] = appsettings.SEO_DESCRIPTION
        context['seo_keywords'] = appsettings.SEO_KEYWORDS
        return context

    def get_queryset(self):
        recipes = Recipe.objects.all().order_by('-id') 
        recipes.base_url = ''
        return recipes

class ItemDetailView(DetailView):
    model = Recipe
    template_name = 'product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            recipe_name = self.kwargs['recipe_name']
            slug = self.kwargs['slug']
            # recipe = Recipe.objects.get(slug=slug)
            recipe = Recipe.objects.get(url=recipe_name,slug=slug)
            if self.request.user.has_perm('vegetarian_cookbook.change_recipe'):
                # admin can see drafts and ideas, users only published
                recipe = Recipe.objects.get(url=recipe_name)
            else:
                recipe = Recipe.objects.get(url=recipe_name, status=u'P')
        except Recipe.DoesNotExist:
            raise Http404("Recipe does not exist")
        context['recipe'] = recipe
        context['seo_description'] = recipe.recipe_ingredients(20, False, True)
        context['seo_keywords'] = recipe.recipe_tags() + ', ' \
            + appsettings.SEO_KEYWORDS
        return context

    
class IngredientView(TemplateView):
    """ ingredient page """
    template_name = "ingredient.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_name = self.kwargs['ingredient_name']
        slug = self.kwargs['slug']
        try:
            # ingredient = Ingredient.objects.get(slug=slug)
            ingredient = Ingredient.objects.get(name=ingredient_name,slug=slug)
            recipes = Recipe.objects.all().filter(
                Q(recipeingredient__ingredient__id=ingredient.id))
        except Recipe.DoesNotExist:
            raise Http404("Ingredient does not exist")
        context['ingredient'] = ingredient
        context['recipes'] = recipes
        context['seo_description'] = appsettings.SEO_DESCRIPTION + \
            ingredient_name
        context['seo_keywords'] = ingredient_name + ', ' + \
            appsettings.SEO_KEYWORDS
        return context    

class TagsView(ListView):
    """ tags page """
    model=Tag
    template_name = "list.html"
    paginate_by=1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.kwargs['tags']
        context['category_name'] = tags
        context['title'] = _('Tags: %(tags)s') % {'tags': tags}
        context['seo_description'] = appsettings.SEO_DESCRIPTION + \
            _('Tags: %(tags)s.') % {'tags': tags}
        context['seo_keywords'] = tags + ', ' + appsettings.SEO_KEYWORDS
        return context

    def get_queryset(self):
        tags = self.kwargs['tags']
        tags_list = tags.split(",")
        recipes = Recipe.objects.all().filter(
            Q(tags__name__in=tags_list)).distinct().order_by('-id')
        recipes.base_url = reverse('core:recipes_tags', args=[tags])
        return recipes

class CategoryView(ListView):
    """ category page """
    model=Category
    template_name = "list.html"
    paginate_by=1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs['category_name']
        category = Category.objects.get(name=category_name)
        context['category_name'] = category_name
        context['title'] = _('Category: %(category)s') % \
            {'category': category.name}
        context['seo_description'] = appsettings.SEO_DESCRIPTION + \
            _('Category: %(category)s.') % {'category': category.name}
        context['seo_keywords'] = category_name + ', ' \
            + appsettings.SEO_KEYWORDS
        return context

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        try:
            category = Category.objects.get(name=category_name)
            recipes = Recipe.objects.filter(
                category=category.id).order_by('-id')
        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        recipes.base_url = reverse('core:recipes_category', args=[category_name])
        return recipes


class OrderSummaryView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user = self.request.user,ordered=False)
            context = {'object':order}
            return render(self.request,'order_summary.html',context)
        except ObjectDoesNotExist:
            messages.error(self.request,'You do ot have an acitve order')
            return redirect('/')
        
@login_required
def add_to_cart(request, slug,recipe_name):
    item = get_object_or_404(Recipe, slug=slug,url = recipe_name)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug,item__url=item.url).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'You have added more of this product.')
            return redirect("core:order_summary")
        else:
            order_item.quantity=1
            order.items.add(order_item)
            messages.info(
                request, 'You have added this product to your current order.')
            return redirect("core:order_summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order_summary")

@login_required
def remove_from_cart(request, slug,recipe_name):
    item = get_object_or_404(Recipe, slug=slug,url=recipe_name)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug,item__url=item.url).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            print(OrderItem.objects.all())
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:recipes_recipe", slug=slug,recipe_name=recipe_name)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:recipes_recipe", slug=slug,recipe_name=recipe_name)

@login_required
def remove_singe_item_from_cart(request, slug,recipe_name):
    item = get_object_or_404(Recipe, slug=slug,url=recipe_name)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug,item__url=item.url).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity>1:
                order_item.quantity -=1
                order_item.save()
            else:
               order.items.remove(order_item)
               order_item.delete() 
            
            # print(OrderItem.objects.all())
            messages.info(request, "This item quantity was updated")
            return redirect("core:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:recipes_recipe", slug=slug,recipe_name=recipe_name)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:recipes_recipe", slug=slug,recipe_name=recipe_name)
