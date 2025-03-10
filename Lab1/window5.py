from main import *
from tkinter import *


def fifth_win():
    root4 = Toplevel()
    root4.title("Вікно 5")
    root4.configure(bg="#98E5FE")
    root4.geometry("920x220")

    res_d = open("D.txt", "r")
    d = res_d.readlines()[0]
    res_d_simple = open("D_simple.txt", "r")
    d_simple = res_d_simple.readlines()[0]

    res_z = open("Z.txt", "r")
    z = res_z.readlines()[0]
    result_z = z_calc(a, b, u)
    z_python = str(result_z)

    def compare_d():
        if d == d_simple:
            Label(root4, bg="#98E5FE", text="D = D (спрощене)", font="Arial 12").place(x=10, y=110)
        else:
            Label(root4, bg="#98E5FE", text="D ≠ D (спрощене)", font="Arial 12").place(x=10, y=110)

    def compare_z():
        if z == z_python:
            Label(root4, bg="#98E5FE", text="Z = Z (функціями)", font="Arial 12").place(x=430, y=110)
        else:
            Label(root4, bg="#98E5FE", text="Z ≠ Z (функціями)", font="Arial 12").place(x=430, y=110)

    Label(root4, bg="#98E5FE", text="D:", font="Arial 12").place(x=10, y=20)
    Label(root4, bg="#98E5FE", text=str(d), font="Arial 12").place(x=160, y=20)
    Label(root4, bg="#98E5FE", text="D (спрощене):", font="Arial 12").place(x=10, y=50)
    Label(root4, bg="#98E5FE", text=str(d_simple), font="Arial 12").place(x=160, y=50)

    Label(root4, bg="#98E5FE", text="Z:", font="Arial 12").place(x=430, y=20)
    Label(root4, bg="#98E5FE", text=str(z), font="Arial 12").place(x=600, y=20)
    Label(root4, bg="#98E5FE", text="Z (вбуд. функціями):", font="Arial 12").place(x=430, y=50)
    Label(root4, bg="#98E5FE", text=str(z_python), font="Arial 12").place(x=600, y=50)

    Button(root4, bg="#FFFFFF", width=12, text="Порівняння D", font="Arial 12", command=compare_d).place(x=10, y=150)
    Button(root4, bg="#FFFFFF", width=12, text="Порівняння Z", font="Arial 12", command=compare_z).place(x=430, y=150)

    res_d.close()
    res_d_simple.close()
    res_z.close()
