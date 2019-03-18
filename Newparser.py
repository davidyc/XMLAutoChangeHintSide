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
      arrFA.append(strFromFA[i])

arrFB = []
for i in range(0, len(strFromFB)): 
      if strFromFB[i].find("<sap2010:ViewStateData Id=") != -1:         
         arrFB.append(re.sub("\d+,\d+", "11,00", strFromFB[i]))   
      else:
         arrFB.append(strFromFB[i])

f = open('1.xaml', 'w')
f.writelines(arrFB)
f.close()

print("Done!")

