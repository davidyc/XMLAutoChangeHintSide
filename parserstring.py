import os 
import re 

fileBefore = open('1.xaml', 'r')
strFromFB = fileBefore.readlines()
fileBefore.close()

fileAfter = open('2.xaml', 'r')
strFromFA = fileAfter.readlines()
fileAfter.close()

arrFA = []
for i in range(0, len(strFromFA)):  
      if strFromFA[i].find("<sap2010:ViewStateData Id=") != -1:         
         arrFA.append(strFromFA[i])

for i in arrFA:
    number = re.findall('\d+,\d+',i))
    sapID = re.findall('<sap2010:ViewStateData Id="\S+"',i))

    input()


print("Done!")

