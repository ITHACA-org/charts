import urllib

from django.http import HttpResponse

def get_wfs_csv(request):
    params = urllib.urlencode({
        'service':'WFS',
        'version':'1.1.0',
        'request':'GetFeature',
        'typename':'geonode:hti_geology_geology_pap_coxetalii_2011_polygon',
        'propertyName':'name,area',
        'outputFormat':'csv',
        'maxFeatures':'10'
    })
    
    wfs_request = urllib.urlopen('http://localhost/geoserver/ows?%s' % params)
    content = wfs_request.read()    
    response = HttpResponse(content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="myfile.csv"'
    return response
