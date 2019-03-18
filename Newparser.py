import os 

f = open('1.xaml', 'r')
a = f.readlines()
f.close()
 
n = []
for i in range(0, len(a)):
   if -1 != a[i].find('Id'):
      n.append(a[i].replace('sap:VirtualizedContainerService.HintSize="314,91"', 'sap:VirtualizedContainerService.HintSize="00,00"'))
   else:
      n.append(a[i])
 
f = open('1.xaml', 'w')
f.writelines(n)
f.close()