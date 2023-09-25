from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import SellerSignUpForm, ItemForm
from .models import Seller, Customer, Item, Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    return render(request, "main/home.html")

def logout_view(request):
    logout(request)
    return redirect('home')


def seller_signup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            seller = Seller.objects.create(user=user)
            seller.address = form.cleaned_data.get('address')
            seller.email = form.cleaned_data.get('email')
            seller.phone = form.cleaned_data.get('phone')
            seller.save()
            return redirect('/')
    else:
        form = SellerSignUpForm()

    return render(request, 'registration/seller_signup.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    

class ItemFormView(LoginRequiredMixin,CreateView):
    form_class = ItemForm
    model = Item
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
    

def seller_items(request):
    seller = Seller.objects.get(id=request.user.seller.id)
    items = Item.objects.filter(seller=seller)
    return render(request, 'main/inventory.html', {"items":items})