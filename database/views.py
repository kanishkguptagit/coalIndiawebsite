from django.shortcuts import render,redirect
from database.models import production,transport

# Create your views here.
def dashboard(request):    
    return render(request,'database.html')

def transport_table(request):
    if(request.method == 'POST'):
        date = request.POST['date1']
        transport_trip = request.POST['transtrip']
        dispatch = request.POST['dispatch']
        c=transport(date=date, transport_trip=transport_trip, dispatch=dispatch)
        c.save()
        return redirect('/database/dashboard')

def production_table(request):
    if(request.method == 'POST'):
        date = request.POST['date2']
        actual_production = request.POST['actprod']
        reported_production = request.POST['repprod']
        b=production(date=date,actual_production=actual_production,reported_production=reported_production)
        b.save()
        return redirect('/database/dashboard')