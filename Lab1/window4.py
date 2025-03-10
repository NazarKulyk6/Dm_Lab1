from main import *
from tkinter import *


def fourth_win():
    root3 = Toplevel()
    root3.title("Вікно 4")
    root3.configure(bg="#98E5FE")
    root3.geometry("500x280")

    def z_calulation():
        result = z_my_calc(a, b, u)
        Label(root3, bg="#98E5FE", text=str(result), font="Arial 12").place(x=70, y=95)
        Label(root3, bg="#98E5FE", text=str(result), font="Arial 12").place(x=70, y=180)

    def save_result_z():
        result = z_my_calc(a, b, u)
        save_res = open("Z.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root3, bg="#98E5FE", text="X:", font="Arial 12").place(x=10, y=20)
    Label(root3, bg="#98E5FE", text=str(u-b), font="Arial 12").place(x=70, y=20)
    Label(root3, bg="#98E5FE", text="Y:", font="Arial 12").place(x=10, y=45)
    Label(root3, bg="#98E5FE", text=str(u-a), font="Arial 12").place(x=70, y=45)
    Label(root3, bg="#98E5FE", text="X \ Y:", font="Arial 12").place(x=10, y=95)
    Label(root3, bg="#98E5FE", text="Z = ", font="Arial 12").place(x=30, y=180)

    Button(root3, bg="#FFFFFF", width=20, text="Обчислити", font="Arial 12", command=z_calulation).place(x=30, y=130)
    Button(root3, bg="#FFFFFF", width=28, text="Зберегти результат у файл Z.txt", font="Arial 12", command=save_result_z).place(x=30, y=210)
