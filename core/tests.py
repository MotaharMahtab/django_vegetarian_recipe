from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from core.models import *

class BaseTest(TestCase):
    def setUp(self):
        self.signupuser_url=reverse('core:signupuser')
        self.loginuser_url=reverse('core:loginuser')
        self.user={
            'username':'username',
            'password1':'password',
            'password2':'password',
            'password':'password'
        }
        self.user_unmatching_password={

            'username':'username',
            'password1':'password1',
            'password2':'password2',
            'password':'password'
        }
        
        return super().setUp()

class SignUpUserTest(BaseTest):
   def test_user_can_view_page_correctly(self):
       response=self.client.get(self.signupuser_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'signupuser.html')


   def test_user_can_register(self):
       response = self.client.post(self.signupuser_url, self.user, format='text/html')
       self.assertEqual(response.status_code, 302)



def test_user_cant_register_with_taken_username(self):
        self.client.post(self.signupuser_url,self.user,format='text/html')
        response=self.client.post(self.signupuser_url,self.user,format='text/html')
        self.assertEqual(response.status_code,400) 



def test_user_cant_register_with_unmatched_passwords(self):
        response=self.client.post(self.signupuser_url,self.user_unmatching_password,format='text/html')
        self.assertEqual(response.status_code,400)   

        
            


class LoginTest(BaseTest):
    def test_user_can_access_login_page(self):
        response=self.client.get(self.loginuser_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'loginuser.html')



    def test_user_can_login_successfully(self):
        self.client.post(self.signupuser_url,self.user,format='text/html')
        user=User.objects.filter(username=self.user['username']).first()
        user.is_active=True
        user.save()
        response= self.client.post(self.loginuser_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302) 



    def test_user_cant_login_without_username(self):
        response= self.client.post(self.loginuser_url,{'password':'passwped','username':''},format='text/html')
        self.assertEqual(response.status_code,200)


    
    def test_user_cant_login_without_password(self):
        response= self.client.post(self.loginuser_url,{'username':'username','password':''},format='text/html')
        self.assertEqual(response.status_code,200)

class RecipeMethodTests(BaseTest):
    """ Test recipe methods """
    def test_calculate(self):
        """
        test calculate energy and nutrients
        """
        self.client.post(self.signupuser_url,self.user,format='text/html')
        user=User.objects.filter(username=self.user['username']).first()
        recipe = Recipe(price=100,owner=user)
        recipe.calculate()
        self.assertEqual(recipe.energy, 0)

        recipe = Recipe(weight=100,price=100,owner=user)
        recipe.calculate()
        self.assertEqual(recipe.energy, 0)

        category = Category(name='Cat1')
        category.save()
        recipe = Recipe(category=category,price=100,owner=user)
        recipe.save()
        ingredient = Ingredient(name='test1', energy=100,
                                protein=1, fat=2, carbohydrate=3)
        ingredient.save()
        recipeingredient = RecipeIngredient(recipe=recipe,
                                            ingredient=ingredient, weight=100)
        recipeingredient.save()
        recipe.calculate()
        self.assertEqual(recipe.energy, 100)
        self.assertEqual(recipe.protein, 1)
        self.assertEqual(recipe.fat, 2)
        self.assertEqual(recipe.carbohydrate, 3)

        ingredient = Ingredient(name='test2', energy=300,
                                protein=5, fat=10, carbohydrate=15)
        ingredient.save()
        recipeingredient = RecipeIngredient(recipe=recipe,
                                            ingredient=ingredient, weight=300)
        recipeingredient.save()
        recipe.calculate()
        self.assertEqual(recipe.energy, 250)
        self.assertEqual(recipe.protein, 4)
        self.assertEqual(recipe.fat, 8)
        self.assertEqual(recipe.carbohydrate, 12)