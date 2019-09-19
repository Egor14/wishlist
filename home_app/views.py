from django.shortcuts import render, redirect
from .models import Wish
from django.views.decorators.http import require_POST, require_GET


@require_GET
def home_page(request):
    # SELECT * FROM home_app_wishes;
    wish_list = Wish.objects.all()
    return render(request, 'home_app/index.html', {'wish_list': wish_list})


@require_POST
def add_wish(request):
    # "INSERT INTO home_app_wishes(name, price, link, comment) VALUES(%s, %s, %s, %s);", [request.POST['name'],
    # price=request.POST['price'], request.POST['link'], request.POST['comment']]
    wish = Wish(name=request.POST['name'], price=request.POST['price'], link=request.POST['link'],
                comment=request.POST['comment'])
    wish.save()
    return redirect('/')


@require_GET
def drop_wish(request, id):
    # "DELETE FROM home_app_wishes WHERE id = %s;", [id]
    wish = Wish.objects.get(id=id)
    wish.delete()
    return redirect('/')
