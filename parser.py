import xml.etree.ElementTree as ET
import os  

  '''  f = open( "pages/xml.xml",'rt')
	data = xml.dom.minidom.parseString(f.read())
	f.close()
	element = xml.dom.minidom.Element('id')
	element.setAttribute('value','newAttr')
	f = open("pages/xml.xml",'wt')
	qw = data.toxml()
	qw = qw.encode('utf-8')
	f.write(qw)
	f.close()'''

tree = ET.parse('1.xaml')
root = tree.getroot()

elements = root.find('{http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation}WorkflowViewState.ViewStateManager')
element = elements.find('{http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation}ViewStateManager')


print(element)
mykey = '{http://schemas.microsoft.com/netfx/2009/xaml/activities/presentation}VirtualizedContainerService.HintSize'

for i in element:
    print(i.attrib[mykey])


for i in element:
     if i.attrib[mykey] == '314,60':
         print("Yes")
         i.attrib[mykey] = '00,00'


for i in element:
    print(i.attrib[mykey])




  
