from main import *
from tkinter import *
from PIL import Image, ImageTk


def fourth_win():
    root3 = Toplevel()
    root3.title("Вікно 4")
    root3.geometry("500x280")

    gif_path = "17xe.gif"
    gif = Image.open(gif_path)

    target_size = (500, 280)

    frames = []
    try:
        while True:
            frame = gif.copy().convert("RGBA").resize(target_size, Image.LANCZOS)  # Масштабування
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass

    gif.close()

    bg_label = Label(root3)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_frame(index=0):
        frame = frames[index]
        bg_label.config(image=frame)
        root3.after(100, update_frame, (index + 1) % len(frames))

    update_frame()

    def z_calulation():
        result = z_my_calc(a, b, u)
        Label(root3, bg="#0e427d", text=str(result), font="Arial 12").place(x=70, y=95)
        Label(root3, bg="#0e427d", text=str(result), font="Arial 12").place(x=70, y=180)

    def save_result_z():
        result = z_my_calc(a, b, u)
        save_res = open("Z.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root3, bg="#0e427d", text="X:", font="Arial 12").place(x=10, y=20)
    Label(root3, bg="#0e427d", text=str(u-b), font="Arial 12").place(x=70, y=20)
    Label(root3, bg="#0e427d", text="Y:", font="Arial 12").place(x=10, y=45)
    Label(root3, bg="#0e427d", text=str(u-a), font="Arial 12").place(x=70, y=45)
    Label(root3, bg="#0e427d", text="X \ Y:", font="Arial 12").place(x=10, y=95)
    Label(root3, bg="#0e427d", text="Z = ", font="Arial 12").place(x=30, y=180)

    Button(root3, bg="#4274ad", width=20, text="Обчислити", font="Arial 12", command=z_calulation, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=130)
    Button(root3, bg="#4274ad", width=28, text="Зберегти результат у файл Z.txt", font="Arial 12", command=save_result_z, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=210)
