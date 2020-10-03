import tkinter as tk
from annoucements import send_req

root = tk.Tk()
root.configure(bg='gray')
root.title("Discord Bot")
frame = tk.Frame(root)
frame.pack()
canvas = tk.Canvas(frame, bg="#0f3057", width=600, height=400)
canvas.pack()
root.resizable(width=False, height=False)


def submit():

    name = name_var.get()
    text = text_var.get()

    send_req(text, name)
    name_var.set("")
    text_var.set("")


name_var = tk.StringVar()
text_var = tk.StringVar()
image = tk.PhotoImage(file="discordlogo.png")
image = image.subsample(6, 6)
canvas.create_image(550, 50, image=image)

name_label = tk.Label(root,
                      text='Username',
                      font=('calibre', 11, 'bold'),
                      bg="#0f3057")


name_entry = tk.Entry(root,
                      textvariable=name_var,
                      font=('calibre', 10, 'normal'))

text_label = tk.Label(root,
                      text='Text',
                      font=('calibre', 11, 'bold'),
                      bg="#0f3057")

text_entry = tk.Entry(root,
                      textvariable=text_var,
                      font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root,
                    text='Submit',
                    command=submit,
                    bg="#9ab3f5")

name_label.place(x=250, y=110)
name_entry.place(x=215, y=130)
text_label.place(x=265, y=200)
text_entry.place(x=215, y=220)
sub_btn.place(x=260, y=250)
root.mainloop()
