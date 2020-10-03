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

    name = name_entry.get("1.0", "end-1c")
    text = text_entry.get("1.0", "end-1c")

    send_req(text, name)


name_var = tk.StringVar()
text_var = tk.StringVar()
image = tk.PhotoImage(file="discordlogo.png")
image = image.subsample(6, 6)
canvas.create_image(550, 50, image=image)

name_label = tk.Label(root,
                      text='Username',
                      font=('calibre', 15, 'bold'),
                      bg="#0f3057",
                      fg="#fff"
                      )


name_entry = tk.Text(root,
                     height=2,
                     width=23,
                     font=('calibre', 13, 'normal'))

text_label = tk.Label(root,
                      text='Text',
                      font=('calibre', 15, 'bold'),
                      bg="#0f3057",
                      fg="#fff"
                      )

text_entry = tk.Text(root,
                     height=5,
                     width=25,
                     font=('calibre', 15, 'normal'))

sub_btn = tk.Button(root,
                    text='Submit',
                    command=submit,
                    bg="#9ab3f5",
                    width=15,
                    fg="#fff"
                    )

name_label.place(x=50, y=135)
name_entry.place(x=215, y=130)
text_label.place(x=50, y=250)
text_entry.place(x=215, y=220)
sub_btn.place(x=260, y=340)
root.mainloop()
