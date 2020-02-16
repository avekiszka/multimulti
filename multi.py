#Generator liczb multi multi
from random import randint
#definicje funkcji
def sprawdzenie(kupon, ilosc_typowanych):
    liczby_trafione = []
    for l in kupon:
        if l in wyniki:
            liczby_trafione.append(l)
    ilosc_trafionych = len(liczby_trafione)
    global suma_wygranych
    global suma_wygranych_plus
    suma_wygranych += wygrana(ilosc_trafionych, ilosc_typowanych)
    suma_wygranych_plus += wygrana_plus(ilosc_trafionych, liczby_trafione, ilosc_typowanych)
    #return print("Ilosc trafionych liczb", ilosc_trafionych, "\nTrafione liczby to", liczby_trafione,"\nWartosc wygranej:", wygrana(ilosc_trafionych, ilosc_typowanych),"\nWartosc wygranej z plusem:", wygrana_plus(ilosc_trafionych, liczby_trafione, ilosc_typowanych))
def wygrana(ilosc_trafionych, ilosc_typowanych):
    if ilosc_trafionych < 4:
        return 0
    return wygrane[ilosc_typowanych][ilosc_trafionych]
def wygrana_plus(ilosc_trafionych, liczby_trafione, ilosc_typowanych):
    if ilosc_trafionych == 0:
        return 0
    if plus in liczby_trafione:
        return wygrane_plus[ilosc_typowanych][ilosc_trafionych]
    else:
        return 0
def beben():
    while True:
        x = randint(1,80)
        if x in beben_maszyny:
            continue
        beben_maszyny.append(x)
        if len(beben_maszyny) == 80:
            break
def generator_kuponow(ilosc_typowanych):
    if ilosc_typowanych > 0 and ilosc_typowanych < 11:
        global liczba_kuponow
        liczba_kuponow = 80 // ilosc_typowanych
        for k in range(1, liczba_kuponow + 1):
            kupon = [beben_maszyny.pop() for i in range(ilosc_typowanych)]
            #print("-------------------------------------------------")
            #print("Kupon nr:", k,"\n", kupon)
            sprawdzenie(kupon, ilosc_typowanych)
            #print("Ilosc Liczb w bebnie maszyny losujacej:", len(beben_maszyny))
            #print("-------------------------------------------------")
        if len(beben_maszyny) in [2,3,8]:
            extra_ilosc_typowanych = len(beben_maszyny)
            global extra_kupon
            extra_kupon = [beben_maszyny.pop() for i in range(len(beben_maszyny))]
            sprawdzenie(extra_kupon, extra_ilosc_typowanych)
        else:
            extra_kupon = "Nie zostal wygenerowany"
#definicje zmiennych            
plus = 13
ilosc_typowanych = 10
suma_wygranych = 0
suma_wygranych_plus = 0
koszt_kuponu = 2.5
koszt_kuponu_plus = 5
#definicje tablic
beben_maszyny = []
wyniki=[9,12,13,20,37,39,42,44,49,51,53,55,58,62,64,65,67,68,37,39]
#definicje slownikow
wygrane = {1:{1:4},2:{1:0,2:16},3:{1:0,2:2,3:54},4:{1:0,2:2,3:8,4:84},5:{1:0,2:0,3:4,4:20,5:700},6:{1:0,2:0,3:2,4:8,5:120,6:1300},7:{1:0,2:0,3:2,4:4,5:20,6:200,7:6000},8:{1:0,2:0,3:0,4:4,5:20,6:60,7:600,8:22000},9:{1:0,2:0,3:0,4:2,5:8,6:42,7:300,8:2000,9:70000},10:{1:0,2:0,3:0,4:2,5:4,6:12,7:140,8:520,9:10000,10:250000}}
wygrane_plus = {1:{1:88},2:{1:24,2:120},3:{1:18,2:28,3:214},4:{1:16,2:16,3:48,4:384},5:{1:14,2:10,3:20,4:80,5:1800},6:{1:14,2:10,3:12,4:20,5:320,6:4300},7:{1:14,2:8,3:8,4:14,5:70,6:700,7:22000},8:{1:14,2:4,3:4,4:14,5:48,6:180,7:1800,8:130000},9:{1:14,2:4,3:4,4:6,5:22,6:122,7:900,8:10000,9:300000},10:{1:10,2:4,3:4,4:6,5:12,6:36,7:380,8:1520,9:50000,10:2500000}}
#wywolywanie funkcji
if __name__ == "__main__":
    beben()
    generator_kuponow(ilosc_typowanych)


                  
print("===========")
print("Suma wygranych", suma_wygranych, "\nSuma wygranych z plusem", suma_wygranych_plus)
print("===========")
print("Ilosc typowanych liczb:",ilosc_typowanych)
print("Ilosc kupionych kuponow:",liczba_kuponow)
print("===========")
print("Suma wygranych", suma_wygranych,"\nWydane pieniadze na kupony:", koszt_kuponu * liczba_kuponow,"\nZysk/Strata:", koszt_kuponu * liczba_kuponow - suma_wygranych)
print("===========")
print("Suma wygranych z plusem", suma_wygranych_plus,"\nWydane pieniadze na kupony:",koszt_kuponu_plus * liczba_kuponow ,"\nZysk/Strata:", koszt_kuponu_plus * liczba_kuponow - suma_wygranych_plus)
print("===========")
print("Extra kupon:", extra_kupon)
print("===========")
print(beben_maszyny)
