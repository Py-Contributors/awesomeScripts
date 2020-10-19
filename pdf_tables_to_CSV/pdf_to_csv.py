import tabula as tb
import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename as open_as
from PIL import ImageTk, Image

def msg_from_author():
	msg='''
\tConvert Your Pdf tables into csv format easily
\tJust Search/Browse the file and hit the convert button

\tTHANK YOU FOR USING
\tSufiyan Ansari
	'''
	print(msg)

def search_file():
	filepath = open_as(filetypes=[("Pdf Files", "*.pdf")])
	if not filepath:
		return
	csv_name = filepath[:-4]+'_csv.csv'
	lbl_file = tk.Label(save_frame,text = 'Added File : ' + filepath.split('/')[-1],bg='#dc3545')
	lbl_file.grid(row=0,column=0,pady=10)
	btn_save = tk.Button(save_frame, text='Save as csv', command=lambda:save_file(filepath,csv_name))
	btn_save.grid(row=0,column=1)
	save_frame.grid(row=4,column=0)

def search_file_online():
	link = txt_search.get()
	lbl_file = tk.Label(save_frame,text = 'Download will take time')
	lbl_file.grid(row=0,column=0)
	path = '/csv/download.csv'
	btn_save = tk.Button(save_frame, text='Save as csv to your /csv folder', command=lambda:save_file(filepath,path))
	btn_save.grid(row=0,column=1)
	save_frame.grid(row=4,column=0)

def save_file(filepath,csv_name):
	tb.convert_into(filepath, csv_name, output_format="csv", pages='all')
	lbl_csv_file = tk.Label(window,text = 'File Converted Successfully.\n Saved at :' + csv_name,bg='#dc3554')
	lbl_csv_file.grid(row=5,column=0,pady=5)

msg_from_author()
window = tk.Tk()
window['bg'] = '#dc3545'
window.columnconfigure(0,weight=1,minsize=600)
window.title('PDF TO CSV CONVERTER')
#window.geometry("685x600")


search_frame = tk.Frame(window)
browse_frame = tk.Frame(window)
save_frame = tk.Frame(window)
photo_frame = tk.Frame(window)

main_font = font.Font(size=40)
lbl_main = tk.Label(window, text='PDF TO CSV CONVERTER', bg='#333', fg='#f1f1f1',font=main_font)
lbl_main.grid(row=0,column=0,sticky='we',pady=20)

lbl_browse = tk.Label(browse_frame, text='Browse Your PDF File')
lbl_browse.grid(row=0, column=0, sticky='we')
browse_frame['borderwidth'] = 2
browse_frame['relief'] = 'sunken'
btn_browse = tk.Button(browse_frame, text='Browse Local', command=search_file)
btn_browse.grid(row=0, column=1, sticky='we')

txt_search = tk.Entry(search_frame)
txt_search.insert(0,'Enter Your Link To Pdf Here')
txt_search.grid(row=0, column=0, sticky='we')
search_frame['borderwidth'] = 2
search_frame['relief'] = 'sunken'
btn_search = tk.Button(search_frame, text='Convert From Online', command=search_file_online)
btn_search.grid(row=0, column=1, sticky='we')

browse_frame.grid(row=1,column=0,pady=5)

lbl_or = tk.Label(window,text='OR',bg='#dc3545')
lbl_or.grid(row=2,column=0)

search_frame.grid(row=3,column=0)

img = ImageTk.PhotoImage(Image.open("images/bar.png"))
panel = tk.Label(photo_frame,image = img,bg="#dc3545")
panel.grid(row=0,column=0,padx=0)
photo_frame.grid(row=9,column=0)
window.mainloop()