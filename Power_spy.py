import psutil
#from playsound import playsound
#from win10toast import ToastNotifier
from win10toast_click import ToastNotifier
import time
import threading
black="black"
import ttkbootstrap
#from ttkbootstrap.constants import *
#from random import randrange
#from ttkbootstrap.tooltip import ToolTip
possible_themes="vapor"
break_taking=[False,]
def take_an_break():
    #print("i take a break")
    break_taking[0]=True
    time.sleep(300)
    break_taking[0]=False
    #print("End of break")

def run():
    threading.Thread(target=take_an_break).start()

notification=ToastNotifier()
def about_Fred():
    
    red="red"
    yellow="yellow"
    bg="black"
    bg=bg
    fred=ttkbootstrap.Window(title="About Energy Spy",resizable=(False,False))
    label=ttkbootstrap.Label(fred,text="Energy_Spy was Developped By Achméle@Fred 2024 All Right Reserved",font=("Bold",10),foreground=red,background=bg)
    label.place(x=10,y=10)
    fred.config(background=bg)
    label2=ttkbootstrap.Label(fred,text="Thanks you to use Energy_Spy !",font=("Bold",20),foreground=yellow,background=bg)
    label2.place(x=60,y=100)
    fred.geometry("700x200")
    fred.after(7000,fred.destroy)
    fred.mainloop()
def run_about_fred():
    threading.Thread(target=about_Fred).start()
def more():
    theme=possible_themes
    screen=ttkbootstrap.Window(title="Energy_Spy",resizable=(False,False))
    #black="black"
    bg="black"
    bg=bg
    screen.configure(background=bg)
    red="red"
    yellow="yellow"
    green="green"
    screen.geometry("600x200")
    menu=ttkbootstrap.Menu(border=3)
    menu.add_command(label="About Energy_Spy",command=lambda:run_about_fred())
    screen.config(menu=menu)
    label1=ttkbootstrap.Label(screen,background=bg,text="Energy Spy",font=("Bold",15),foreground=red)
    label2=ttkbootstrap.Label(screen,background=bg,text="Energy Spy is so boring ??:",font=("arial",13),foreground=yellow)
    but=ttkbootstrap.Button(screen,text="Take an break",command=lambda:run(),bootstyle="btn-outline-danger")
    label3=ttkbootstrap.Label(screen,background=bg,text="Running...",font=("arial",12),foreground=green)
    label1.place(x=200,y=5)
    label2.place(x=70,y=140)
    label3.place(x=30,y=67)
    but.place(x=400,y=140)
    running=ttkbootstrap.Progressbar(length=300,mode=["determinate"])
    running.start(73)
    running.place(x=190,y=70)
    screen.after(8000,screen.destroy)
    screen.mainloop()

def run_more():
    threading.Thread(target=more).start()

def more_than_80():
    try:notification.show_toast(
        "Nova",
        "Fred,Please ckeck power percent And disconnect Alimentation Quicklly !! height Batterie: "+str(power),
        duration=5,
        callback_on_click=run_more,
        threaded=True
        )
    except:pass
   # playsound("memories.mp3")
    
def less_than_20():
    try:notification.show_toast(
        "Nova",
        "Fred,Please check power percent And Connect Alimentation Quicklly !! Low Batterie: "+str(power),
        duration=5,
        callback_on_click=run_more,
        threaded=True
        )
    except:pass
   # playsound("memories.mp3")
try:notification.show_toast(
    "Nova",
    "Nova launch Energy_spy successfully !!",
    duration=3
    )
except:print("Can't show the Toast")
#print("Nova Running ")
def for_more(power):
    if baterie.power_plugged and power >= 80 :
        return 5
    else:
        return 300
def for_less(power):
    if 20 >= power and not baterie.power_plugged :
        return 15
    else:
        return 300
while True:
    print(break_taking)
    if not break_taking[0]:
        duree=300
        baterie=psutil.sensors_battery()

        power=baterie.percent
        power#la bat
        baterie.power_plugged #True if en charge
        

        #print("power:"+str(power)+"Connected:"+str(baterie.power_plugged)) No needed 
        if power >= 80 and baterie.power_plugged:
            more_than_80()
            duree=for_more(power)
            
        if 20 >= power and not baterie.power_plugged :
            less_than_20()
            duree=for_less(power)
        print(duree)
    time.sleep(duree)