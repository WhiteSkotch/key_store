from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from accounts.models import Game, Key, Transaction, Money
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.models import User
from django.contrib import messages

@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(game=game,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:detail')

def cart_add_1(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.add(game=game, quantity=1, update_quantity=False)
    return redirect('cart:detail')


def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect('cart:detail')


def cart_buy(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        money = Money.objects.filter(user=request.user).first()
        if not money:
            money = Money.objects.create(user=request.user, money=0)
        game_ids = cart.cart.keys()
        games = Game.objects.filter(id__in=game_ids)
        for item in cart:
            tran = Transaction()
            tran.user_id = request.user.id
            tran.game_id = item['game_id']
            keys = Key.objects.filter(game=tran.game_id, is_sold=False)
            if len(keys) < item['quantity']:
                messages.error(request, 'Not enough keys available for game {}'.format(tran.game_id))
                return redirect('cart:detail')
            for i in range(item['quantity']):
                tran.key = keys[i]
                tran.save()
                keys[i].is_sold = True
                keys[i].save()
                money.money -= item['price']
                money.save()
        cart.clear()
        messages.success(request, 'Thank you for your purchase!')
        return render(request, 'cart/detail.html', {'cart': cart})


def cart_detail(request):
    cart = Cart(request)
    print(request)
    print(cart)
    print(*[item for item in cart])
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

