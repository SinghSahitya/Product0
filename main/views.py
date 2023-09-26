from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import SellerSignUpForm, ItemForm, NewSaleForm, NewCustomerForm
from .models import Seller, Customer, Item, Order
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    try: 
        seller = Seller.objects.get(id=request.user.seller.id)
        customers = Customer.objects.filter(seller=seller)
        return render(request, "main/customer.html", {"customers":customers})
    except:
        return render(request, 'main/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def sales(request):
    seller = Seller.objects.get(id=request.user.seller.id)
    orders = Order.objects.filter(seller=seller)
    return render(request, "main/sales.html", {"orders":orders})




class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    

class ItemFormView(LoginRequiredMixin,CreateView):
    form_class = ItemForm
    model = Item
    success_url = reverse_lazy('inventory')

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
    
@login_required
def seller_items(request):
    seller = Seller.objects.get(id=request.user.seller.id)
    items = Item.objects.filter(seller=seller)
    return render(request, 'main/inventory.html', {"items":items})


def new_sale(request):
    seller = Seller.objects.get(id=request.user.seller.id)  # Assuming you're using the user's session
    items = Item.objects.filter(seller=seller)
    customers = Customer.objects.filter(seller=seller)

    if request.method == 'POST':
        form = NewSaleForm(seller, request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.seller = seller
            if order.item.decrease_units(order.quantity):  # Call the decrease_units method
                order.save()
                return redirect('sales')  # Redirect to the sales list view
            else:
                form.add_error('quantity', 'Not enough available units.')

    else:
        form = NewSaleForm(seller)

    return render(request, 'main/new_sale.html', {'form': form, 'items': items, 'customers': customers})

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

def new_customer(request):
    seller = Seller.objects.get(id=request.user.seller.id)
    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.seller = seller
            customer.save()
            return redirect('home')
    else:
        form = NewCustomerForm()

    return render(request, 'main/new_customer.html', {'form':form})
