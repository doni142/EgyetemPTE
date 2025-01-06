# első GUI tesztprogramom Nov. 15. Pécs
# PTE TTK,

import tkinter as tk

width = 700 # Az ablak méretei
height = 500

window = tk.Tk() # létrehozza az ablakot

screenHeight = window.winfo_screenwidth()
screenWidth = window.winfo_screenheight()

# Kiszámítja, hogy hol legyen az ablak, hol lesz a képernyő közepén
winX = (screenWidth / 2) - (width / 2)
winY = (screenHeight / 2) - (height / 2)

# Ez a fv beállítja az ablak részeit
window.geometry('%dx%d+%d+%d' % (width, height, winX, winY))

# Kiír
window.title("Első ablakos alkalmazás")
window.configure(bg='blue')

# Címke + szöveg
greeting = tk.Label(text="Első GUI-m")
greeting.pack()

# Gomb lenyomását kezelő fv
def handle_click(event):
    print("Az EXIT gombot lenyomták")
    exit(0)

def handle_click_multi(event):
    print("Az * gombot lenyomták")
    greeting.configure(text='*')
'''def handle_click_mod(event):
    print("Az / gombot lenyomták")'''

def handle_click_plus(event):
    print("Az + gombot lenyomták")
    greeting.configure(text='+')

'''def handle_click_minus(event):
    print("Az - gombot lenyomták")'''

def handle_click_egy(event):
    print("a 1 gombot lenyomták")
    greeting.configure(text=1)

def handle_click_ketto(event):
    print("a 2 gombot lenyomták")
    greeting.configure(text=2)

def handle_click_harom(event):
    print("a 3 gombot lenyomták")
    greeting.configure(text=3)

# Hozzá ad egy gombot
exitgomb = tk.Button(text="EXIT")
# Figyeli, hogy lenyomja a gombot
exitgomb.bind("<Button-1>", handle_click)
# Ez rakja ki a gombot
exitgomb.pack()
# Fő ciklus, hogy lefusson
exitgomb.place(x=400, y=400)

plusgomb = tk.Button(text="+")
plusgomb.bind("<Button-1>", handle_click_plus)
plusgomb.pack()
plusgomb.place(x=120, y=120)

szorzasgomb = tk.Button(text="*")
szorzasgomb.bind("<Button-1>", handle_click_multi)
szorzasgomb.pack()
szorzasgomb.place(x=40, y=40)

'''minusngomb = tk.Button(text="-")
minusngomb.bind("<Button-1>", handle_click_minus)
minusngomb.pack()'''

'''osztasgomb = tk.Button(text="/")
osztasgomb.bind("<Button-1>", handle_click_mod)
osztasgomb.pack()'''

'''szamok = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0",
]
for index in enumerate(szamok):
    sor = (index // 4) + 1
    oszlop = index % 4
    szamok = tk.Button(font=("Arial", 18),
        width=5,
        height=2, )'''

window.mainloop()