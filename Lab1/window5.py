from main import *
from tkinter import *
from PIL import Image, ImageTk

def fifth_win():
    root4 = Toplevel()
    root4.title("Вікно 5")
    root4.geometry("620x220")

    gif_path = "17xe.gif"
    gif = Image.open(gif_path)

    target_size = (620, 220)

    frames = []
    try:
        while True:
            frame = gif.copy().convert("RGBA").resize(target_size, Image.LANCZOS)  # Масштабування
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass

    gif.close()

    bg_label = Label(root4)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_frame(index=0):
        frame = frames[index]
        bg_label.config(image=frame)
        root4.after(100, update_frame, (index + 1) % len(frames))

    update_frame()

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
            Label(root4, bg="#0e427d", text="D = D (спрощене)", font="Arial 12").place(x=10, y=110)
        else:
            Label(root4, bg="#0e427d", text="D ≠ D (спрощене)", font="Arial 12").place(x=10, y=110)

    def compare_z():
        if z == z_python:
            Label(root4, bg="#0e427d", text="Z = Z (функціями)", font="Arial 12").place(x=430, y=110)
        else:
            Label(root4, bg="#0e427d", text="Z ≠ Z (функціями)", font="Arial 12").place(x=430, y=110)

    Label(root4, bg="#0e427d", text="D:", font="Arial 12").place(x=10, y=20)
    Label(root4, bg="#0e427d", text=str(d), font="Arial 12").place(x=160, y=20)
    Label(root4, bg="#0e427d", text="D (спрощене):", font="Arial 12").place(x=10, y=50)
    Label(root4, bg="#0e427d", text=str(d_simple), font="Arial 12").place(x=160, y=50)

    Label(root4, bg="#0e427d", text="Z:", font="Arial 12").place(x=330, y=20)
    Label(root4, bg="#0e427d", text=str(z), font="Arial 12").place(x=500, y=20)
    Label(root4, bg="#0e427d", text="Z (вбуд. функціями):", font="Arial 12").place(x=330, y=50)
    Label(root4, bg="#0e427d", text=str(z_python), font="Arial 12").place(x=500, y=50)

    Button(root4, bg="#4274ad", width=12, text="Порівняння D", font="Arial 12", command=compare_d, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=10, y=150)
    Button(root4, bg="#4274ad", width=12, text="Порівняння Z", font="Arial 12", command=compare_z, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=430, y=150)

    res_d.close()
    res_d_simple.close()
    res_z.close()
