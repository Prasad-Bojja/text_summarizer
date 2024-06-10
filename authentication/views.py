from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.models import User

from django.http import JsonResponse
from .models import CustomUser
from django.views.decorators.http import require_GET

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

from django.shortcuts import render
from .models import CustomUser




def register(request): 
    if request.method == "POST":
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            # Validate the password using Django's built-in validators
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, '\n'.join(e))
            return redirect('/register/')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/register/')

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!")
            return redirect('/register/')

        # Create user
        user = CustomUser(email=email, firstname=firstname, lastname=lastname)
        user.set_password(password1)
        user.save()
        messages.success(request, "User account Created successfully!")
        return redirect('/login_form/')

    return render(request, 'register.html')




def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('/register/')


@login_required(login_url='/login/')
def change_password(request, user_id):
    # Get the user object or return a 404 response if not found
    user = get_object_or_404(CustomUser, id=user_id)
    
    # Check if the user has permission to change passwords
    if not request.user.is_staff and request.user != user:
        messages.error(request, "You don't have permission to change passwords for this user.")
        return HttpResponseForbidden()

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not user.check_password(old_password):
            messages.error(request, "Your old password is incorrect.")
            return redirect(f'/change-password/{user_id}/')

        if password1 != password2:
            messages.error(request, "New Password and Confirm password need to be the same.")
            return redirect(f'/change-password/{user_id}/')

        user.set_password(password1)
        user.save()

        # Update the session authentication hash to prevent log out
        update_session_auth_hash(request, user)

        messages.success(request, 'Password changed successfully!')
        return redirect(f'/profile/{user_id}/')
    
    return render(request, 'change_password.html', {'user': user})


def login_form(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Invalid Email address!')
            return redirect('/login/')
        user = authenticate(email=email, password=password)
        if user is None:
            messages.info(request, 'Invalid Email!')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/summarize_text/')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def profile_page(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    context = {'user': user}
    return render(request, 'profile.html', context)


@login_required(login_url='/login/')
def profile_update(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            user.email = email
            user.firstname = firstname
            user.lastname = lastname
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect(f'/profile/{user_id}/')
        except Exception:
            messages.error(request, 'This Email already exists. Please try a different Email!')

    context = {'user': user}
    return render(request, 'profile_update.html', context)


def logout_page(request):
    logout(request)
    return redirect('/login/')

def home(request):
    return render(request, 'base.html')


def search_users(request):
    term = request.GET.get('term', '').strip()
    if term:
        users = CustomUser.objects.filter(firstname__icontains=term)
        user_list = []
        for user in users:
            name_email = f"{user.first_name} {user.last_name} ({user.email})"
            user_list.append({
                'nameEmail': name_email,
                'email': user.email
            })
        return render(request, 'search_users.html', {'user_list': user_list})
    else:
        error_message = 'Please provide a search term'
        return render(request, 'search_users.html', {'error_message': error_message})
