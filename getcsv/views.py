#from django.shortcuts import render

# Create your views here.

import urllib
import xml.etree.ElementTree as ET
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
    return render(request, 'pie_chart_v2.html')


def donut_chart_v2(request):
        return render(request, 'donut_chart_v2.html')


def chart(request):
    layer = ['vvff', 'osm_forest', 'hti_geology_geology_pap_coxetalii_2011_polygon']
    context = {'layer': layer}
    return render(request, 'Chart.html', context)


def get_fields(request):
    lyrname = request.GET['lyrname']
    params = urllib.urlencode({
        'service': 'WFS',
        'version': '1.1.0',
        'request': 'DescribeFeatureType',
        'typename': lyrname
    })

    wfs_request = urllib.urlopen('http://localhost/geoserver/ows?%s'
                                 % params)
    content = wfs_request.read()

    root = ET.fromstring(content)
    namespace = root.tag.split('}')[0] + '}'
    xpath = ('./{0}complexType/{0}complexContent/'
             '{0}extension/{0}sequence/{0}element').format(namespace)
    numeric_types = ['byte', 'decimal', 'int', 'integer', 'long', 'short',
                     'boolean', 'double', 'float']
    fields = {}
    for element in root.findall(xpath):
        type = element.attrib['type']
        if not type.startswith('gml:'):
            fields[element.attrib['name']] = type[4:]

    fieldnames = fields.keys()
    num_fieldnames = [k for k, v in fields.iteritems() if v in numeric_types]

    context = {
        'lyrname': lyrname,
        'fieldnames': fieldnames,
        'num_fieldnames': num_fieldnames
    }
    return render(request, 'Chart.html', context)

if __name__ == '__main__':
    get_fields('geonode:forest_osm')

def get_wfs_csv(request):
    qdict = request.GET
    typename = qdict['lyrname']
    category_field = qdict['category']
    quantity_field = qdict['quantity']

    params = urllib.urlencode({
        'service': 'WFS',
        'version': '1.1.0',
        'request': 'GetFeature',
        'typename': typename,
        'propertyName': category_field + ',' + quantity_field,
        'outputFormat': 'csv',
        'maxFeatures': '10'
    })

    wfs_request = urllib.urlopen('http://localhost/geoserver/ows?%s' % params)
    content = wfs_request.read()
    response = HttpResponse(content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="myfile.csv"'
    return response



