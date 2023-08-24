from django.shortcuts import get_object_or_404, render
from .models import Iha


def index(request):
    ihas = Iha.objects.filter(is_active=True)
    context = {
        'ihas': ihas
    }
    return render(request, "iharental/index.html", context)

def rent(request,iha_id):
    
    ihaObj = get_object_or_404(Iha,pk = iha_id)
    if request.method == 'GET':
        # if 'activate' in request.GET:
        print('İha kiralandı.', iha_id)
        ihaObj.is_rented = True
        ihaObj.save()
        # elif 'deactivate' in request.POST:
        #     ihas1.is_rented = False
        #     ihas1.save()
    ihas = Iha.objects.filter(is_active=True)
    context = {
        'ihas' : ihas
    }
    return render(request, 'iharental/index.html', context)

def release(request,iha_id):
    
    ihaObj = get_object_or_404(Iha,pk = iha_id)
    if request.method == 'GET':
        # if 'activate' in request.GET:
        print('İha kiralandı.', iha_id)
        ihaObj.is_rented = False
        ihaObj.save()
        # elif 'deactivate' in request.POST:
        #     ihas1.is_rented = False
        #     ihas1.save()
    ihas = Iha.objects.filter(is_active=True)
    context = {
        'ihas' : ihas
    }
    return render(request, 'iharental/index.html', context)