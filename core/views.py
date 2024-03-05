from django.shortcuts import render, get_object_or_404
from auth_user.decorators import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@admin_only
def index (request):
    return render(request, 'admin/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['controller'])
def controller(request):
    hopps_list = Hopps.objects.all()

    if request.method == 'POST':
        form = HoppsForm(request.POST)
        if form.is_valid():
            hopps = form.save(commit=False)
            hopps.save()
            return redirect('controller')
    else:
        form = HoppsForm()

    context = {
         'hopps_list': hopps_list,
         'form': form
    }
    return render(request, 'controller.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def staff(request):
    return render(request, 'staff.html')

def ticket_logs(request):
     return render(request, 'admin/ticket_logs.html')
def repair(request):
      return render(request, 'repair.html')

# Department
def hopps(request):
    hopps_form = HoppsForm()

    if request.method == 'POST':
        hopps_form = HoppsForm(request.POST)

        if hopps_form.is_valid():
            hopps_form.save()
            return redirect('hopps')

    hopps_list = Hopps.objects.all()
    context = {
        'hopps_form': hopps_form,
        'hopps_list': hopps_list,
    }

    return render(request, 'department/hopss/hopps.html', context)

def hopss_update(request, pk):
    hopss = Hopps.objects.get(id=pk)
    if request.method == 'POST':
        form = HoppsForm(request.POST, instance=hopss)
        if form.is_valid():
            form.save()
            return redirect('controller')
    else:
        form = HoppsForm(instance=hopss)
    context = { 'form': form}
    return render(request, 'department/hopss/hopss_update.html', context)

@login_required(login_url='login')
def hopps2(request, event_id):
    hopps2 = get_object_or_404(Hopps, id=event_id)
    hopps3 = get_object_or_404(Hopps, id=event_id)
    hopps_list = Hopps.objects.all()

    context = {
        'hopps2':hopps2,
        'hopps_list': hopps_list,
        'hopps3': hopps3
    }
    
    return render(request, 'department/hopss/hopps2.html', context)

def nursing(request):
     return render(request, 'department/nursing.html')
def medical(request):
     return render(request, 'department/medical.html')
def allied(request):
     return render(request, 'department/allied.html')
def finance(request):
     return render(request, 'department/finance.html')
def mcc(request):
     return render(request, 'department/mcc.html')