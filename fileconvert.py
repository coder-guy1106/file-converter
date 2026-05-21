from tkinter import filedialog as fd
from PIL import Image,ImageTk
import tkinter as tk
root = tk.Tk()

root.title("file converter")







def select_file():
    filetypes = (
        ('image files', '*.png *.jpg *.jpeg *.webp *.bmp *.tif *.tiff *.ico *.icns *.ppm *.pgm *.pbm *.tga *.eps'),
        ('All files', '*.*')
    )
    
    f = fd.askopenfilename(filetypes=filetypes)
    print("\n------------------------------------\n")

    im= Image.open(f)
    im_label = ImageTk.PhotoImage(im)
    lab = tk.Label(root, image=im_label)
    lab.pack(side="left",expand=True)
    root.mainloop()



button1 = tk.Button(
    root,
    text='Open a File',
    command=select_file,
    bg="azure4"   
)
button1.pack(side="top",fill="x",expand=True)
supported=['png','jpg','jpeg','webp','bmp','tif','tiff','ico','icns','ppm','pgm','pbm','tga','eps']

list = tk.Listbox(root)
for i in range(1,15):
    list.insert(i,supported[i-1])

list.pack(side="right")


root.geometry("+"+str(860)+"+"+str(390))
root.geometry("300x200")
root.mainloop()