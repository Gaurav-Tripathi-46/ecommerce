from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from .models import Electronics

# Create your views here.
def electronics(request):
    electronics =Electronics.objects.all()
    return render(request,"electronics.html",{"elec":electronics})

def home(request):
    return render(request,"home.html")


def electronics_add(request):
    if request.method == 'POST':
        # Extract data from the form
        Sid = request.POST.get('Sid')
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        # Create a new electronic
        Electronics.objects.create(
        Sid=Sid,
        name=name,
        price=price,
        desc=desc
        )
 # Redirect to the student list after saving
        return redirect('electronics')
    return render(request, 'add.html')

def electronics_edit(request, pk):
    # Fetch the Electronics by primary key (ID)
    electronics = get_object_or_404(Electronics, pk=pk)
    if request.method == 'POST':
        # Update the student details
        electronics.Sid = request.POST.get('Sid')
        electronics.name = request.POST.get('name')
        electronics.price = request.POST.get('price')
        electronics.desc= request.POST.get('desc')
        electronics.save() # Save changes to the database
        return redirect('electronics')
    # Render the form with existing data
    return render(request, 'add.html', {'electronics': electronics})

def electronics_delete(request, pk):
    # Fetch the student by primary key (ID)
    electronics = get_object_or_404(Electronics, pk=pk)
    if request.method == 'POST':
        electronics.delete() # Delete the student record
        return redirect('electronics')
 # Render the delete confirmation page
    return render(request, 'delete.html', {'electronics': electronics})
