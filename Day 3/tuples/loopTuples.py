# loop tuples, basicly same with list
namaa = ('Sarah', 'Amanda', 'Lisa', 'Emily', 'Jessica')
for nama in namaa:
    print(nama) #output: Sarah, Amanda, Lisa, Emily, Jesica


# use range() and len() method
nama_tuan_putri = ('Elizabeth', 'Victoria', 'Catherine', 'Isabella', 'Mary')
for i in range(len(nama_tuan_putri)):
    print(nama_tuan_putri[i]) #output: Elizabeth, Victoria, Catherine, Isabella, Mary

#use while
nama_kucing_lucu = ('Whiskers', 'Fluffy', 'Mittens', 'Peanut', 'Marshmallow')
i = 0
while i < len(nama_kucing_lucu):
    print(nama_kucing_lucu[i]) #output: Whiskers, Fluffy, Mittens, Peanut, Marshmallow
    i+=1