def topla(sayi1,sayi2):
    return sayi1 + sayi2
def cikar(sayi1,sayi2):
    return sayi1 - sayi2
def carp(sayi1,sayi2):
    return sayi1 * sayi2
def böl(sayi1,sayi2):
    return sayi1 / sayi2

print("operasyon:")
print("1:Topla")
print("2:Çıkar")
print("2:Çarp")
print("2:Böl")
sec = input("operasyon seciniz")

sayi1=int(input("birinci sayi"))
sayi2=int(input("ikinci sayi"))

if sec == '1':
    print("toplam:" + str(topla(sayi1,sayi2)))
elif sec == '2':
    print("cıkar:" + str(cikar(sayi1,sayi2)))
elif sec == '3':
    print("carp:" + str(carp(sayi1,sayi2)))Böl
elif sec == '4':
    print("böl:" + str(böl(sayi1,sayi2)))
else:
    print("geçersiz seçenek")