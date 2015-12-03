from random import shuffle

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
    if counter==2:             ##określa wielkość paczki | dodaje do listy paczek paczke gotową z danymi
        counter=0               ##i dodanym numerze paczki
        package_number+=1
        binary_package_number=bin(package_number).split('b')[1]
        data=bytearray(package_data)
        data.insert(0,int(binary_package_number))  ###TODO dodać prepend
        packagelist.append(data)
        package_data=[]

    package_data.append(singlebytes)
    counter+=1

print('lista')
print(packagelist)
print(packagelist[1])
##Mieszanie listy paczel
# shuffle(packagelist)
# print(packagelist)


