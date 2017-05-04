#from django.shortcuts import render

# Create your views here.

import csv
from django.http import HttpResponse

def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'

    writer = csv.writer(response)
    writer.writerow(['label', '1', '2', '3'])
    writer.writerow(['label 2', '4', '5', '6'])

    return response
