from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password


def home(request):
    return render(request, "Superadmin/superadmin.html")


@csrf_exempt  # Only use if CSRF token is not included in the request
def add_property_owner(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Ensure all fields are provided
        if not username or not email or not password:
            return JsonResponse({"success": False, "message": "All fields are required."}, status=400)

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists."}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email already registered."}, status=400)

        # Create user and hash password
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # Hash password before storing
        )

        # Assign user to "property_owner" group
        group, created = Group.objects.get_or_create(name="property_owner")
        user.groups.add(group)

        return JsonResponse({"success": True, "message": f"User {username} added successfully!"})

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)