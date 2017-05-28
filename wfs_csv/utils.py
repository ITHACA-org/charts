import urllib
import xml.etree.ElementTree as ET

def get_fields(lyrname):
    params = urllib.urlencode({
        'service':'WFS',
        'version':'1.1.0',
        'request':'DescribeFeatureType',
        'typename':lyrname
    })

    wfs_request = urllib.urlopen('http://www.masdap.mw/geoserver/wfs?%s'
                                 % params)
    content = wfs_request.read()

    root = ET.fromstring(content)

    namespace = root.tag.split('}')[0] + '}'
    xpath = ('./{0}complexType/{0}complexContent/'
             '{0}extension/{0}sequence/{0}element').format(namespace)

    fields = {}
    numeric_types = ['byte', 'decimal', 'int', 'integer', 'long', 'short',
                     'boolean', 'double', 'float']
    for element in root.findall(xpath):
        type = element.attrib['type']
        if not type.startswith('gml:'):
            fields[element.attrib['name']] = type[4:]

    fieldnames = fields.keys()
    num_fieldnames = [k for k, v in fields.iteritems() if v in numeric_types]

    return fieldnames, num_fieldnames

if __name__ == '__main__':
    get_fields('geonode:forest_osm')