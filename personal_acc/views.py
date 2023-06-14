from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.models import Money
from .forms import AddMoneyForm
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import logout


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@receiver(post_save, sender=User)
def create_money(sender, instance, created, **kwargs):
    if created:
        print('Creating Money object for user', instance.username)
        Money.objects.create(user=instance, money=0)


def home(request):
    return render(request, 'lk.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def get_money(request):
    user = request.user
    money = Money.objects.get(user=user)
    context = {'money': money.money}
    return render(request, 'lk.html', context)


def add_money_view(request):
    user = request.user
    money, created = Money.objects.get_or_create(user=user)
    balance = money.money
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            add_money_to_user(user.id, amount)
            balance += amount
            return render(request, 'success.html', {'balance': balance})
        else:
            form = AddMoneyForm()
        return render(request, 'lk.html', {'form': form, 'balance': balance})


def add_money_to_user(user, amount):
    money, created = Money.objects.get_or_create(user=user)
    amount_decimal = Decimal(amount)
    money.money += amount_decimal
    money.save()


def add_money(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        user = request.user
        add_money_to_user(user, amount)
        money = Money.objects.get(user=request.user)
        context = {'money': money.money}
        return render(request, 'lk.html', context)
    else:
        return render(request, 'lk.html')