from http.client import PAYMENT_REQUIRED
from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from ckeditor.widgets import CKEditorWidget
from .models import *
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class IngredientForm(ModelForm):
    """ Ingredient form - enable CKEditor for description """
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Ingredient
        exclude = []


class RecipeIngredientInlineForm(ModelForm):
    """ recipe ingredient inline form - added validate """
    def clean(self):
        ingredient = self.cleaned_data.get('ingredient')
        quantity = self.cleaned_data.get('quantity')
        unit = self.cleaned_data.get('unit')
        weight = self.cleaned_data.get('weight')
        try:
            quantity = float(quantity)
        except TypeError:
            raise forms.ValidationError(_('Quantity must be float'))
        if quantity > 0 and not unit:
            raise forms.ValidationError(
                _('You not set unit for this ingredient'))
        if quantity > 0 and unit and ingredient:
            try:
                ingredient_unit = IngredientUnit.objects.get(
                    unit=unit,
                    ingredient=ingredient)
                weight = int(quantity * float(ingredient_unit.ratio))
            except IngredientUnit.DoesNotExist:
                url = reverse('admin:vegetarian_cookbook_ingredient_change',
                              args=(ingredient.id,))
                ing_link = '<a  target="_blank" href="{}">{}</a>'.format(
                    url, ingredient.name)
                message = _('You did not set ratio for this ingredient and unit.'
                            'Please edit {} property'.format(ing_link))
                raise forms.ValidationError(format_html(message))
        if not weight:
            raise forms.ValidationError(_('Zero weight for this ingredient'))
        return self.cleaned_data

    class Meta:
        model = RecipeIngredient
        exclude = []


class RecipeForm(ModelForm):
    """ Recipe form - enable CKEditor for description """
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Recipe
        exclude = []
        # labels = {
        #     'category': '',
        #     'complexity': '',
        #     'generate_url': '',
        # }
        labels = {
            'generate_url': '',
        }

PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('B', 'Bkash')
)
class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'1234 Main St'}))
    apartment_address = forms.CharField(required = False,
    widget=forms.TextInput(attrs={'placeholder':'Apartment or Suite'}))
    country = CountryField(blank_label='(select country)').formfield(widget = CountrySelectWidget(attrs={'class':'custom-select d-block w-100'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),
                                        choices = PAYMENT_CHOICES)
