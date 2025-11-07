from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the user
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})

@login_required
def admin_view(request):
    if request.user.userprofile.role != 'Admin':
        return redirect('login')  # Redirect non-admin users to login or another appropriate page
    else:
        return render(request, 'relationship_app/admin_view.html')
    
@login_required
def member_view(request):
    if request.user.userprofile.role != 'Member':
        return redirect('login')  
    else:
        return render(request, 'relationship_app/member_view.html')
    
@login_required
def librarian_view(request):
    if request.user.userprofile.role != 'Librarian':
        return redirect('login')  
    else:
        return render(request, 'relationship_app/librarian_view.html')