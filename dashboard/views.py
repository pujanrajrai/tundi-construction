from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


# Create your views here.
@staff_member_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'dashboard/home.html')
