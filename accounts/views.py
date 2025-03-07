# accounts/views.py
from django.shortcuts import render, redirect
from .forms import LandlordUserForm, TenantUserForm, TenantOnboardingForm
from .models import User, SiteConfig
from django.contrib.auth.decorators import login_required

def users_list(request):
    landlords = User.objects.filter(role='landlord')
    tenants = User.objects.filter(role='tenant')
    context = {'landlords': landlords, 'tenants': tenants}
    return render(request, 'accounts/users_list.html', context)


def landlord_create(request):
    form = LandlordUserForm()

    if request.method == 'POST':
        form = LandlordUserForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
                
    context={'form': form}
    return render(request, 'accounts/landlords.html', context)

def landlord_update(request, pk):
    user = User.objects.get(id = pk)
    form = LandlordUserForm(instance=user)
    if request.method == 'POST':
        form = LandlordUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
    context = {"form": form}  
    return render(request, 'accounts/landlords.html', context)

def landlord_delete(request, pk):
    user = User.objects.get(id = pk)
    user.delete()
    return redirect ('users_list.html')


def tenant_create(request):
    form = TenantUserForm() 
    if request.method == 'POST':
        form = TenantUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form":form}
    return render(request, 'accounts/tenants.html',context)

def tenant_update(request, pk):
    user = User.objects.get(id = pk)
    form = TenantUserForm(instance=user)
    if request.method == 'POST':
        form = TenantUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        
    return render(request, 'accounts/tenants.html', {'form': form, 'user': user})

def tenant_delete(request, pk):
    user = User.objects.get(id = pk)
    user.delete()
    return redirect('users_list.html')


def site_config(request):
    site_config_obj, created = SiteConfig.objects.get_or_create()

    if request.method == 'POST':
        site_config_obj.maintenance_mode = request.POST.get('maintenance_mode') == 'on'
        site_config_obj.save()
        return redirect('users_list.html')
    context = {'site_config': site_config_obj}
    return render(request, '', context)








# def user_create(request):
   
#     if request.method == 'POST':
#         if request.POST.get('role') == 'landlord':
#             form = LandlordUserForm(request.POST)
#         else:
#             form = TenantUserForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.role = form.cleaned_data['role']
#             new_user.save()
#             if new_user.role == 'landlord':
#                 return redirect('accounts:landlord_list')
#             else:
#                 return redirect('accounts:tenant_list')
#     else:
#         form = LandlordUserForm()
#     return render(request, 'accounts/landlord_create.html', {'form': form})

# def user_list(request):
    
#     landlords = User.objects.filter(role='landlord')
#     tenants = User.objects.filter(role='tenant')
#     return render(request, 'accounts/user_list.html', {'landlords': landlords, 'tenants': tenants})

# def user_update(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         if user.role == 'landlord':
#             form = LandlordUserForm(request.POST, instance=user)
#         else:
#             form = TenantUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:user_list')
#     else:
#         if user.role == "landlord":
#             form = LandlordUserForm(instance=user)
#         else:
#             form = TenantUserForm(instance=user)
#     return render(request, 'accounts/user_update.html', {'form': form, 'user': user})

# def user_delete(request, pk):
    
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         user.delete()
#         if user.role == "landlord":
#             return redirect('accounts:user_list')
#         else:
#             return redirect('accounts:tenant_list')
#     if user.role == "landlord":
#         return render(request, 'accounts/landlord_delete_confirmation.html', {'user': user})
#     else:
#         return render(request, 'accounts/tenant_delete_confirmation.html', {'user': user})