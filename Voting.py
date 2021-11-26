from tkinter import *
from PIL import Image, ImageTk
root = Tk()
image = Image.open(r"D:\vote.jpg")
photo = ImageTk.PhotoImage(image)
root.title("Voting Eligibility")
root.geometry("500x300")

def voting():
    Age = int(t4.get()) - int(t3.get())
    deta_value.set(Age)

    if Age >= 18:
        m.set(f"{name.get()} you are eligible to Vote")
        message.set("Thank You!")
        Label(root, textvariable=m, fg="green").grid(row=12, column=4)
        Label(root, textvariable=message, fg="blue",font=("Arial", 25)).grid(row=15, column=4)
    else:
        m.set(f"Sorry! {name.get()} you are not eligible")
        message.set("Thank You!")
        Label(root, textvariable=m, fg="red").grid(row=12, column=4)
        Label(root, textvariable=message, fg="blue",font=("Arial", 25)).grid(row=15, column=4)

det1 = Label(root, text="Name")
det2 = Label(root, text="Gender")
det3 = Label(root, text="Year Of Birth")
det4 = Label(root, text="Current Year")
det5 = Label(root, text="Age")
img=Label(root,image=photo)
deta_value = StringVar()
name = StringVar()
m = StringVar()
message = StringVar()
res = Entry(root, text="", textvariable=deta_value)

t1 = Entry(root, text="", textvariable=name)
t2 = Entry(root)
t3 = Entry(root)
t4 = Entry(root)
t5 = Text(root,height=1.5,width=30)

b1 = Button(root, text="Check Eligibility", bg="grey", command=voting)
b2 = Button(root, text="Exit",bg="grey", command=root.destroy)

det1.grid(row=0, column=0)
det2.grid(row=1, column=0)
det3.grid(row=2, column=0)
det4.grid(row=3, column=0)
det5.grid(row=6, column=4)

t1.grid(row=0, column=1)
t2.grid(row=1, column=1)
t3.grid(row=2, column=1)
t4.grid(row=3, column=1)
t5.grid(row=12, column=4)
res.grid(row=8, column=4)
b1.grid(row=9, column=4)
b2.grid(row=14, column=4)
img.place(x=6, y=120)

root.mainloop()