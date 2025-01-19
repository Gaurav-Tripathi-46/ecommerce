from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Grocery

# Create your views here.
def grocery(request):
    grocery=Grocery.objects.all()
    return render(request,"grocery.html",{"groc":grocery})

def grocery_add(request):
    if request.method == 'POST':
        # Sno = request.POST.get('Sno')
        item = request.POST.get('item')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        # Create a new electronic
        Grocery.objects.create(
        # Sno=Sno,
        item=item,
        price=price,
        quantity=quantity
        )
        return redirect('grocery')
    return render(request, 'addgrocery.html')


def grocery_edit(request, pk):
    # Fetch the grocery item by primary key (ID)
    grocery_item = get_object_or_404(Grocery, pk=pk)
    if request.method == 'POST':
         # grocery_item.Sno = request.POST.get('Sno')
        grocery_item.item = request.POST.get('item')  # Ensure item is set
        grocery_item.price = request.POST.get('price')
        grocery_item.quantity = request.POST.get('quantity')
        grocery_item.save()  # Save changes to the database
        return redirect('grocery')
    return render(request, 'addgrocery.html', {'grocery': grocery_item})



from django.shortcuts import get_object_or_404, redirect, render

def grocery_delete(request, pk):
    # Fetch the grocery item by primary key (ID)
    grocery_item = get_object_or_404(Grocery, pk=pk)  # Use a distinct variable name
    if request.method == 'POST':
        grocery_item.delete()  # Delete the grocery record
        return redirect('grocery')
    # Render the delete confirmation page
    return render(request, 'deletegrocery.html', {'grocery': grocery_item})

