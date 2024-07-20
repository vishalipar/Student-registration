from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import mainForm
from .models import User


def home(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        location = request.POST.get('location')
        user = User(name=name,email=email, mobile=mobile, age=age, location=location)
        user.save()
        return render(request, 'home.html')
        
        
    else:
        form = mainForm()
    return render(request, 'home.html')


def students(request):
    students = User.objects.all()
    # students = get_object_or_404(User)
    return render(request, 'students.html',{'students':students})


def detail(request, stud_id):
    students = User.objects.all()
    student = get_object_or_404(User, pk=stud_id)
    
    return render(request,'detail.html',{'students':students, 'student':student})



def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def more(request):
    return render(request, 'more.html')

def animals(request):
    return render(request, 'animals.html')