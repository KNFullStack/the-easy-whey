from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
    )
from .models import Product, Nutrition, Ingredient
from .forms import (
    ProductForm,
    NutritionForm,
    IngredientEditForm,
    IngredientForm
    )

# Create your views here.


def index(request):
    """
    Returns the homepage
    """
    request.session['checkout_key'] = False
    return render(request, "products/index.html")


def product_detail(request):
    """
    Returns the product details page
    """
    request.session['checkout_key'] = False
    context = {
        "products": Product.objects.all(),
    }

    return render(request, "products/product_detail.html", context)


@login_required
@staff_member_required
def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")


@login_required
@staff_member_required
def admin_add(request):
    """
    View to add new product, nutrition or ingredients
    """
    product_form = ProductForm()
    nutrition_form = NutritionForm()
    ingredient_form = IngredientForm()

    template = 'products/admin_add.html'
    context = {
        "product_form": product_form,
        "nutrition_form": nutrition_form,
        "ingredient_form": ingredient_form,
    }

    if request.method == "POST":
        if "product_form_submit_button" in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added Product!")
                return redirect(reverse('admin_add'))
            else:
                messages.error(request,
                               "The form was not valid and therefore failed.")
                return redirect(reverse('admin_add'))

        if "nutrition_form_submit_button" in request.POST:
            form = NutritionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added Nutrition!")
                return redirect(reverse('admin_add'))
            else:
                messages.error(request,
                               "The form was not valid and therefore failed.")
                return redirect(reverse('admin_add'))

        if "ingredient_form_submit_button" in request.POST:
            form = IngredientForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added Ingredient!")
                return redirect(reverse('admin_add'))
            else:
                messages.error(request,
                               "The form was not valid and therefore failed.")
                return redirect(reverse('admin_add'))

    return render(request, template, context)


@login_required
@staff_member_required
def admin_edit_list(request):
    """
    Displays the list of products that can be selected to be edited
    """
    items = Product.objects.all()
    template = 'products/admin_edit_list.html'
    context = {"items": items}
    return render(request, template, context)


@login_required
@staff_member_required
def admin_edit_item_ingredient(request, item_id, ingredient_id):
    """
    View to edit a products ingredient
    """
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient_form = IngredientEditForm(instance=ingredient)

    if request.method == "POST":
        form = IngredientEditForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited ingredient!")
            return redirect(reverse('admin_edit_item', args=[item_id]))
        else:
            return redirect(reverse('product_management'))

    template = 'products/admin_edit_item_ingredient.html'
    context = {
        "ingredient_form": ingredient_form,
        "ingredient": ingredient
        }
    return render(request, template, context)


@login_required
@staff_member_required
def admin_edit_item(request, item_id):
    """
    View to edit a products information
    """
    item_product = False
    try:
        item_product = Product.objects.get(id=item_id)
    except Exception as error:
        messages.error(request, ('Sorry, there has been an error.'))
        return HttpResponse(content=error, status=400)

    item_nutrition = False
    try:
        item_nutrition = Nutrition.objects.filter(product_id=item_id)
    except Exception as error:
        messages.error(request, ('Sorry, there has been an error.'))
        return HttpResponse(content=error, status=400)

    item_ingredients = False
    try:
        item_ingredients = Ingredient.objects.filter(product__id=item_id)
    except Exception as error:
        messages.error(request, ('Sorry, there has been an error.'))
        return HttpResponse(content=error, status=400)

    template = 'products/admin_edit_item.html'
    items = Ingredient.objects.filter(product_id=item_id)
    product_id = item_id

    context = {
        "items": items,
        "product_id": product_id,
        }

    ingredient_forms = []
    if item_product:
        product_form = ProductForm(instance=item_product)
        context["product_form"] = product_form
    if item_nutrition:
        nutrition_form = NutritionForm(instance=item_nutrition.first())
        context["nutrition_form"] = nutrition_form
    if item_ingredients:
        for ingredient in item_ingredients:
            ingredient_forms.append(IngredientForm(instance=ingredient))

    context["ingredient_forms"] = ingredient_forms

    if request.method == "POST":
        if "product_form_edit_button" in request.POST:
            form = ProductForm(request.POST, instance=item_product)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
        if "nutrition_form_edit_button" in request.POST:
            form = NutritionForm(request.POST, instance=item_nutrition.first())
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
        if "ingredients_form_edit_button" in request.POST:
            form = IngredientForm(request.POST, instance=item_ingredients)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))

    return render(request, template, context)


@login_required
@staff_member_required
def admin_delete(request, item_id):
    """
    view to delete product
    """
    item = get_object_or_404(Product, id=item_id)
    item.delete()
    messages.success(request, "Successfully deleted Product!")
    return redirect(reverse('product_management'))


@login_required
@staff_member_required
def delete_ingredient(request, ingredient_id):
    """
    view to delete an ingredient
    """
    item = get_object_or_404(Ingredient, id=ingredient_id)
    item.delete()
    messages.success(request, "Successfully deleted ingredient!")
    return redirect(reverse('admin_edit_list'))
