from tkinter.font import BOLD
from pytube import YouTube
from tkinter import *
from customtkinter import *
from tkinter import messagebox
import webbrowser


### TKINTER SECTION // UI SECTION
root=CTk()
root.geometry("700x450")
root.configure(background="#000000")
root.title("YtDon - @imranpgda")
root.resizable(False,False)

##FUNCTIONS HERE

def submit_btn():
    global roottube
    roottube=YouTube(entLink.get())
    linkLoad.set(roottube.title)

def temp_text(e):
   topen.delete(0,"end")
 
def connect():
    url="https://github.com/imranpgda"
    new=1
    webbrowser.open(url,new=new)
    print("<> THANK YOU FOR CONNECTING BUDDDY <>")

def qual_select():
    vids=roottube.streams.filter(progressive=True)
    setvids=list(enumerate(vids))
    choice=rvar.get()
    messagebox.showinfo(title="YtDon--Heyy User!",message="Fetching Data > Kindly Wait")
    vids[choice].download()
   
    messagebox.showinfo(title="YtDon--Heyy User!",message="Download Completed\nFile Will Be In Same Folder Of Program\n\nConnect With Me On Github >> https://github.com/imranpgda")
    
### Program By _ @imranpgda :
# if notice any bug or error -- plz Report me
# don't forget to Follow me on Github - 
# https://github.com/imranpgda


#variables HERE
entLink=StringVar()
linkLoad=StringVar()
optlink=StringVar()
rvar=IntVar()

#design and Display
toplb=CTkLabel(root,text="YtDon - @imranpgda",corner_radius=10,fg_color="#f5b301",text_color="#000000",font=("Corbyn Serif Medium",15)).pack(ipadx=10,ipady=10,padx=10,pady=10)
topen=CTkEntry(root,width=450,textvariable=entLink,corner_radius=15,border_width=1)
topen.insert(0,"Paste Link Here...")
topen.bind("<FocusIn>", temp_text)
topen.pack(ipadx=10,ipady=5,padx=10,pady=5)

topbtn = CTkButton(root,width=80,height=25,fg_color="#000000",hover_color="#f5b301",border_width=1,corner_radius=10,text="Submit",command=submit_btn).pack(anchor="center",pady=10)


### AFTER LINK PASTE HERE
lowlb=CTkLabel(root,textvariable=linkLoad,corner_radius=10,fg_color="transparent",text_color="#f5b301",font=("exo",13,BOLD)).pack(ipadx=5,ipady=5,padx=10,pady=20)


# RADIOBUTTON

rd1=CTkRadioButton(root,text="144p ",font=("nexa",12),radiobutton_width=35,radiobutton_height=15,border_width_checked=4,border_color="#f5b301",fg_color="#f5b301",hover_color="#000000",border_width_unchecked=2,variable=rvar,value=0).pack(padx=15,anchor="center")
rd2=CTkRadioButton(root,text="360p ",font=("nexa",12),radiobutton_width=35,radiobutton_height=15,border_width_checked=4,border_color="#f5b301",fg_color="#f5b301",hover_color="#000000",border_width_unchecked=2,variable=rvar,value=1).pack(anchor="center")
rd3=CTkRadioButton(root,text="720p ",font=("nexa",12),radiobutton_width=35,radiobutton_height=15,border_width_checked=4,border_color="#f5b301",fg_color="#f5b301",hover_color="#000000",border_width_unchecked=2,variable=rvar,value=2).pack(anchor="center")
rd4=CTkRadioButton(root,text="1080p ",font=("nexa",12),radiobutton_width=35,radiobutton_height=15,border_width_checked=4,border_color="#f5b301",fg_color="#f5b301",hover_color="#000000",border_width_unchecked=2,variable=rvar,value=3).pack(anchor="center")
#lower_submit btn
regbtn=CTkButton(root,width=80,height=25,fg_color="#000000",hover_color="#f5b301",border_width=1,corner_radius=10,text="Submit",command=qual_select).pack(anchor="center",pady=15)

#DEvConnect_btn
contbtn=CTkButton(root,text="Developer",font=("recoleta",15),text_color="#000000",fg_color="#f5b301",corner_radius=5,hover_color="#3B3F46",command=connect).pack(anchor="center",pady=15)


root.mainloop()