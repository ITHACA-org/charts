import urllib

from django.http import HttpResponse

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

