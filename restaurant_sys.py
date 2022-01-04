import sys
from tkinter import ttk
from tkinter import * 
import tkinter.font
import time
import random

#-----functions--------------------

def reciept():
    textReceipt.delete(1.0,END)
    x = random.randint(100,10000)
    billnumber='BILL'+str(x)
    date = time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Reciept ref: \t\t'+ billnumber+'\t\t'+date+'\n')
    textReceipt.insert(END, '***************************************************************\n')
    textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
    textReceipt.insert(END,'***************************************************************\n')
    if e_roti.get()!='0':
        textReceipt.insert(END, f'Roti\t\t\t{int(e_roti.get())+10}\n\n')
    if e_dal.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_dal.get())+90}\n\n')
    if e_fish.get()!='0':
        textReceipt.insert(END, f'FISH\t\t\t{int(e_fish.get())+150}\n\n')
    if e_chicken.get()!='0':
        textReceipt.insert(END, f'CHICKEN\t\t\t{int(e_chicken.get())+250}\n\n')
    if e_noodles.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_noodles.get())+150}\n\n')
    if e_pizza.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_pizza.get())+200}\n\n')
    if e_dosa.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_dosa.get())+120}\n\n')
    if e_idli.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_idli.get())+100}\n\n')
    if e_manchurian.get()!='0':
        textReceipt.insert(END, f'DAAL\t\t\t{int(e_manchurian.get())+120}\n\n')
    
def Totalcost():
    item1=int(e_roti.get())
    item2=int(e_dal.get())
    item3=int(e_fish.get())
    item4=int(e_chicken.get())
    item5=int(e_noodles.get())
    item6=int(e_pizza.get())
    item7=int(e_dosa.get())
    item8=int(e_idli.get())
    item9=int(e_manchurian.get())

    item10=int(e_faluda.get())
    item11=int(e_fanta.get())
    item12=int(e_coke.get())
    item13=int(e_moito.get())
    item14=int(e_coffee.get())
    item15=int(e_tea.get())
    item16=int(e_sprite.get())
    item17=int(e_lemonade.get())
    item18=int(e_icetea.get())

    item19=int(e_oreo.get())
    item20=int(e_kitkat.get())
    item21=int(e_vanilla.get())
    item22=int(e_apple.get())
    item23=int(e_blackforest.get())
    item24=int(e_banana.get())
    item25=int(e_brownie.get())
    item26=int(e_pineapple.get())
    item27=int(e_chocolate.get())

    priceofFood=(item1*10)+(item2*90)+(item3*150)+(item4*250)+ (item5*150) + (item6 * 200) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

    priceofDrinks=(item10*120)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 150)

    priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

    costoffoodvar.set(str(priceofFood)+ ' Rs')
    costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
    costofcakesvar.set(str(priceofCakes)+ ' Rs')


    subtotalofItems=priceofFood+priceofDrinks+priceofCakes
    subtotalvar.set(str(subtotalofItems)+' Rs')

    servicetaxvar.set('50 Rs')

    tottalcost=subtotalofItems+50
    totalcostvar.set(str(tottalcost)+' Rs')


def Roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def Daal():
    if var2.get()==1:
        textdal.config(state=NORMAL)
        textdal.delete(0,END)
        textdal.focus()
    elif var2.get()==0:
        textdal.config(state=DISABLED)
        e_dal.set('0')

def Fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    elif var3.get()==0:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def Chicken():
    if var4.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    elif var4.get()==0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')
def noodle():
    if var5.get()==1:
        textnoodles.config(state=NORMAL)
        textnoodles.delete(0,END)
        textnoodles.focus()
    elif var5.get()==0:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')
def Pizza():
    if var6.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete(0,END)
        textpizza.focus()
    elif var6.get()==0:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')

def Dosa():
    if var7.get()==1:
        textdosa.config(state=NORMAL)
        textdosa.delete(0,END)
        textdosa.focus()
    elif var7.get()==0:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')

def Idli():
    if var8.get()==1:
        textidli.config(state=NORMAL)
        textidli.delete(0,END)
        textidli.focus()
    elif var8.get()==0:
        textidli.config(state=DISABLED)
        e_idli.set('0')

def Manchurian():
    if var9.get()==1:
        textmanchurian.config(state=NORMAL)
        textmanchurian.delete(0,END)
        textmanchurian.focus()
    elif var9.get()==0:
        textmanchurian.config(state=DISABLED)
        e_manchurian.set('0')
#------------------------------------

def Faluda():
    if var10.get()==1:
        textFaluda.config(state=NORMAL)
        textFaluda.delete(0,END)
        textFaluda.focus()
    elif var10.get()==0:
        textFaluda.config(state=DISABLED)
        e_faluda.set('0')
        
def Fanta():
    if var11.get()==1:
        textfanta.config(state=NORMAL)
        textfanta.delete(0,END)
        textfanta.focus()
    elif var11.get()==0:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')
        
def Coke():
    if var12.get()==1:
        textcoke.config(state=NORMAL)
        textcoke.delete(0,END)
        textcoke.focus()
    elif var12.get()==0:
        textcoke.config(state=DISABLED)
        e_coke.set('0')
        
def Coffee():
    if var13.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    elif var13.get()==0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

        
def Tea():
    if var14.get()==1:
        textea.config(state=NORMAL)
        textea.delete(0,END)
        textea.focus()
    elif var14.get()==0:
        textea.config(state=DISABLED)
        e_tea.set('0')
        
def Sprite():
    if var15.get()==1:
        textsprite.config(state=NORMAL)
        textsprite.delete(0,END)
        textsprite.focus()
    elif var15.get()==0:
        textsprite.config(state=DISABLED)
        e_sprite.set('0')

        
def Lemonade():
    if var16.get()==1:
        textlemonade.config(state=NORMAL)
        textlemonade.delete(0,END)
        textlemonade.focus()
    elif var16.get()==0:
        textlemonade.config(state=DISABLED)
        e_lemonade.set('0')

        
def Icetea():
    if var17.get()==1:
        texticetea.config(state=NORMAL)
        texticetea.delete(0,END)
        texticetea.focus()
    elif var17.get()==0:
        texticetea.config(state=DISABLED)
        e_icetea.set('0')
        
def Moito():
    if var18.get()==1:
        textmoito.config(state=NORMAL)
        textmoito.delete(0,END)
        textmoito.focus()
    elif var18.get()==0:
        textmoito.config(state=DISABLED)
        e_moito.set('0')

#---------------------------------------------
def Oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    elif var19.get()==0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def Kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    elif var20.get()==0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def Vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    elif var21.get()==0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def Apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    elif var22.get()==0:
        textapple.config(state=DISABLED)
        e_apple.set('0')

def Black():
    if var27.get()==1:
        textblack.config(state=NORMAL)
        textblack.delete(0,END)
        textblack.focus()
    elif var23.get()==0:
        textblack.config(state=DISABLED)
        e_blackforest.set('0')

def Banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    elif var24.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def Brownie():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    elif var25.get()==0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')       

def Pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    elif var26.get()==0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0') 

def Choclate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    elif var27.get()==0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')    
window = Tk()

window.geometry("1270x690+0+0")

window.wm_resizable(0,0) 

window.title('Restaurent management system')

window.configure(bg = 'dark turquoise')

topFrame = Frame(window, bd=10, relief=RIDGE,bg='dark turquoise')

topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text = 'Restaurant Management System', font = ('arial',30,'bold'), fg='gray15',bg='gold',
                    border=9,width= 51 )
labelTitle.grid(row=0, column=0)


#frame

menuFrame=Frame(window,bd=10,relief=RIDGE,bg='dark turquoise')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame,bd=4,relief=RIDGE, bg='gold')
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'), bd=10,relief=RIDGE)
foodFrame.pack(side=LEFT)

drinkFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'), bd=10,relief=RIDGE)
drinkFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'), bd=10,relief=RIDGE)
cakesFrame.pack(side=LEFT) 
  
rightFrame=Frame(window,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack()

recieptFrame=Frame(rightFrame, bd=4,relief=RIDGE)
recieptFrame.pack()

buttonFrame=Frame(rightFrame, bd=3,relief=RIDGE)
buttonFrame.pack()


#variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()

var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar() 

var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar() 

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti=StringVar()
e_dal=StringVar()
e_fish=StringVar()
e_chicken=StringVar()
e_noodles=StringVar()
e_pizza=StringVar()
e_dosa=StringVar()
e_idli=StringVar()
e_manchurian=StringVar()

e_faluda=StringVar()
e_fanta=StringVar()
e_coke=StringVar()
e_coffee=StringVar()
e_tea=StringVar()
e_sprite=StringVar()
e_lemonade=StringVar()
e_icetea=StringVar()
e_moito=StringVar()

e_oreo=StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

#---------------------------------
e_roti.set('0')
e_dal.set('0')
e_fish.set('0')
e_chicken.set('0')
e_noodles.set('0')
e_pizza.set('0')
e_dosa.set('0')
e_idli.set('0')
e_manchurian.set('0')

e_faluda.set('0')
e_fanta.set('0')
e_coke.set('0')
e_coffee.set('0')
e_tea.set('0')
e_sprite.set('0')
e_lemonade.set('0')
e_icetea.set('0')
e_moito.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0') 

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar() 

##FOOD

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var1, command=Roti)
roti.grid(row=0, column=0, sticky = W)

dal=Checkbutton(foodFrame,text='Dal',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var2, command=Daal)
dal.grid(row=1, column=0, sticky = W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var3, command=Fish)
fish.grid(row=2, column=0, sticky = W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var4, command=Chicken)
chicken.grid(row=3, column=0, sticky = W)

noodles=Checkbutton(foodFrame,text='Noodles',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var5, command=noodle)
noodles.grid(row=4, column=0, sticky = W)

pizza=Checkbutton(foodFrame,text='Pizza',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var6, command=Pizza)
pizza.grid(row=5, column=0, sticky = W)

dosa=Checkbutton(foodFrame,text='Dosa',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var7, command=Dosa)
dosa.grid(row=6, column=0, sticky = W)

idli=Checkbutton(foodFrame,text='Idli',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var8, command=Idli)
idli.grid(row=7, column=0, sticky = W)

manchurian=Checkbutton(foodFrame,text='Manchurian',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var9, command=Manchurian)
manchurian.grid(row=8, column=0, sticky = W)

#entry button
textroti=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED, textvariable = e_roti ) 
textroti.grid(row=0, column=1)

textdal=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_dal)
textdal.grid(row=1, column=1)

textfish=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_fish ) 
textfish.grid(row=2, column=1)

textchicken=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_chicken )
textchicken.grid(row=3, column=1)

textnoodles=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_noodles)
textnoodles.grid(row=4, column=1)

textpizza=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_pizza)
textpizza.grid(row=5, column=1)

textdosa=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_dosa)
textdosa.grid(row=6, column=1)

textidli=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_idli )
textidli.grid(row=7, column=1)

textmanchurian=Entry(foodFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_manchurian )
textmanchurian.grid(row=8, column=1)

#drinks
faluda=Checkbutton(drinkFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var10, command=Faluda)
faluda.grid(row=0, column=0, sticky = W)

Fanta=Checkbutton(drinkFrame,text='Fanta',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var11,command=Fanta)
Fanta.grid(row=1, column=0, sticky = W)

coke=Checkbutton(drinkFrame,text='Coke',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var12,command=Coke)
coke.grid(row=2, column=0, sticky = W)

coffee=Checkbutton(drinkFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var13,command=Coffee)
coffee.grid(row=3, column=0, sticky = W)

tea=Checkbutton(drinkFrame,text='Tea',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var14,command=Tea)
tea.grid(row=4, column=0, sticky = W)

sprite=Checkbutton(drinkFrame,text='Sprite',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var15,command=Sprite)
sprite.grid(row=5, column=0, sticky = W)

lemonade=Checkbutton(drinkFrame,text='Lemonade',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var16,command=Lemonade)
lemonade.grid(row=6, column=0, sticky = W)

icetea=Checkbutton(drinkFrame,text='Ice Tea',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var17,command=Icetea)
icetea.grid(row=7, column=0, sticky = W)

moito=Checkbutton(drinkFrame,text='Moito ',font=('arial',18,'bold'),onvalue=1, offvalue=0,variable=var18, command=Moito)
moito.grid(row=8, column=0, sticky = W)
#-----------------------------------------------------------------------------------------------------------
textfaluda=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_faluda)
textfaluda.grid(row=0, column=1)

textfanta=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_fanta )
textfanta.grid(row=1, column=1)

textcoke=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_coke )
textcoke.grid(row=2, column=1)

textcoffee=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_coffee )
textcoffee.grid(row=3, column=1)

textea=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_tea)
textea.grid(row=4, column=1)

textsprite=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_sprite )
textsprite.grid(row=5, column=1)

textlemonade=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_lemonade )
textlemonade.grid(row=6, column=1)

texticetea=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_icetea )
texticetea.grid(row=7, column=1)

textmoito=Entry(drinkFrame,font = ('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable = e_moito )
textmoito.grid(row=8, column=1)
#---cakes--------------------------------------------------------------------------------------------------------

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=Oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=Apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=Kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=Vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=Banana)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=Brownie)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=Pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=Choclate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=Black)
blackforestcake.grid(row=8,column=0,sticky=W) 

#entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblack = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblack.grid(row=8, column=1)

#------cost label and entry feilds-------------

labelcostfood=Label(costFrame, text='Cost of food', font=('arial',16,'bold'), bg='gold', fg='black')
labelcostfood.grid(row=0, column=0)

textfood = Entry(costFrame, font=('arial', 18, 'bold'),bd=6, width=14, state='readonly',  textvariable=costoffoodvar)
textfood.grid(row=0,column=1,padx=41)

labelcostofdrink = Label(costFrame, text = 'Cost of drinks', font=('arial',16,'bold'), bg='gold', fg='black')
labelcostofdrink.grid(row =1, column=0)

textdrink = Entry(costFrame, font=('arial', 18, 'bold'),bd=6, width=14, state='readonly',  textvariable=costofdrinksvar)
textdrink.grid(row=1,column=1,padx=41)

labelcostofcake = Label(costFrame, text = 'Cost of Cake', font=('arial',16,'bold'), bg='gold', fg='black')
labelcostofcake.grid(row =2, column=0)

textcake = Entry(costFrame, font=('arial', 18, 'bold'),bd=6, width=14, state='readonly',  textvariable=costofdrinksvar)
textcake.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='gold',fg='black')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='gold',fg='black')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='gold',fg='black')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0) 

#===buttons====

buttontotal = Button(buttonFrame, text = 'Total', font=('arial',14,'bold'),bg='gold',fg='black', bd= 3,command=Totalcost)
buttontotal.grid(row=0, column=0)

buttonreciept = Button(buttonFrame, text = 'Reciept', font=('arial',14,'bold'),bg='gold',fg='black', bd= 3, command=reciept)
buttonreciept.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text = 'Save', font=('arial',14,'bold'),bg='gold',fg='black', bd= 3)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text = 'Send', font=('arial',14,'bold'),bg='gold',fg='black', bd= 3)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text = 'Reset', font=('arial',14,'bold'),bg='gold',fg='black', bd= 3)
buttonReset.grid(row=0, column=4)

#text area for reciept


#calculator
operator ='' #7+9
def buttonClick(numbers):
    global operator
    operator=operator+numbers #7+9
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def Clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0, result)
    operator=''

calculatorField=Entry(calculatorFrame, font=('arial',16,'bold'), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               ,command = lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               , command = lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               , command = lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                  , command = lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               , command = lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               , command = lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               , command = lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                   , command = lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               , command = lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               , command = lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               , command = lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                  , command = lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                 ,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                   , command=Clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
               , command = lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='black',bg='gold',bd=6,width=6
                 , command = lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)


window.mainloop()


