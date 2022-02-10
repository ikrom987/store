from django.shortcuts import render, redirect

from .models import *


######################################################################
# INDEX
######################################################################


def control_index(request):
    context = {

    }
    return render(request, "control/index/index.html", context)


######################################################################
# CATEGORY
######################################################################

def category_add(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code
    }
    return render(request, "control/category/add.html", context)


def category_all(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "code": code,
    }
    return render(request, "control/category/all.html", context)


def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "category": category,
        "code": code
    }
    return render(request, "control/category/detail.html", context)


def category_create(request):
    if request.method == "POST": 
        arr = list(map(lambda x: x.title.lower(), Category.objects.all()))
        if request.POST["category_title"].lower() not in arr:
            Category.objects.create(
                title = request.POST["category_title"],
                priority = request.POST["category_priority"]
            )
            return redirect("/control/category/all/?create")
        else:
            return redirect("/control/category/add/?title")


def category_edit(request):
    if request.method == 'POST':
        c = Category.objects.get(id=request.POST['id'])
        arr = list(map(lambda x: x.title.lower(), Category.objects.all()))      
        if request.POST["category_title"].lower() == c.title.lower():
            c.priority = request.POST['category_priority']
            c.save()
            return redirect("/control/category/all/?edit")
        elif request.POST["category_title"].lower() not in arr:
            c.title = request.POST['category_title']
            c.priority = request.POST['category_priority']
            c.save()
            return redirect("/control/category/all/?edit")
        else:
            return redirect("/control/category/detail/{}/?title".format(c.slug))


def category_delete(request):
    if request.method == "POST":
        c = Category.objects.get(id=request.POST['id'])
        c.delete()
    return redirect("/control/category/all/?delete")


######################################################################
# PRODUCTS
######################################################################

def product_add(request):
    categories = Category.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        'categories': categories,
        "code": code
    }
    return render(request, "control/product/add.html", context)

def product_create(request):
    if request.method == 'POST' and request.FILES['file']:
        arr = list(map(lambda x: x.title.lower(), Product.objects.all()))
        if request.POST["title"].lower() not in arr:
            Product.objects.create(
                priority = request.POST['priority'],
                title = request.POST['title'],
                price = request.POST['price'],
                description = request.POST['description'],
                category_id = request.POST['category'],
                image_min = request.FILES['file'],
                image_max = request.FILES['file'],
            )
            return redirect('/control/product/all/?create/product')
        else:
            return redirect("/control/product/add/?title/product")

def product_all(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    products = Product.objects.all()
    context = {
        "products": products,
        "code": code
    }
    return render(request, "control/product/all.html", context)

def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    categories = Category.objects.all()
    context = {
        "product": product,
        "categories": categories,
        "code": code
    }
    return render(request, "control/product/detail.html", context)

def product_edit(request):
    if request.method == 'POST' or request.FILES['file']:
        p = Product.objects.get(id=request.POST['id'])
        arr = list(map(lambda x: x.title.lower(), Product.objects.all()))
        if request.POST["title"].lower() == p.title.lower():
            p.priority = request.POST['priority']
            p.price = request.POST['price']
            p.description = request.POST['description']
            p.category_id = request.POST['category']
            try:
                p.image_min = request.FILES['file']
                p.image_max = request.FILES['file']
            except:
                pass
            p.save()
            return redirect('/control/product/all/?edit/product')
        elif request.POST["title"].lower() not in arr:
            p.title = request.POST['title']
            p.priority = request.POST['priority']
            p.price = request.POST['price']
            p.description = request.POST['description']
            p.category_id = request.POST['category']
            try:
                p.image_min = request.FILES['file']
                p.image_max = request.FILES['file']
            except:
                pass
            p.save()
            return redirect('/control/product/all/?edit/product')
        else:
            return redirect('/control/product/detail/{}/?title/product'.format(p.slug))


def product_delete(request):
    if request.method == "POST":
        p = Product.objects.get(id=request.POST['id'])
        p.delete()
    return redirect("/control/product/all/?delete/product")



