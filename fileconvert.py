from tkinter import filedialog as fd
from PIL import Image,ImageTk
import tkinter as tk
root = tk.Tk()
root.title("file converter")
#lab = tk.Label(root)
#lab.pack(fill='both',padx=10,pady=10)
supported=['png','jpg','jpeg','webp','bmp','tif','tiff','ico','icns','ppm','pgm','pbm','tga','eps']

def select_file():
    filetypes = (
        ('image files', '*.png *.jpg *.jpeg *.webp *.bmp *.tif *.tiff *.ico *.icns *.ppm *.pgm *.pbm *.tga *.eps'),
        ('All files', '*.*')
    )
    
    f = fd.askopenfilename(filetypes=filetypes)
    print("\n------------------------------------\n")

    im= Image.open(f)
    w=300
    im.thumbnail((w,w))
    im_label = ImageTk.PhotoImage(im)
    lab = tk.Label(root, image=im_label)
    lab.pack(fill='both',padx=10,pady=10)
    root.mainloop()



button1 = tk.Button(
    root,
    text='Open a File',
    command=select_file,
    bg="azure4"
    height=1
    font=("arial",25,"bold")
)

button1.pack(side="top",fill="x")


# RIGHT UI
right_ui = tk.Frame(root)
right_ui.pack(side="right")

filetype = tk.Label(text="No file selected")
filetype.pack(side="top")


list = tk.Listbox(root)
for i in range(1,15):
    list.insert(i,supported[i-1])
list.pack(side="right")







root.geometry("+"+str(860)+"+"+str(390))
root.geometry("400x350")
root.mainloop()