from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.models import Money, Transaction
from .forms import AddMoneyForm
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django import forms
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@receiver(post_save, sender=User)
def create_money(sender, instance, created, **kwargs):
    if created:
        print('Creating Money object for user', instance.username)
        Money.objects.create(user=instance, money=0)


@login_required
def home(request):
    user = request.user
    money = Money.objects.get(user=user)
    transactions = Transaction.objects.filter(user=user)
    context = {'money': money.money, 'transactions': transactions}
    print(money.money)
    print(user.balance.all()[0].money)
    return render(request, 'lk.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def get_money(request):
    return redirect(reverse_lazy('home'))


@login_required
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
            return render(request, 'lk.html', {'money': balance})
        else:
            form = AddMoneyForm()
        return render(request, 'lk.html', {'form': form, 'money': balance})


def add_money_to_user(user, amount):
    money, created = Money.objects.get_or_create(user=user)
    amount_decimal = Decimal(amount)
    if amount_decimal>=0:
        money.money += amount_decimal
    money.save()


def add_money(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        user = request.user
        add_money_to_user(user, amount)
        money = Money.objects.get(user=request.user)
        context = {'money': money.money}
        return redirect(reverse_lazy('home'))
    else:
        return redirect(reverse_lazy('home'))


def get_trans(request):
    transactions = Transaction.objects.filter(user=request.user)
    context1 = {'transactions': transactions}
    redirect(reverse_lazy('home'), context1)