from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from .models import UserProfile

# Create your tests here.


class ProfileModelTestCase(TestCase):
    """
    Test profile model object creation
    """
    def setUp(self):
        self.user = User.objects.create_user(username='UserForTesting', password='12345')
        self.user_to_add = User(self.user)
        self.new_profile = UserProfile.objects.create(
            user=self.user_to_add.id,
            default_address_one="Test Address Line 1",
            default_address_two="Test Address Line 2",
            default_town_city="Test City",
            default_postcode="AA99 9AA",
            default_phone_number="07123123123",
            default_county="Test County",
            default_country="UK",
        )

    def test_user_exists_and_is_correct(self):
        users_count = UserProfile.objects.all().count()
        self.assertEqual(users_count, 1)
        self.assertEqual(self.new_profile.default_address_one, "Test Address Line 1")
        self.assertEqual(self.new_profile.default_address_two, "Test Address Line 2")
        self.assertEqual(self.new_profile.default_town_city, "Test City")


#     def test_product_price_default_is_699(self):
#         new_product = Product.objects.create(
#             flavour="Tasty Flavour V2",
#             description="Tasty Flavour Description V2",
#         )
#         self.assertEqual(new_product.price, "6.99")

#     def test_product_model_string_name(self):
#         self.assertEqual(str(self.product), "Flavour: Tasty Flavour")


# class NutritionModelTestCase(TestCase):
#     """
#     Test nutrition model object creation
#     """
#     def setUp(self):
#         self.product = Product.objects.create(
#             flavour="Tasty Flavour",
#             description="Tasty Flavour Description",
#             price=6.99
#         )
#         self.nutrition = Nutrition.objects.create(
#             product=self.product,
#             energy=400,
#             fat=10,
#             carbohydrate=10,
#             sugars=10,
#             protein=80,
#             salt=0.5
#         )

#     def test_nutrition_information(self):
#         self.assertEqual(self.nutrition.product, self.product)
#         self.assertEqual(self.nutrition.energy, 400)
#         self.assertEqual(self.nutrition.fat, 10)
#         self.assertEqual(self.nutrition.carbohydrate, 10)
#         self.assertEqual(self.nutrition.sugars, 10)
#         self.assertEqual(self.nutrition.protein, 80)
#         self.assertEqual(self.nutrition.salt, 0.5)

#     def test_nutrition_model_string_name(self):
#         self.assertEqual(str(self.nutrition), "Flavour: Tasty Flavour nutrition")

# class IngredientModelTestCase(TestCase):
#     """
#     Test ingredient model object creation
#     """
#     def setUp(self):
#         self.product = Product.objects.create(
#             flavour="Tasty Flavour",
#             description="Tasty Flavour Description",
#             price=6.99
#         )
#         self.nutrition = Nutrition.objects.create(
#             product=self.product,
#             energy=400,
#             fat=10,
#             carbohydrate=10,
#             sugars=10,
#             protein=80,
#             salt=0.5
#         )
#         self.ingredient_one = Ingredient.objects.create(
#             product=self.product,
#             name="Tasty Ingredient 1"
#         )
#         self.ingredient_two = Ingredient.objects.create(
#             product=self.product,
#             name="Tasty Ingredient 2"
#         )

#     def test_ingredient_information_number(self):
#         self.assertEqual(self.product.ingredient.all().count(), 2)

#     def test_ingredient_information_one(self):
#         self.assertEqual(self.product.ingredient.first().name, "Tasty Ingredient 1")

#     def test_ingredient_information_two(self):
#         self.assertEqual(self.product.ingredient.last().name, "Tasty Ingredient 2")

#     def test_ingredient_default_name(self):
#         ingredient_three = Ingredient.objects.create(
#             product=self.product,
#         )
#         self.assertEqual(self.product.ingredient.last().name, "You need an ingredient")

#     def test_ingredient_model_string_name(self):
#         self.assertEqual(str(self.ingredient_one), "ingredient - Flavour: Tasty Flavour ingredients")