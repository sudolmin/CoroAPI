import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.font import Font
import time
import country_list
from tkinter import messagebox

class corona_update:

    def  __init__(self):
        self.root = Tk()
        
        self.root.resizable(False,False)
        self.root.geometry('500x400+400+200')
        
        self.country_name = 'india'
        
        self.updates()
        
    def updates(self):
        self.root.title('CoroAPP - %s'%(self.country_name).title())
        

        try:
            self.main_frame = Frame(self.root, width = 500, height = 400,bg = 'midnight blue').place(x=0,y=0)

            self.ref_b = Button(self.root,text= '  Refresh  ', command = self.updates).place(x=35,y=375)

            self.co = Entry(self.root, justify =CENTER)
            #print(type(self.co))
            self.co.place(x=267,y=377)
            #print(type(self.co))
            
            self.search = Button(self.root,text= '  Search  ', command = self.coun).place(x=400,y=375)
            
            self.fr_cfmd = Frame(self.root, width = 500, height = 125, bg = 'paleturquoise3', relief =RAISED, bd=4).place(x=0,y=0)
        
        
            self.fr_succ = Frame(self.root, width = 250, height = 125, bg = 'pale green', relief =RAISED, bd=4).place(x=0,y=125)
            
            
            self.fr_dang = Frame(self.root, width = 250, height = 125, bg = 'light coral', relief =RAISED, bd=4).place(x=250,y=125)
            
            
            self.fr_info = Frame(self.root, width = 500, height = 125, bg = 'khaki1', relief =RAISED, bd=4).place(x=0,y=250)
            
            self.ul = 'https://corona.help/country/%s'%(self.country_name)
            self.page=requests.get(self.ul)
            self.soup=BeautifulSoup(self.page.content,'html.parser')
            
            self.confirmed_case = self.soup.find_all('h2',class_="text-bold-700 warning")
            self.cfmd = str(self.confirmed_case).split('<')[1].split('>')[1]

            self.cfmd1 = Label(self.fr_cfmd,
                             font=Font(family="Copperplate Gothic Light",size=25),
                             fg='blue4',bg='paleturquoise3',
                             text=' Total Confirmed Cases: ').place(x=20,y=10)
            
            self.cfmd2 = Label(self.fr_cfmd,
                             font=Font(family="Copperplate Gothic Light",size=40),
                             fg='blue4',bg='paleturquoise3',
                             text=self.cfmd).place(x=120,y=50)

            self.recoveries = self.soup.find_all('h2',class_="text-bold-700 success")

            self.rcvr =  str(self.recoveries).split('<')[1].split('>')[1]

            self.rcvr1 = Label(self.fr_succ,
                             font=Font(family="Copperplate Gothic Light",size=14),
                             fg='blue4',bg='pale green',
                             text='Confirmed Recoveries:').place(x=4,y=129)
            
            self.rcvr2 = Label(self.fr_succ,
                             font=Font(family="Copperplate Gothic Light",size=30),
                             fg='blue4',bg='pale green',
                             text=self.rcvr).place(x=60,y=170)
            
            self.deaths = self.soup.find_all('h2',class_="text-bold-700 danger")
            self.t_de = (str(self.deaths).split('<')[1].split('>')[1])

            self.t_de1 = Label(self.fr_dang,
                             font=Font(family="Copperplate Gothic Light",size=18),
                             fg='blue4',bg='light coral',
                             text='Total Deaths:').place(x=280,y=129)
            
            self.t_de2 = Label(self.fr_dang,
                             font=Font(family="Copperplate Gothic Light",size=30),
                             fg='blue4',bg='light coral',
                             text=self.t_de).place(x=300,y=170)
            
            
            self.active_case = self.soup.find_all('h2',class_="text-bold-700 info")

            self.accs =  str(self.active_case).split('<')[1].split('>')[1]
            self.accs1 = Label(self.fr_info,
                             font=Font(family="Copperplate Gothic Light",size=25),
                             fg='blue4',bg='khaki1',
                             text='Total Active Cases:').place(x=80,y=259)
            
            self.accs2 = Label(self.fr_info,
                             font=Font(family="Copperplate Gothic Light",size=40),
                             fg='blue4',bg='khaki1',
                             text=self.accs).place(x=120,y=300)
            ti = Label(self.main_frame, font=Font(family="Corbel",size=12),
                             fg='khaki1',bg='midnight blue',
                             text=time.strftime('%I:%M %p')).place(x=145,y=375)
        except:
            self.noCEF = Frame(self.root, width = 500, height = 400,bg = 'light coral').place(x=0,y=0)
            self.noce1 = Label(self.noCEF, text='\n\n  NO CONNECTION!!!!!',font=Font(family="Copperplate Gothic Light",size=30),
                             fg='red',bg='light coral').grid(row=1,column=1)
            self.noce2 = Label(self.noCEF, text='\nConnect to Internet',font=Font(family="Copperplate Gothic Light",size=25),
                             fg='red',bg='light coral').grid(row=3,column=1)
            self.ref_b = Button(self.root,text= '  Refresh  ', command = self.updates).place(x=220,y=300)
        

    def info(self):
        self.ty =''' Please Enter Valid Country Name.
(E.g - United States >> united-states)'''
        messagebox.showinfo('Input Error', self.ty)
    def coun(self):
        self.country_name = str(self.co.get())
        self.country_name = self.country_name.lower()
        if self.country_name in country_list.co_list:
            self.co.delete(0,END)
            
            self.updates()
        else:
            self.co.delete(0,END)
            self.info()
            
obj=corona_update()
obj.root.iconbitmap('covid.ico')
obj.root.mainloop()
