from django.shortcuts import render, redirect
from .models import Item
from django.views.generic import DetailView
from .forms import OrderForm


def index(req):
    items = Item.objects.all()
    data = {
        'items': items
    }

    response = render(req, 'main/index.html', data)
    if req.GET.get('id') is None:
        pass
    else:
        cookie = req.COOKIES.get('favorite')
        if cookie:
            response.set_cookie('favorite', cookie + req.GET.get('id') + ',', 60 * 60 * 24 * 30)
        else:
            response.set_cookie('favorite', req.GET.get('id') + ',', 60 * 60 * 24 * 30)

    return response


class ItemsDetailView(DetailView):
    model = Item
    template_name = 'main/details_view.html'
    context_object_name = 'item'


def buy(req, pk):
    error = ''
    id_of_item = req.GET['id']
    if req.method == 'POST':
        form = OrderForm(req.POST, id_of_item=id_of_item)
        if form.is_valid():
            form.save()

            trash_item = id_of_item

            cookie = req.COOKIES.get('cart')
            if cookie:
                arr = cookie.split(',')
                if arr[-1] == '':
                    arr.pop(-1)

                product_exist = False
                for i in arr:
                    product_exist = i == id_of_item

                if product_exist:
                    arr.remove(trash_item)

                    c = ','.join(arr)

                    response = render(req, 'main/bought.html')
                    if c == '':
                        response.delete_cookie('cart')
                    else:
                        response.set_cookie('cart', c + ',', 60 * 60 * 24 * 30)

                    return response
                else:
                    return render(req, 'main/bought.html')
            else:
                return render(req, 'main/bought.html')
        else:
            error = 'Форма неправильно заполнена'

    item = Item.objects.get(id=id_of_item)

    form = OrderForm(id_of_item=id_of_item)

    data = {
        'form': form,
        'id_of_item': id_of_item,
        'name_of_item': item.name,
        'category_of_item': item.category,
        'price_of_item': item.price,
        'error': error
    }

    return render(req, 'main/items_buy.html', data)


def buy_all(req):
    cookie = req.COOKIES.get('cart')

    arr = cookie.split(',')
    if arr[-1] == '':
        arr.pop(-1)

    products = []
    for i in arr:
        products += [Item.objects.get(id=i)]

    id_of_items = ''
    for i in products:
        i.id = str(i.id)
        id_of_items += i.id + ', '
    id_of_items = id_of_items[:-1]
    id_of_items = id_of_items[:-1]

    error = ''
    if req.method == 'POST':
        form = OrderForm(req.POST, id_of_item=products)
        if form.is_valid():
            form.save()
            return redirect('bought_all')
        else:
            error = 'Форма неправильно заполнена'

    form = OrderForm(id_of_item=products)   # сюда передаем все id и обрабатываем в форме

    name = ''
    for a in products:
        name += a.name + ', '
    name = name[:-1]
    name = name[:-1]

    category = ''
    for j in products:
        category += j.category + ', '
    category = category[:-1]
    category = category[:-1]

    price = 0
    for k in products:
        price += k.price

    data = {
        'form': form,
        'id_of_item': id_of_items,
        'name_of_item': name,
        'category_of_item': category,
        'price_of_item': price,
        'error': error
    }

    return render(req, 'main/buy_all.html', data)


def bought_all(req):
    response = render(req, 'main/bought_all.html')
    response.delete_cookie('cart')
    return response


def order(req):
    response = render(req, 'main/order.html')

    cookie = req.COOKIES.get('cart')
    if cookie:
        response.set_cookie('cart', cookie + req.GET['id'] + ',', 60 * 60 * 24 * 30)
    else:
        response.set_cookie('cart', req.GET['id'] + ',', 60 * 60 * 24 * 30)

    return response


def cart(req):
    cookie = req.COOKIES.get('cart')

    if cookie is not None:
        arr = cookie.split(',')
        if arr[-1] == '':
            arr.pop(-1)

        products = []
        for i in arr:
            products += [Item.objects.get(id=i)]

        data = {
            'products': products,
            'cookie': cookie
        }
    else:
        data = {

        }

    return render(req, 'main/cart.html', data)


def favorite(req):
    cookie = req.COOKIES.get('favorite')

    if cookie is not None:
        arr = cookie.split(',')
        if arr[-1] == '':
            arr.pop(-1)

        products = []
        for i in arr:
            products += [Item.objects.get(id=i)]

        products = list(set(products))

        data = {
            'products': products,
            'cookie': cookie
        }
    else:
        data = {

        }

    return render(req, 'main/favorite.html', data)


def trash_favorite(req):
    trash_item = req.GET['id']

    cookie = req.COOKIES.get('favorite')
    arr = cookie.split(',')

    while trash_item in arr:
        arr.remove(trash_item)

    c = ','.join(arr)

    response = render(req, 'main/trash_favorite.html')

    response.set_cookie('favorite', c, 60 * 60 * 24 * 30)

    return response


def trash(req):
    trash_item = req.GET['id']

    cookie = req.COOKIES.get('cart')
    arr = cookie.split(',')

    response = render(req, 'main/trash.html')

    if trash_item in arr:
        arr.remove(trash_item)

        c = ','.join(arr)

        response.set_cookie('cart', c, 60 * 60 * 24 * 30)

    return response


def profile(req):
    return render(req, 'main/profile.html')


# categories

def notebooks_and_accessories(req):
    items = Item.objects.filter(category='Ноутбуки и аксессуары')

    return render(req, 'main/notebooks_and_accessories.html', {'items': items})


def smartphones_tv_electronics(req):
    items = Item.objects.filter(category='Смартфоны, ТВ и электроника')

    return render(req, 'main/smartphones_tv_electronics.html', {'items': items})


def search_results(req):
    search = req.GET['search']

    items = Item.objects.filter(name__icontains=search)

    return render(req, 'main/search.html', {'items': items, 'search': search})
