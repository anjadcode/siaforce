namaFile=raw_input("Masukkan output file : ")
a=raw_input("masukkan wordphrase (pisahkan dengan spasi): ")
b=[]
stop='y'
'''while stop=="y":
    i=raw_input("masukka wordprase : ")
    a.append(str(i))
    print (a)
    stop=raw_input("Tambah wordPhrase Lagi ? y/n ")'''
a=a.split()
int_a=len(a)
for x in range(len(a)):
    for y in range(len(a)):
        if y==x:
            pass
        else:
            if a[x].isdigit() and a[y].isdigit():
                pass
            else:
                print (a[x]+a[y])
                b.append(a[x]+a[y])
for w in range(len(a)):
    if not a[w].isdigit():
        b.append(a[w])
        print (a[w])
    
fw=open(namaFile+'.txt','w')
for z in b:
    fw.write(z+'\n')
fw.close()
