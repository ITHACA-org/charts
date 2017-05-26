import urllib
import xml.etree.ElementTree as ET

from django.http import HttpResponse
from django.shortcuts import render


def get_fields(request):
    lyrname = request.GET['lyrname']
    params = urllib.urlencode({
        'service':'WFS',
        'version':'1.1.0',
        'request':'DescribeFeatureType',
        'typename':lyrname
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
    return render(request, 'wfs_csv/field_choice.html', context)


def get_wfs_csv(request):
    qdict = request.GET
    typename = qdict['lyrname']
    category_field = qdict['category']
    quantity_field = qdict['quantity']

    params = urllib.urlencode({
        'service':'WFS',
        'version':'1.1.0',
        'request':'GetFeature',
        'typename':typename,
        'propertyName':category_field + ',' + quantity_field,
        'outputFormat':'csv',
        'maxFeatures':'10'
    })
    
    wfs_request = urllib.urlopen('http://localhost/geoserver/ows?%s' % params)
    content = wfs_request.read()    
    response = HttpResponse(content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="myfile.csv"'
    return response
