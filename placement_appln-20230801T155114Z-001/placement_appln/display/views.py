from django.shortcuts import render
from .models import CustomUser, Company, Updates

# Create your views here.
def home(request):
    cand = CustomUser.objects.get(username=request.user)
    upd = Updates.objects.filter(company__in=cand.companies_applied.all())
    return render(request, 'home.html', {'updates':upd})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies':companies})

def company(request, pk):
    company = Company.objects.get(pk=pk)
    updates = Updates.objects.filter(company=company)
    return render(request, 'company.html', {'company':company, 'updates':updates})

def placement(request):
    return render(request, 'placement.html')

