#Testing stuff

#Reppun sisältö tulee tähän listaan, WIP
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
        
        else:
            print('Virheellinen valinta', '\n')

#Kioskin sisällä
def kioskissa():
    while True:
        kioskissa = input('''
 Kioskissa on paljon virvokkeita ja välipaloja
 Mitä haluat tehdä?

 1. Selaa lehtiä 

 2. Katsele suklaapatukka tarjonaa

 3. Tarkastele juoma tarjontaa

 4. Katsele ympärille

 5. Käännyt ja lähdet ulos kioskista

 > ''')
        if kioskissa == '1':
            print('''
Selaat lehtiä...
Juorulehtiä, aikakausilehtiä, uutislehtiä... muutama sarjakuva, mutta ei mikään mikä kiinostaisi.
Jätät lehtien selailun sikseen.
''')

        elif kioskissa == '2':
            print('Perus maitosuklaata, pähkinäsuklaata, erilaisia täyte suklaita... Ehkei nyt')

        elif kioskissa == '3':
            print('Kaljaa, kaljaa, kaljaa ja lisää kaljaa... Juovatko ihmiset mitään muuta täällä?!')

        elif kioskissa == '4':
            print('''
Päätät vähän katsella ympärille...

Kioskin myyjä näyttää elämäänsä kyllästyneeltä keski-ikäiseltä mieshenkilöltä, vaikuttaa kuin hän ei olisi nukkunut viimeaikoina tarpeeksi.

Kioskissa notkuu alkoholilta ja kuselta haiseva epämääräinen henkilö, parempi varmaan pysyä kaukana siitä.

Ikkunasta ulos katsoessa näet viliseviä ihmisiä kävelevän junista ulos ja junien sisään... kiireinen juna-asema tähän aikaan päivästä.            
''')

        elif kioskissa == '5':
            print('Käännyt ja menet takaisin ulos')
            break

        else:
            print('Ei ole hyväksytty komento')

#Hampurilaisravintolan sisällä
def purilaiselle():
    while True:
        purilaisella = input('''
Astut sisään hampurilaisravintolaan, mitä saisi olla?
 ___________________________________________________________
|   __      ____     __     _     ___      ___   _____    |
|  |   \   |  __|   |  \   | |   |   \    |  /  / ____|   |
|  | |  |  | |__    | | \  | |   | |\ \    \_\  | |____   |
|  |  _/   |  __|   | |\ \ | |   | ___ \         \___  \  |
|  | |     | |__    | | \ \| |   | ____ \        ____| |  |
|  |_|     |____|   |_|  \___|   |_|   \_\      |_____/   |
|_________________________________________________________|
|                                                         |
|                   < B U R G E R S >                     |
|_________________________________________________________|

1. Pirtelö - 2e

2. Juustohampurilainen - 2e

3. Ranskalaiset - 1e

4. Limu - 1e

5. Jäätelö - 2e

6. Ei mitään tällä kertaa

> ''')
        if purilaisella == '1':
            print('Ostat kylmän ja herkullisen mansikkapirtelön')


        elif purilaisella == '2':
            print('Ostat Juustohampurilaisen, NAMI!')


        elif purilaisella == '3':
            print('Ostat lämpimät, suolaiset ja rasvaiset, mutta herkulliset, ranskalaiset!')


        elif purilaisella == '4':
            print('Ostat virkistävän limun')


        elif purilaisella == '5':
            print('Ostat kermaisen, makean ja hyvän jäätelön')


        elif purilaisella == '6':
            print('Päätät kääntyä ja lähteä hampurilaisravintolasta')
            break

        else:
            print('Virheellinen valinta')

#Kahvilan sisällä
def kahvilassa():
    while True:
            kahvilassa = input('Astut sisälle kahvilaan, siellä on paljon ihmisiä')

#Ulos pääovista
def paaovistaulos():
    while True:
            paaovista = input('''
Edessä näkyy Elielin aukio...

Näet kerjäläisiä, jeesustelijoita, hyväntekeväisyys keräilijöitä sekä kiireellisiä ihmisiä kuljeksimassa.

1. Katsele jeesustelijoita

2. Tarkkaile kerjäläistä

3. Tutkaile hyväntekeväisyys keräilijöitä

4. Käänny takaisin sisälle
''')
            
            if paaovista == '1':
                print('''
Jeesustelija huutaa megafoniin jotain kuinka Jeesus tulee ja kaikkien pitää pelastautua, hänen mukanaan oleva henkilö jakaa lehtisiä ohikulkijoille... jotka eivät ole kiinnostuneita...''')

            elif paaovista == '2':
                print('Kerjäläinen istuu polvillaan pahvin päällä ja kerjää tyhjään kertakäyttö kahvimukiin almuja, kaikki kiireiset ihmiset vilisevät ohi')

            elif paaovista == '3':
                print('Hyväntekeväisyys henkilöt keräävät allekirjoituksia johonkin luonnon pelastus juttuun. Monet kävelevät ohi, mutta muutamat jäävät puhumaan ja kyselemään')

            elif paaovista == '4':
                print('Eiköhän tässä ollut kaupungin vilinää tarpeeksi... Suuntaat takaisin sisälle.')
                break

#Tervehdys teksti
terve = ('''

Tervehdys!

Matkasi alkaa on pysähtynyt Helsingin rautatieasemalle, sinulla on aikaa tuhlattavana.

Miten haluat kuluttaa aikaa? Se on sinusta kiinni.

''')

print(terve)

#Aloitus rautatieasemalta
while True:
    hesarauttisvalinnat = input('''
Olet Helsingin rautatieasemalla. Edessä näet laitureille vievät ovet.
Ympärilläsi on kahviloita, hampurilaisravintola ja kioskeja.

Mihin haluat mennä?

1. Kioski

2. Hampurilaisravintola

3. Kahvila

4. Ulos (pääovista)

5. Ulos (laitureille)

Q. Lopeta peli

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

    elif hesarauttisvalinnat == 'Q':
        print('Kiitos, kun pelasit tämän pienen prototyyppi pelin, tämä on vain testi peli harjoittelun takia :)', '\n')
        break
    
    else:
        print('Virhellinen valinta tai ei valintaa annettu')

