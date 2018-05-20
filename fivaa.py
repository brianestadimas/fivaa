def fivaa(angka):
    angkaHead = angka+1
    angkaTail = angka-1
    if (angka<=0):
        angkaTail = 0
    while angkaTail>=0:
        print(str(angkaTail)*2, end="")
        print(str(angkaHead)*(angkaHead-1))
        angkaTail-=1
        angkaHead-=1
        
