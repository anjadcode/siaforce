a=raw_input('Masukkan nim awal : ')
b=raw_input('Banyak yang di Gnerate : ')
fr=open('user.txt','w')

for x in range(int(b)):
    print(str(int(a)+x))
    fr.write(str(int(a)+x)+'\n')
fr.close()
