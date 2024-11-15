from django.shortcuts import render,redirect
from .models import watches,watchUploads,wishlist,cart,CartItem
from .forms import UploadForm
from django.contrib.auth.decorators import login_required

# This is array to create the cards manually

# sample_watches=[{"name":"watch_name","description":"descrption here","price":5000},
#          {"name":"watch_name1","description":"descrption here","price":5000},
#          {"name":"watch_name2","description":"descrption here","price":5000},
#          ]

# Create your views here.

# This function is for home page
def Home(request):
    watches_list = watchUploads.objects.all()  # To Retrieve all instances from the watches model
    context = {'watches_t': watches_list}
    return render(request,'home.html',context)


# This function is for about page
def About(request):
    return render(request,'about.html')


# This function is for upload image page
@login_required(login_url='/login')
def Upload(request):
    if request.method=='POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
            form=UploadForm()\



    return render(request,'WatchUpload.html',{'form':form})



from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout


# for login
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = user_name, password = password)
            
            if user is not None:
                 login(request,user)
                 return redirect('home') 
            else:
                return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form': form})


# for signup

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



#for logout

def log_out(request):
     logout(request)
     return redirect('home')




#for display product
from django.shortcuts import get_object_or_404
def show_product(request,id):
    product= get_object_or_404(watchUploads, id=id)
    return render(request,'product.html',{"product":product})

     
#for wishlisting the watches
def Addtowishlist(request, id):
    user = request.user
    product = watchUploads.objects.get(id=id)
    obj1, created  = wishlist.objects.get_or_create(user=user)
    obj1.product.add(product)
    obj1.save()
    return redirect('home')

#for showing the products in wishlist

def show_wishlist(request):
    user = request.user
    wish_object = wishlist.objects.get(user= user)
    return render(request, "wishlist.html", {"user_products": wish_object.product.all()})


   # for removing the product from wishlist     
def removewish(request, id):
    product_rm = watchUploads.objects.get(id=id)
    wish_obj = wishlist.objects.get(user=request.user)
    wish_obj.product.remove(product_rm)
    return render(request, 'wishlist.html', {"user_products": wish_obj.product.all()})


def addtocart(request, id):
     user_cart, created = cart.objects.get_or_create(user = request.user)
     product = watchUploads.objects.get(id=id)
     cart_item, created = CartItem.objects.get_or_create(user = user_cart, product= product )
     cart_item.product= product
     cart_item.save()

     return redirect('home')


def show_cart(request):
    user_cart, created = cart.objects.get_or_create(user = request.user)
    cart_objects = user_cart.cartitem_set.all()
    return render(request, "cart.html", {"user_products": cart_objects})

    
def removeCart(request, id):
    product_rm = watchUploads.objects.get(id=id)
    cart_obj = cart.objects.get(user=request.user)
    cart_obj.product.remove(product_rm)
    return render(request, 'cart.html', {"user_products": cart_obj.product.all()}) 