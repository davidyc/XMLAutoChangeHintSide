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




arrFB = []
for i in range(0, len(strFromFB)):
    addstr = strFromFB[i]
    for string in arrFA:
        number = re.findall('\d+,\d+',string)
        sapID = re.findall('<sap2010:ViewStateData Id="\S+"',string)
        if strFromFB[i].find(sapID[0]) != -1:         
            addstr = re.sub("\d+,\d+", number[0], strFromFB[i]) 
            break     
   
    arrFB.append(addstr)

f = open('1.xaml', 'w')
f.writelines(arrFB)
f.close()

print("Done!")

