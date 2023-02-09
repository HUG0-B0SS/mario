from tkinter import *
from tkinter import filedialog, simpledialog

vastuvoetud=[]
aastad=[2011,2012,2013,2014,2015,2016,2017,2018,2019]

def failivalik():
    nupp.place_forget()
    failinimi=filedialog.askopenfilename()
    fail=open(failinimi,encoding="UTF-8")
    for rida in fail:
        vastuvoetud.append(int(rida))
    aasta=simpledialog.askinteger("Vastuvõtu aasta", "\tMis aasta vastuvõetuid soovid, vahemikus 2011-2019:\t")
    if aasta not in aastad:
        tekst=Label(aken,text="Antud aastal vastuvõetuid pole")
        tekst.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        tekst=Label(aken,text=f"{aasta} aastal vastuvõetuid: {vastuvoetud[aastad.index(aasta)]}")
        tekst.place(relx=0.5, rely=0.5, anchor=CENTER)
       
aken=Tk()
aken.title("Vastuvõetud")
aken.geometry("200x70")

nupp = Button(aken,text='Vali fail',width=7,command=failivalik)
nupp.place(relx=0.5, rely=0.5, anchor=CENTER)

aken.mainloop()    
fail.close()