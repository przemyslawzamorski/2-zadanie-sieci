from random import shuffle
from quicksort import *
__author__ = 'Komputer'

file=[]
with open('data', 'rb') as f1:
# with open('IMG_20150411_154513.jpg', 'rb') as f1:
    while True:
        bytes = f1.read(1024)
        if bytes:
              for byte in bytes:
                file.append(byte)
        else:
            break
print(file)

packagelist=[] ## pusta lista paczek

#paczkowanie
counter=0
package_number=0
package_data=[]

for singlebytes in file:

    package_data.append(singlebytes) #Dodaje bit do  danych pojedynczej paczki
    counter+=1 #licznik bitow w paczce

    if counter==2:             ##określa wielkość paczki |
        counter=0               ## resetuje ilosc danych w paczce
        package_number+=1       ##okresla numer paczki
        binary_package_number=bin(package_number).split('b')[1]  ##konwertuje nr paczki na binarny
        data=bytearray(package_data)    ##tworzy paczke z danymi
        data.insert(0,int(binary_package_number))  ###dodaje do paczki przedrostek z numerem paczki
        packagelist.append(data)        ##dodaje do listy paczek  paczuszke
        package_data=[]   ## czysci dane dla kolejnej paczki

if package_data:        ##w przypadku gdy ilość danychw  paczce jest nierówna innym
    package_number+=1       ##okresla numer paczki
    binary_package_number=bin(package_number).split('b')[1]  ##konwertuje nr paczki na binarny
    data=bytearray(package_data)    ##tworzy paczke z danymi
    data.insert(0,int(binary_package_number))  ###dodaje do paczki przedrostek z numerem paczki
    packagelist.append(data)

print('lista paczek')
print(packagelist)

#Mieszanie listy paczel
shuffle(packagelist)
print('Pomieszane paczki')
print(packagelist)

##sortowanie paczek

sorted_package_list=quickSort(packagelist)




# z=int(str(qw),2) #konwersja nr na decymal paczke







