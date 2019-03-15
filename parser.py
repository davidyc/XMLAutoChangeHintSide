import xml.etree.ElementTree as ET

tree = ET.parse('1.xaml')
root = tree.getroot()

elements = root.find('{http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation}WorkflowViewState.ViewStateManager')
element = elements.find('{http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation}ViewStateManager')


print(element)

for i in element:
    print(i.attrib['{http://schemas.microsoft.com/netfx/2009/xaml/activities/presentation}VirtualizedContainerService.HintSize'])







  
