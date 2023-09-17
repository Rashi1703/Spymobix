from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

my_wind=Tk()
my_wind.title("Phone number Tracker")
my_wind.geometry("{0}x{1}+0+0".format(my_wind.winfo_screenwidth(),my_wind.winfo_screenheight()))
my_wind.overrideredirect(True)
    
my_wind.configure(bg="#FFDDD6")
same=True
n=1.75
# Adding a background image
background_image =Image.open("phn.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(my_wind)
Canvas1.create_image(750,340,image = img)      
Canvas1.config(bg="#FFDDD6",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.grid()

label_1=Label(my_wind,text="Get Info Of Your Phone Number",bg="Black",fg="white",font="Arial 37 bold italic ",bd=10,relief="sunken",padx=3,pady=3)
label_1.place(relx=0.3,rely=0.07,relwidth=0.6,relheight=0.11)

def Exit():
    Exit=messagebox.askyesno("Phone Number Tracker","Confirm if you want to exit")
    if Exit > 0:
        my_wind.destroy()

def get():
    global number
    region.delete(0,END)
    service.delete(0,END)
    Country.delete(0,END)
    num=number.get("1.0",END)
    mobileNo=phonenumbers.parse(num)
    region.insert(END,timezone.time_zones_for_number(mobileNo))
    service.insert(END," "+carrier.name_for_number(mobileNo,"en"))
    Country.insert(END," "+geocoder.description_for_number(mobileNo,"en"))

def refresh():
    number.delete(1.0,END)
    region.delete(0,END)
    service.delete(0,END)
    Country.delete(0,END)
    
label_num=Label(my_wind,text="Enter Your Phone Number :",bg="#DEDEDE",fg="black",font="Arial 22 bold italic ",bd=5,relief="sunken",padx=3,pady=3)
label_num.place(relx=0.32,rely=0.26,relwidth=0.3,relheight=0.05)
number= Text(bg="#DEDEDE",fg="black",font="Arial 22 bold italic",bd=5,relief="sunken")
number.place(relx=0.69,rely=0.26, relwidth=0.2, relheight=0.05)

button_get_info=Button(my_wind,text="GET INFO",bg="Black",fg="white",font="Arial 20 bold ",bd=10,relief="raised",padx=2,pady=2,command=get)
button_get_info.place(relx=0.6,rely=0.34, relwidth=0.1, relheight=0.08)

label_region=Label(my_wind,text="Phone No. Belongs To Region :",bg="#DEDEDE",fg="black",font="Arial 20 bold italic ",bd=5,relief="sunken",padx=3,pady=3)
label_region.place(relx=0.32,rely=0.46,relwidth=0.3,relheight=0.05)
region= Entry(bg="#DEDEDE",fg="black",font="Arial 20 bold italic",bd=5,relief="sunken")
region.place(relx=0.69,rely=0.46, relwidth=0.2, relheight=0.05)

label_service=Label(my_wind,text="Service Provider Of Phone No. :",bg="#DEDEDE",fg="black",font="Arial 20 bold italic ",bd=5,relief="sunken",padx=3,pady=3)
label_service.place(relx=0.32,rely=0.56,relwidth=0.3,relheight=0.05)
service= Entry(bg="#DEDEDE",fg="black",font="Arial 20 bold italic",bd=5,relief="sunken")
service.place(relx=0.69,rely=0.56, relwidth=0.2, relheight=0.05)

label_Country=Label(my_wind,text="Phone No. Belongs To Country :",bg="#DEDEDE",fg="black",font="Arial 20 bold italic ",bd=5,relief="sunken",padx=3,pady=3)
label_Country.place(relx=0.32,rely=0.66,relwidth=0.3,relheight=0.05)
Country= Entry(bg="#DEDEDE",fg="black",font="Arial 20 bold italic",bd=5,relief="sunken")
Country.place(relx=0.69,rely=0.66, relwidth=0.2, relheight=0.05)

button_refresh=Button(my_wind,text="REFRESH",bg="Black",fg="white",font="Arial 20 bold ",bd=10,relief="raised",padx=3,pady=3,command=refresh)
button_refresh.place(relx=0.6,rely=0.77, relwidth=0.1, relheight=0.08)

button_refresh=Button(my_wind,text="EXIT",bg="Black",fg="white",font="Arial 20 bold ",bd=10,relief="raised",padx=3,pady=3,command=Exit)
button_refresh.place(relx=0.6,rely=0.87, relwidth=0.1, relheight=0.08)
my_wind.mainloop()
