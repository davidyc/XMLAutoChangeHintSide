import xml.etree.ElementTree as ET

ET.register_namespace("", "http://schemas.microsoft.com/netfx/2009/xaml/activities")
ET.register_namespace("mc","http://schemas.openxmlformats.org/markup-compatibility/2006")
ET.register_namespace("mva", "clr-namespace:Microsoft.VisualBasic.Activities;assembly=System.Activities")
ET.register_namespace("njl", "clr-namespace:Newtonsoft.Json.Linq;assembly=Newtonsoft.Json")
ET.register_namespace("s", "clr-namespace:System;assembly=mscorlib")
ET.register_namespace("sads", "http://schemas.microsoft.com/netfx/2010/xaml/activities/debugger")
ET.register_namespace("sap", "http://schemas.microsoft.com/netfx/2009/xaml/activities/presentation")
ET.register_namespace("sap2010", "http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation")
ET.register_namespace("scg", "clr-namespace:System.Collections.Generic;assembly=mscorlib")
ET.register_namespace("sco", "clr-namespace:System.Collections.ObjectModel;assembly=mscorlib")
ET.register_namespace("ui", "http://schemas.uipath.com/workflow/activities")
ET.register_namespace("x", "http://schemas.microsoft.com/winfx/2006/xaml")


tree = ET.parse('1.xaml')

root = tree.getroot()



xmlstr = ET.tostring(root, encoding='utf8', method='xml')



print(xmlstr)