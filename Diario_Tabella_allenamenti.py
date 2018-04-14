"""Programma che simula un calendario sportivo di un atleta
con tanto di indicatori di modalità,allenamento da fare e orario di inizio.
Alla fine dell'allenamento se hai superato un record puoi trascriverli nel file record.csv
@author Michael Tezza
@version 3.2 2017-12-17
"""
def Index_1():
    a=""
    bgcolor("blue")
    title("Athletics Calendar 3.2")
    Penna=turtle.Turtle()
    screen= turtle.Screen()
    screen.setup(1200,1000,0,0)
    Penna.penup()
    Penna.goto(-650,280)
    Penna.pencolor("white")
    Penna.write("Benvenuti nel calendario riservato agli atleti italiani",font=("Arial",40, "normal"))
    Penna.right(90)
    Penna.forward(50)
    Penna.write("Qui potrai,tramite un file csv,inserire gli allenamenti mensili",font=("Arial",20, "normal"))
    Penna.forward(40)
    Penna.write("Inserire nel file csv: cosa c'è da fare tra [scarico,lavoro,palestra,salite,gara,riposo]",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("                       scrivi l'allenamento",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("                       e orario (ex. come 18:00)",font=("Arial",20, "normal"))
    Penna.forward(40)
    Penna.write("Attenzione!!! separare tutto con ; (ex. scarico;velocità,streatching,allunghi;18:00)",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("              separare la scrittura dell'allenamento con le virgole(ex. 40 minuti di corsa,streatching,allunghi",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("              in riposo mettere --> riposo;RIPOSO;----",font=("Arial",20, "normal"))
    Penna.forward(40)
    Penna.write("Colori-allenamenti: scarico=pallino Verde",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("                    lavoro=pallino Blu",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("                    palestra=pallino Marrone",font=("Arial",20, "normal"))
    Penna.forward(25)
    Penna.write("                    salite=pallino Giallo",font=("Arial",20, "normal"))
    Penna.forward(50)
    Penna.write("Tra    inizierà il programma...",font=("Arial",20, "normal"))
    Penna.goto(540,-345)
    Penna.hideturtle()
    Penna.write("@copyright Michael Tezza")
    Penna.goto(-600,-110)
    n=20
    Penna_2=turtle.Turtle()
    Penna_2.penup()
    Penna_2.goto(-607,-210)
    Penna_2.pendown()
    Penna_2.right(90)
    Penna_2.forward(30)
    Penna_2.left(90)
    Penna_2.forward(1200)
    Penna_2.left(90)
    Penna_2.forward(30)
    Penna_2.left(90)
    Penna_2.forward(1200)
    Penna_2.pencolor("red")
    Penna_2.hideturtle()
    Penna_2.penup()
    Penna_2.goto(-607,-210)
    Penna_2.left(90)
    Penna_2.forward(30)
    Penna_2.left(90)
    Penna_2.pendown()
    for i in range(20):
        Penna_2.pendown()
        Penna.write(n)
        Penna_2.forward(1200/20) # Cambiare solo se difficile da leggere
        Penna_2.left(90)
        Penna_2.forward(30)
        Penna_2.left(90)
        Penna_2.forward(1200/20) # Cambiare solo se difficile da leggere
        Penna_2.left(90)
        Penna_2.forward(30)
        Penna_2.left(90)
        Penna_2.forward(1200/20) # Cambiare solo se difficile da leggere
        #time.sleep(1)
        Penna.dot(30,"blue")
        n -= 1
    record(filename = "record.csv")
    Tabella_allenamenti()
            

def Index ():
    print("Benvenuti nel calendario riservato agli atleti italiani")
    print("Qui potrai,tramite un file csv,inserire gli allenamenti mensili")
    print("Inserire nel file csv: cosa c'è da fare tra [scarico,lavoro,palestra,salite,gara,riposo]")
    print("                       scrivi l'allenamento")
    print("                       e orario (ex. come 18:00)")
    print("Attenzione!!! separare tutto con ; (ex. scarico;40 minuti di corsa;18:00)")
    print("              in riposo mettere --> riposo;RIPOSO;----")
    print("Colori-allenamenti: scarico=pallino Verde")
    print("                    lavoro=pallino Blu")
    print("                    palestra=pallino Marrone")
    print("                    salite=pallino Giallo")
    print("                    gara=pallino Rosso")
    print("                    riposo=pallino Bianco")


    print("Al termine della giornata,se hai fatto un record potrai scriverlo nel file csv")
    record(filename = "record.csv")
def Tabella_allenamenti() :
    clearscreen()
    anno,mese,giorno,orario_attuale=oggi()
    anno= int(anno)
    mese_1=int(mese)
    day=int(giorno)
    Penna=turtle.Turtle()
    Penna.hideturtle()
    Penna.penup()
    Penna.goto(-650,-340)
    Penna.pendown()
    Penna.speed(0)
    
    giorno=1
    for i in range(5):
        n_colonna=1
        for i in range(7): # 5 righe e 7 colonne
            Penna.forward(185*n_colonna)
            Penna.left(90)
            Penna.forward(136)
            Penna.penup()
            Penna.forward(-36)
            Penna.right(90)
            Penna.forward(-36)
            if mese== "01" or mese== "03" or mese== "05" or mese== "07" or mese== "08" or mese== "10" or mese== "12" :
                mese_giorni= 31
                if giorno < 32:
                    if giorno == day :
                        giorno_settimana=settimana(anno,mese_1,giorno)
                        Penna.pencolor("red")
                        Penna.write(giorno,font=("Arial",20, "normal"))
                        Penna.pencolor("black")
                        Penna.right(180)
                        Penna.forward(20)
                        Penna.left(90)
                        Penna.forward(10)
                        Penna.write(giorno_settimana)
                        Penna.forward(-10)
                        Penna.left(-90)
                        Penna.forward(-20)
                        Penna.right(-180)
                        for i in open("allenamento.csv"):
                            attività,allenamento,orario=i.split(";")
                            print(orario)
                            print(orario_attuale)
                        
                    else :
                        giorno_settimana=settimana(anno,mese_1,giorno)
                        Penna.write(giorno)
                        Penna.right(180)
                        Penna.forward(20)
                        Penna.left(90)
                        Penna.forward(10)
                        Penna.write(giorno_settimana)
                        Penna.forward(-10)
                        Penna.left(-90)
                        Penna.forward(-20)
                        Penna.right(-180)
                else:
                    Penna.write("-")
            elif mese == "02" :
                if anno%4 ==0 :
                    if anno%100==0:
                        if anno%400==0:
                            if giorno < 30:
                                mese_giorni= 29
                                if giorno == day :
                                    giorno_settimana=settimana(anno,mese_1,giorno)
                                    Penna.pencolor("red")
                                    Penna.write(giorno,font=("Arial",20, "normal"))
                                    Penna.pencolor("black")
                                    Penna.right(180)
                                    Penna.forward(20)
                                    Penna.left(90)
                                    Penna.forward(10)
                                    Penna.write(giorno_settimana)
                                    Penna.forward(-10)
                                    Penna.left(-90)
                                    Penna.forward(-20)
                                    Penna.right(-180)
                                else :
                                    giorno_settimana=settimana(anno,mese_1,giorno)
                                    Penna.write(giorno)
                                    Penna.right(180)
                                    Penna.forward(20)
                                    Penna.left(90)
                                    Penna.forward(10)
                                    Penna.write(giorno_settimana)
                                    Penna.forward(-10)
                                    Penna.left(-90)
                                    Penna.forward(-20)
                                    Penna.right(-180)
                            else:
                                Penna.write("-")
                        else:
                            if giorno < 29:
                                mese_giorni= 28
                                if giorno == day :
                                    giorno_settimana=settimana(anno,mese_1,giorno)
                                    Penna.pencolor("red")
                                    Penna.write(giorno,font=("Arial",20, "normal"))
                                    Penna.pencolor("black")
                                    Penna.right(180)
                                    Penna.forward(20)
                                    Penna.left(90)
                                    Penna.forward(10)
                                    Penna.write(giorno_settimana)
                                    Penna.forward(-10)
                                    Penna.left(-90)
                                    Penna.forward(-20)
                                    Penna.right(-180)
                                else :
                                    giorno_settimana=settimana(anno,mese_1,giorno)
                                    Penna.write(giorno)
                                    Penna.right(180)
                                    Penna.forward(20)
                                    Penna.left(90)
                                    Penna.forward(10)
                                    Penna.write(giorno_settimana)
                                    Penna.forward(-10)
                                    Penna.left(-90)
                                    Penna.forward(-20)
                                    Penna.right(-180)
                            else:
                                Penna.write("-")
                    else:
                        if giorno < 30:
                            mese_giorni= 29
                            if giorno == day :
                                giorno_settimana=settimana(anno,mese_1,giorno)
                                Penna.pencolor("red")
                                Penna.write(giorno,font=("Arial", 20, "normal"))
                                Penna.pencolor("black")
                                Penna.right(180)
                                Penna.forward(20)
                                Penna.left(90)
                                Penna.forward(10)
                                Penna.write(giorno_settimana)
                                Penna.forward(-10)
                                Penna.left(-90)
                                Penna.forward(-20)
                                Penna.right(-180)
                            else :
                                giorno_settimana=settimana(anno,mese_1,giorno)
                                Penna.write(giorno)
                                Penna.right(180)
                                Penna.forward(20)
                                Penna.left(90)
                                Penna.forward(10)
                                Penna.write(giorno_settimana)
                                Penna.forward(-10)
                                Penna.left(-90)
                                Penna.forward(-20)
                                Penna.right(-180)
                        else:
                            Penna.write("-")
                else:
                    if giorno < 29:
                        mese_giorni= 28
                        if giorno == day :
                            giorno_settimana=settimana(anno,mese_1,giorno)
                            Penna.pencolor("red")
                            Penna.write(giorno,font=("Arial", 20, "normal"))
                            Penna.pencolor("black")
                            Penna.right(180)
                            Penna.forward(20)
                            Penna.left(90)
                            Penna.forward(10)
                            Penna.write(giorno_settimana)
                            Penna.forward(-10)
                            Penna.left(-90)
                            Penna.forward(-20)
                            Penna.right(-180)
                        else :
                            giorno_settimana=settimana(anno,mese_1,giorno)
                            Penna.write(giorno)
                            Penna.right(180)
                            Penna.forward(20)
                            Penna.left(90)
                            Penna.forward(10)
                            Penna.write(giorno_settimana)
                            Penna.forward(-10)
                            Penna.left(-90)
                            Penna.forward(-20)
                            Penna.right(-180)
                    else:
                        Penna.write("-")
            elif mese =="04" or mese== "06" or mese== "09" or mese== "11":
                if giorno < 31:
                    mese_giorni= 30
                    if giorno == day :
                        giorno_settimana=settimana(anno,mese_1,giorno)
                        Penna.pencolor("red")
                        Penna.write(giorno,font=("Arial", 20, "normal"))
                        Penna.pencolor("black")
                        Penna.right(180)
                        Penna.forward(20)
                        Penna.left(90)
                        Penna.forward(10)
                        Penna.write(giorno_settimana)
                        Penna.forward(-10)
                        Penna.left(-90)
                        Penna.forward(-20)
                        Penna.right(-180)
                    else :
                        giorno_settimana=settimana(anno,mese_1,giorno)
                        Penna.write(giorno)
                        Penna.right(180)
                        Penna.forward(20)
                        Penna.left(90)
                        Penna.forward(10)
                        Penna.write(giorno_settimana)
                        Penna.forward(-10)
                        Penna.left(-90)
                        Penna.forward(-20)
                        Penna.right(-180)
                else:
                    Penna.write("-")
            Penna.forward(+36)
            Penna.left(90)
            Penna.forward(36)
            Penna.left(90)
            Penna.pendown()
            color=colori(filename="allenamento.csv")
            orari=orario1("allenamento.csv")
            allenamenti=allenamento1(filename="allenamento.csv")
            numero=1
            for i in range(n_colonna):
                Penna.forward(185)
                Penna.penup()
                Penna.left(90)
                Penna.forward(15)
                Penna.left(90)
                Penna.forward(15)
                if numero == 1 and giorno <=mese_giorni:
                    a=False
                    Penna.dot(20,color[giorno-1])
                    numero = 0
                    Penna.forward(15)
                    Penna.write(str(orari[giorno-1]))
                    Penna.right(90)
                    Penna.forward(40)
                    for i in allenamenti[giorno-1]:
                        if i ==",":
                            a=True
                    if a==True :
                        spazio=0
                        allenamenti[giorno-1].split(",")
                        for i in allenamenti[giorno-1].split(","):
                            Penna.write(i)
                            Penna.forward(10)
                            spazio-=10
                        Penna.forward(spazio)
                    else:
                        Penna.write(allenamenti[giorno-1])
                    Penna.forward(-40)
                    Penna.right(-90)
                    Penna.forward(-15)
                    
                Penna.forward(-15)
                Penna.right(90)
                Penna.forward(-15)
                Penna.right(90)
                Penna.pendown()
            Penna.left(90)
            Penna.forward(136)
            Penna.left(90)
            n_colonna+=1
            giorno+=1
        Penna.left(90)
        Penna.forward(136)
        Penna.right(90)

def colori(filename="allenamento.csv"):
    color=[]
    for i in open(filename):
        attività,allenamento,orario=i.split(";")
        if attività== "scarico":
            color.append("green")
        elif attività== "lavoro":
            color.append("blue")
        elif attività =="palestra":
            color.append("brown")
        elif attività =="gara":
            color.append("red")
        elif attività =="salite":
            color.append("yellow")
        elif attività =="riposo":
            color.append("white")
    return color

def orario1(filename):
    orari=[]
    for i in open(filename):
        attività,allenamento,orario=i.split(";")
        if orario[-1] == "\n" :
            orario=orario[:-1]
        orari.append(str(orario))
    return orari

def oggi():
    data=date.today()
    anno,mese,giorno=str(data).split("-")
    orario=datetime.datetime.time(datetime.datetime.now())
    ora,minuti,secondi=str(orario).split(":")
    orario_attuale=ora+":"+minuti
    return anno,mese,giorno,orario_attuale

def settimana(anno,mese_1,giorno):
    num=date(anno,mese_1,giorno).weekday()
    if num == 0:
        giorno_settimana="Lunedì"
    elif num == 1:
        giorno_settimana="Martedì"
    elif num == 2:
        giorno_settimana="Mercoledì"
    elif num == 3:
        giorno_settimana="Giovedì"
    elif num == 4:
        giorno_settimana="Venerdì"
    elif num == 5:
        giorno_settimana="Sabato"
    elif num == 6:
        giorno_settimana="Domenica"
    return giorno_settimana
def allenamento1(filename="allenamento.csv"):
    allenamenti=[]
    for i in open(filename):
        attività,allenamento,orario=i.split(";")
        allenamenti.append(allenamento)
    return allenamenti

def record(filename="record.csv"):
    print("I tuoi RECORD")
    for i in open(filename):
        misura,tempo=i.split(";")
        print(misura,"--->",tempo)
if __name__=="__main__":
    from turtle import bgcolor,title,clearscreen,onscreenclick
    import turtle
    from datetime import date
    import datetime
    import time
    Index()
    Cambio_record = input("Vuoi aggiungere un record? ")

    if record == "si" or record == "SI" :
        a = open("record.csv","a")
        misura_mod = input("Che misura vuoi modificare? ")
        for i in open("record.csv"):
            misura,tempo=i.split(";")
            if misura == misura_mood :
                tempo_mod = input("Dimmi il tempo: ")
                a.write(a)#finire
        
        
        
    #Index_1()
    #print(colori(filename="allenamento.csv"))
    #Tabella_allenamenti()
    #print(orario(filename="allenamento.csv"))
    #print(allenamento(filename="allenamento.csv"))
    #print(oggi())
    
