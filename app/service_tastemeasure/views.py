from django.shortcuts import render


def servicepage(request):
    return render(request, 'service_tastemeasure/servicepage.html')
