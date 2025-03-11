from main import *
from window2 import second_win
from window3 import third_win
from window4 import fourth_win
from window5 import fifth_win
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Головне вікно")
root.geometry("850x550")  # Розмір вікна

gif_path = "17xe.gif"
gif = Image.open(gif_path)

target_size = (850, 550)

frames = []
try:
    while True:
        frame = gif.copy().convert("RGBA").resize(target_size, Image.LANCZOS)  # Масштабування
        frames.append(ImageTk.PhotoImage(frame))
        gif.seek(len(frames))
except EOFError:
    pass

gif.close()

bg_label = Label(root)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def update_frame(index=0):
    frame = frames[index]
    bg_label.config(image=frame)
    root.after(100, update_frame, (index + 1) % len(frames))

update_frame()

def a_set():
    a_rand(input_a, min_u, max_u, root)
    u_gen(min_u, max_u)

def b_set():
    b_rand(input_b, min_u, max_u, root)
    u_gen(min_u, max_u)

def c_set():
    c_rand(input_c, min_u, max_u, root)
    u_gen(min_u, max_u)

def a_w():
    a_write(enter_a, root)

def b_w():
    b_write(enter_b, root)

def c_w():
    c_write(enter_c, root)

Button(root, bg="#4274ad", text="Вікно 2", font="Arial 12", command=second_win, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=250, y=35)
Button(root, bg="#4274ad", text="Вікно 3", font="Arial 12", command=third_win, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=400, y=35)
Button(root, bg="#4274ad", text="Вікно 4", font="Arial 12", command=fourth_win, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=550, y=35)
Button(root, bg="#4274ad", text="Вікно 5", font="Arial 12", command=fifth_win, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=700, y=35)

Label(root, text="Кулик Назар Ярославлвич", font="Arial 14", bg="#0e427d").place(x=5, y=5)
Label(root, text="Студент групи ІО-" + "43", font="Arial 14", bg="#0e427d").place(x=5, y=30)
Label(root, text="Номер у списку: " + "15", font="Arial 14", bg="#0e427d").place(x=5, y=55)
Label(root, text="Варіант: " + str((25 + 33 % 60) % 30 + 1), font="Arial 14", bg="#0e427d").place(x=5, y=80)

Label(root, bg="#0e427d", text="Потужність", font="Arial 14").place(x=40, y=110)
Label(root, bg="#0e427d", text="А:", font="Arial 12").place(x=25, y=145)
Label(root, bg="#0e427d", text="В:", font="Arial 12").place(x=25, y=175)
Label(root, bg="#0e427d", text="С:", font="Arial 12").place(x=25, y=205)
input_a = Entry(root, width=12, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
input_a.place(x=80, y=145)
input_b = Entry(root, width=12, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
input_b.place(x=80, y=175)
input_c = Entry(root, width=12, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
input_c.place(x=80, y=205)

Label(root, bg="#0e427d", text="Діапазон універсальної множини", font="Arial 14").place(x=395, y=110)
Label(root, bg="#0e427d", text="U:", font="Arial 12").place(x=390, y=145)
Label(root, bg="#0e427d", text="(", font="Arial 14").place(x=425, y=140)
Label(root, bg="#0e427d", text=";", font="Arial 14").place(x=515, y=140)
Label(root, bg="#0e427d", text=")", font="Arial 14").place(x=605, y=140)
min_u = Entry(root, width=7, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
min_u.place(x=440, y=145)
max_u = Entry(root, width=7, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
max_u.place(x=535, y=145)


Label(root, bg="#0e427d", text="Випадкова генерація", font="Arial 14").place(x=540, y=400)
Button(root, width=15, bg="#4274ad", text="Сформувати A", font="Arial 12", command=a_set, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=550, y=440)
Button(root, width=15, bg="#4274ad", text="Сформувати B", font="Arial 12", command=b_set, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=550, y=470)
Button(root, width=15, bg="#4274ad", text="Сформувати C", font="Arial 12", command=c_set, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=550, y=500)

Label(root, bg="#0e427d", text="Ручний ввід", font="Arial 14").place(x=40, y=400)
Label(root, bg="#0e427d", text="А:", font="Arial 12").place(x=25, y=440)
Label(root, bg="#0e427d", text="В:", font="Arial 12").place(x=25, y=470)
Label(root, bg="#0e427d", text="С:", font="Arial 12").place(x=25, y=500)
enter_a = Entry(root, width=25, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
enter_a.place(x=80, y=440)
enter_b = Entry(root, width=25, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
enter_b.place(x=80, y=470)
enter_c = Entry(root, width=25, font="Arial 12", bg="#4570a1", highlightbackground="#051221", highlightthickness=2, bd=0)
enter_c.place(x=80, y=500)

Button(root, width=17, bg="#4274ad", text="Підтвердити", font="Arial 12", command=a_w, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=340, y=440)
Button(root, width=17, bg="#4274ad", text="Підтвердити", font="Arial 12", command=b_w, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=340, y=470)
Button(root, width=17, bg="#4274ad", text="Підтвердити", font="Arial 12", command=c_w, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=340, y=500)

Label(root, bg="#0e427d", text="Множини", font="Arial 14").place(x=295+450, y=400)
Label(root, bg="#0e427d", text="A:", font="Arial 12").place(x=280+450, y=440)
Label(root, bg="#0e427d", text="B:", font="Arial 12").place(x=280+450, y=470)
Label(root, bg="#0e427d", text="C:", font="Arial 12").place(x=280+450, y=500)
root.mainloop()
