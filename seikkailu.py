#Testing stuff

#Reppun sisältö tulee tähän listaan
reppu = ['omena']
#Rahat
rahat = [100]

#Reppu funktio
def omareppu():
    while True:
        
        print('Tutkit omaa reppuasi, repusta löytyy: ', reppu)

        repputoiminto = input('''
Rahasi: ''', rahat, '''
        
Mitä haluat tehdä?

1. Käytä tavara

2. Tutki tavaraa

3. Heitä tavara pois

4. Sulje reppu
> ''')

        if repputoiminto == '1':
            print('Minkä tavaran haluat käyttää?', '\n')
            
        elif repputoiminto == '2':
            print('Mitä tavaraa haluat katsoa?', '\n')
        
        elif repputoiminto == '3':
            print('Minkä tavaran haluat heittää pois?', '\n', reppu)
        
        elif repputoiminto == '4':
            print('Päätät ettet tarvitse mitään tällä hetkellä', '\n')
            break
            
        else:
            print('Virheellinen toiminto')
        
#Rautatieaseman laiturien ympäristö
def rauttislaiturit(): 
    while True:
        
        laitureilla = input('''Näet junia
Mitä teet?

1. Katselet ympärille

2. Katsot puhelinta

4. Suuntaat eteenpäin junille

5. Suuntaa takaisin sisälle

I. Tutki reppuasi

> ''')
        if laitureilla == '1':
            print('Näet paljon junia ja odottavia ihmisiä.')
            
        elif laitureilla == '2':
            print('asd')
        
        elif laitureilla == '3':
            print('asd')
        
        elif laitureilla == '4':
            print('asd')
       
        elif laitureilla == '5':
            print('päätät suunnata takaisin sisälle')
            break
        
        elif laitureilla == 'I':
            omareppu()
        
        else:
            print('Virheellinen valinta', '\n')

#Kioskin sisällä
def kioskissa():
    while True:
        kioskissa = input('Kioskissa on paljon virvokkeita ja välipaloja')      

#Hampurilaisravintolan sisällä
def purilaiselle():
    while True:
        purilaisella = input('Menet hampurilaisravintolaan, näet menun')

#Kahvilan sisällä
def kahvilassa():
    while True:
            kahvilassa = input('Astut sisälle kahvilaan, siellä on paljon ihmisiä')

#Ulos pääovista
def paaovistaulos():
    while True:
            paaovista = input('Edessä näkyy Elielin aukio')

#Tervehdys teksti
terve = ('''

Tervehdys!

Matkasi alkaa tästä, olet Helsingissä, tarkalleen rautatieasemalla.

Minne haluisitkaan matkata? Se on sinusta kiinni.

''')

print(terve)

#Aloitus rautatieasemalta
while True:
    hesarauttisvalinnat = input('''
Olet Helsingin rautatieasemalla. Edessä näet laitureille vievät ovet.
Ympärilläsi on kahviloita, hampurilaisravintola ja kioskeja.

Mihin haluat mennä?

1. Kioski

2. Hampurilaisravintoal

3. Kahvila

4. Ulos (pääovista)

5. Ulos (laitureille)

> ''')
    
    #kioskille
    if hesarauttisvalinnat == '1':
        kioskissa()
    
    #purilaiselle
    elif hesarauttisvalinnat == '2':
        purilaiselle()
    
    #kahvilaan
    elif hesarauttisvalinnat == '3':
        kahvilassa()
    
    #ulos pääovista
    elif hesarauttisvalinnat == '4':
        paaovistaulos()
   
    #ulos laitureille
    elif hesarauttisvalinnat == '5':
        rauttislaiturit()
  
    else:
        print('Virhellinen valinta tai ei valintaa annettu')

