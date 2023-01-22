from django.shortcuts import render, redirect
from .models import Service, Category, Portfolio, Comparison
from .forms import ServiceForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    service = Service.objects.all()
    context = {'service':service}
    return render(request, 'index.html', context)

def services(request):
    services = Service.objects.all()
    categories = Category.objects.all()
    context ={'services':services, 'categories':categories}
    return render(request, "services/services.html", context)

@login_required(login_url='login')
def createService(request):
    form = ServiceForm()

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')

    context ={'form':form}
    return render(request, "services/service_form.html", context)

@login_required(login_url='login')
def updateService(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():

            form.save()
            return redirect('services')

    context = {'form':form, 'image':service.image}
    return render(request, "services/service_form.html", context)

@login_required(login_url='login')
def deleteService(request, pk):
    service = Service.objects.get(id=pk)

    if request.method == "POST":

        service.delete()

        return redirect('services')
    
    context = {'object':service}
    return render (request, 'delete_template.html', context)

def viewService(request, pk):
    service = Service.objects.get(id=pk)
    
    context = {'service':service}
    return render (request, 'services/service_view.html', context)

@login_required(login_url='login')
def createCategory(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category-list")

    context = {'form':form}
    return render (request, 'services/category_form.html', context)

@login_required(login_url='login')
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("services")

    context = {'form':form}
    return render (request, "services/category_form.html", context)

@login_required(login_url='login')
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    
    if request.method == "POST":
        category.delete()
        return redirect('category-list')

    context = {'object':category}
    return render (request, 'delete_template.html', context)

@login_required(login_url='login')
def categoryList (request):
    categories = Category.objects.all()

    context = {"categories":categories}
    return render (request, 'services/category_list.html', context)

def viewPortfolio(request, pk):
    service = Service.objects.get(id=pk)
    portfolio = service.portfolio_set.all()


# Beginning of paginator logic
    page = request.GET.get('page')
    results = 8
    paginator =Paginator(portfolio, results)

    try:
        portfolio = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        portfolio = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
# End of Paginator logic


    custom_range = range(leftIndex, rightIndex)

    context = {"service":service, "portfolio":portfolio, 'paginator':paginator, 'custom_range':custom_range}
    return render (request, 'services/service_portfolio.html', context)
