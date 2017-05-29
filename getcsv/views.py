#from django.shortcuts import render

# Create your views here.

import csv
from django.http import HttpResponse
from django.shortcuts import render


def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'area'])
    writer.writerow(['Af', 3.51])
    writer.writerow(['Ems / ems', 0.00])
    writer.writerow(['Ep / ep', 0.00])
    writer.writerow(['Lmst', 4.88])
    writer.writerow(['Mpb', 18.93])
    writer.writerow(['Pf', 30.53])
    writer.writerow(['Ppf', 6.84])
    writer.writerow(['Qa', 0.49])
    writer.writerow(['Qhac', 5.91])
    writer.writerow(['Qhad', 0.00])
    writer.writerow(['Qham', 11.01])
    writer.writerow(['Qht1', 1.10])
    writer.writerow(['Qht2', 27.60])
    writer.writerow(['Qpf', 34.40])
    writer.writerow(['Qphf', 42.30])

    return response

def get_csv_aggr(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'area'])
    writer.writerow(['Af', 3.51])
    writer.writerow(['Ems / ems', 0.00])
    writer.writerow(['Ep / ep', 0.00])
    writer.writerow(['Lmst', 4.88])
    writer.writerow(['Mpb', 18.93])
    writer.writerow(['Pf', 30.53])
    writer.writerow(['Ppf', 6.84])
    writer.writerow(['Qa', 0.49])
    writer.writerow(['Qhac', 5.91])
    writer.writerow(['Qhad', 0.00])
    writer.writerow(['Qham', 11.01])
    writer.writerow(['Qht1', 1.10])
    writer.writerow(['Qht2', 27.60])
    writer.writerow(['Qphf', 42.30])
    writer.writerow(['Af', 6.58])
    writer.writerow(['Qa', 30.78])
    writer.writerow(['Af', 16.58])

    return response


def pie_chart_v1(request):
    return render(request, 'pie_chart_v1.html')


def donut_chart_v1(request):
    return render(request, 'donut_chart_v1.html')


def pie_chart_v2(request):
    qdict = request.GET
    typename = qdict['lyrname']
    category_field = qdict['category']
    quantity_field = qdict['quantity']
    context = {
        'lyrname': typename,
        'category': category_field,
        'quantity': quantity_field
    }
    return render(request, 'pie_chart_v2.html', context)


def donut_chart_v2(request):
    return render(request, 'donut_chart_v2.html')
