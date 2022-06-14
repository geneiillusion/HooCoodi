#Testing stuff

#Reppun sisältö tulee tähän listaan, WIP
reppu = ['omena']

#Rahat
rahat = [100]

#Osto funktio (WIP)
#def osto():


#Energia
energia = [100]

#Reppu funktio
def omareppu():
    while True:
        
        print('Tutkit omaa reppuasi, repusta löytyy: ', reppu)

        repputoiminto = input('''
        
Mitä haluat tehdä?

1. Käytä tavara

2. Tutki tavaraa

3. Heitä tavara pois

4. Katso rahatilanne

5. Sulje reppu
> ''')

        if repputoiminto == '1':
            print('Minkä tavaran haluat käyttää?', '\n')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif repputoiminto == '2':
            print('Mitä tavaraa haluat katsoa?', '\n')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
        
        elif repputoiminto == '3':
            print('Minkä tavaran haluat heittää pois?', '\n', reppu)
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif repputoiminto == '4':
            print('Rahasi on', rahat, 'euroa')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
        
        elif repputoiminto == '5':
            print('Päätät ettet tarvitse mitään tällä hetkellä', '\n')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
            break
            
        else:
            print('Virheellinen toiminto')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
        
#Rautatieaseman laiturien ympäristö
def rauttislaiturit(): 
    while True:
        
        laitureilla = input('''Näet junia
Mitä teet?

1. Katselet ympärille

2. Katsot puhelinta

3. Suuntaat eteenpäin junille

4. Suuntaa takaisin sisälle

> ''')

        if laitureilla == '1':
            print('Näet paljon junia ja odottavia ihmisiä. Paljon liikennettä näyttää olevan tänään.')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
            
        elif laitureilla == '2':
            print('Katsot puhelinta... Ei viestejä tai puheluita, ei mitään mielenkiintoista')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
        
        elif laitureilla == '3':
            print('Kävelet eteenpäin laitureille ja katselet junia. Junia lähtee moniin kaupunkeihin eri osaan Suomea, lopulta olet kiertänyt laiturin ja palaat takaisin')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif laitureilla == '4':
            print('Päätät suunnata takaisin sisälle')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
            break
        
        else:
            print('Virheellinen valinta', '\n')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

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

 5. Osta jotakin

 6. Käännyt ja lähdet ulos kioskista

 > ''')
        if kioskissa == '1':
            print('''
Selaat lehtiä...
Juorulehtiä, aikakausilehtiä, uutislehtiä... muutama sarjakuva, mutta ei mikään mikä kiinostaisi.
Jätät lehtien selailun sikseen.
''')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif kioskissa == '2':
            print('Perus maitosuklaata, pähkinäsuklaata, erilaisia täyte suklaita... Ehkei nyt')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif kioskissa == '3':
            print('Kaljaa, kaljaa, kaljaa ja lisää kaljaa... Juovatko ihmiset mitään muuta täällä?!')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif kioskissa == '4':
            print('''
Päätät vähän katsella ympärille...

Kioskin myyjä näyttää elämäänsä kyllästyneeltä keski-ikäiseltä mieshenkilöltä, vaikuttaa kuin hän ei olisi nukkunut viimeaikoina tarpeeksi.

Kioskissa notkuu alkoholilta ja kuselta haiseva epämääräinen henkilö, parempi varmaan pysyä kaukana siitä.

Ikkunasta ulos katsoessa näet viliseviä ihmisiä kävelevän junista ulos ja junien sisään... kiireinen juna-asema tähän aikaan päivästä.            
''')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif kioskissa == '5':
            print('Ostit maitosuklaata, se maksoi 1e')
            

        elif kioskissa == '6':
            print('Käännyt ja menet takaisin ulos')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
            break

        else:
            print('Ei ole hyväksytty komento')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

#Hampurilaisravintolan sisällä
def purilaiselle():

    print('''
 __________________________________________________________
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
''')

    while True:
        purilaisella = input('''
Olet hampurilaisravintolassa, mitä haluat tehdä?

9. Katso ruokalistaa

0. Ei mitään tällä kertaa, poistu

> ''')
        if purilaisella == '1':
            print('Ostat kylmän ja herkullisen mansikkapirtelön')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')


        elif purilaisella == '2':
            print('Ostat Juustohampurilaisen, NAMI!')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif purilaisella == '3':
            print('Ostat lämpimät, suolaiset ja rasvaiset, mutta herkulliset, ranskalaiset!')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')


        elif purilaisella == '4':
            print('Ostat virkistävän limun')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif purilaisella == '5':
            print('Ostat kermaisen, makean ja hyvän jäätelön')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

        elif purilaisella == '9':
            print('''
1. Pirtelö - 2e

2. Juustohampurilainen - 2e

3. Ranskalaiset - 1e

4. Limu - 1e

5. Jäätelö - 2e
''')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')


        elif purilaisella == '0':
            print('Päätät kääntyä ja lähteä hampurilaisravintolasta')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')
            break

        else:
            print('Virheellinen valinta')
            eteenpain = input('Paina ENTER jatkaaksesi . . .')

#Kahvilan sisällä
def kahvilassa():
    while True:
            kahvilassa = input('''Astut sisälle kahvilaan, siellä on paljon ihmisiä.

1. Katso kahvilan tarjontaa

2. Etsi tyhjä istumapaikka

3. Tutkaile kahvilaa

4. Poistu kahvilasta
> ''')

            if kahvilassa == '1':
                print('''

Ruoka- ja juomalista:

''')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif kahvilassa == '2':
                print('Menet istumaan tyhjälle paikalle')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif kahvilassa == '3':
                print('Katselet ympärille')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif kahvilassa == '4':
                print('Et halua mitään, joten käännyt takaisin')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')
                break

            else:
                print('Virheellinen valinta')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

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
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif paaovista == '2':
                print('Kerjäläinen istuu polvillaan pahvin päällä ja kerjää tyhjään kertakäyttö kahvimukiin almuja, kaikki kiireiset ihmiset vilisevät ohi')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif paaovista == '3':
                print('Hyväntekeväisyys henkilöt keräävät allekirjoituksia johonkin luonnon pelastus juttuun. Monet kävelevät ohi, mutta muutamat jäävät puhumaan ja kyselemään')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')

            elif paaovista == '4':
                print('Eiköhän tässä ollut kaupungin vilinää tarpeeksi... Suuntaat takaisin sisälle.')
                eteenpain = input('Paina ENTER jatkaaksesi . . .')
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

6. Katso repun sisältö

7. Osta junalippu

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

    elif hesarauttisvalinnat == '6':
        omareppu()

    elif hesarauttisvalinnat == '7':
        print('Minne haluat lähteä?')

    elif hesarauttisvalinnat == 'Q':
        print('Kiitos, kun pelasit tämän pienen prototyyppi pelin, tämä on vain testi peli harjoittelun takia :)', '\n')
        break
    
    else:
        print('Virhellinen valinta tai ei valintaa annettu')

