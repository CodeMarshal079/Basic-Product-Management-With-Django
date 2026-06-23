from django.shortcuts import render, redirect
from T_RelationApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Register
def registerPage(request):
    if request.method =="POST":
        username =request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        user_type = request.POST.get('user_type')
        
        user_exists =UserModel.objects.filter(username=username).exists()
        email_exists =UserModel.objects.filter(email=email).exists()
        
        if user_exists or email_exists:
            return  HttpResponse('User name/email already exists')
        if password == confirmpassword:
            UserModel.objects.create_user(
                username = username,
                email= email,
                first_name = f_name,
                password=password,
                user_type=user_type
            ) 
            return redirect ('login')
    return render (request, 'auth/register.html')
# Log in
def loginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return redirect('dashboard')
    return render (request, 'auth/login.html')
# logout

def logoutPage(request):
    logout(request)
    return redirect('register')

# dashboard
@login_required
def dashboardPage(request):
    p_data = ProductModel.objects.all()
    con = {
        'p_data': p_data}
    return render(request, 'pages/dashboard.html', con)

# Category
def addCategory(request):
    if request.method=="POST":
        category_name =request.POST.get('category')
        CategoryModel.objects.create(
            name =category_name
        ) 
        return redirect('category')
    return render (request, 'pages/addcategory.html')

# add product
def addProductPage(request):
    category =CategoryModel.objects.all()
    if request.method =="POST":
        name = request.POST.get('p_name')
        category_id =request.POST.get('category')
        price = request.POST.get('p_price')
        description = request.POST.get('p_description')
        image = request.FILES.get('p_image')
        
        ProductModel.objects.create(
            name =name,
            category_id =category_id,
            price =price,
            description =description,
            image =image
        ) 
        return redirect('dashboard')
    
    con={
        'catdata':category
    }
    return render (request, 'pages/addProduct.html', con)
# Product Edit
def productEdit(request, id):
    get_data = ProductModel.objects.get(id=id)

    if request.method == "POST":
        get_data.name = request.POST.get('name')
        get_data.price = request.POST.get('price')
        get_data.description = request.POST.get('description')
        get_data.category_id = request.POST.get('category')

        if request.FILES.get('image'):
            get_data.image = request.FILES.get('image')

        get_data.save()
        
        return redirect('dashboard')

    con = {
        'data': get_data
    }
    return render(request, 'pages/editpro.html', con)

# Product Delete
def productDelete(request,id):
    ProductModel.objects.get(id=id).delete()
    return redirect('dashboard')
    
# Order Page
def orderPage(request,id):
    if request.method =="POST":
        product = ProductModel.objects.get(id=id)
        
        OrderModel.objects.create(
            product =product,
            status ='pending',
            user =request.user
        )
        return redirect('orderlist')
    return redirect('dashboard')

# ViewPage

def viewPage(request,id):
    viewData = ProductModel.objects.get(id=id)
    if request.method =="POST":
        quantity =int(request.POST.get('quantity', 1))
        total =viewData.price * quantity
        
        OrderModel.objects.create(
            user =request.user,
            product=viewData,
            quantity=quantity,
            total =total,
            status = 'pending'
        )
        return redirect('orderList')
    con ={
        'data': viewData}
    return render (request, 'pages/viewproduct.html',con)

def orderListPage(request):
    if request.user.user_type == 'admin':
        user_order = OrderModel.objects.all()
    else:
        user_order = OrderModel.objects.filter(user=request.user)
        
    con = {
        'orderData': user_order
    }
    return render(request, 'pages/orderList.html', con)

def orderDelete(request, id):
    OrderModel.objects.get(id=id).delete()
    return redirect('orderList')