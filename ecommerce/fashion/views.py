from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import Fashion

# Create your views here.
def fashion(request):
    fashion=Fashion.objects.all()
    return render(request,"fashion.html",{"fn":fashion})

def fashion_add(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        # Create a new electronic
        Fashion.objects.create(
        name=name,
        price=price,
        brand=brand
        )
 # Redirect to the student list after saving
        return redirect('fashion')
    return render(request, 'addfashion.html')

def fashion_edit(request, pk):
    # Fetch the Electronics by primary key (ID)
    fashion = get_object_or_404(Fashion, pk=pk)
    if request.method == 'POST':
        # Update the student details
        fashion.name = request.POST.get('name')
        fashion.price = request.POST.get('price')
        fashion.brand= request.POST.get('brand')
        fashion.save() # Save changes to the database
        return redirect('fashion')
    # Render the form with existing data
    return render(request, 'addfashion.html', {'fashion': fashion})

def fashion_delete(request, pk):
    # Fetch the student by primary key (ID)
    fashion = get_object_or_404(Fashion, pk=pk)
    if request.method == 'POST':
        fashion.delete() # Delete the student record
        return redirect('fashion')
 # Render the delete confirmation page
    return render(request, 'deletefashion.html', {'fashion': fashion})