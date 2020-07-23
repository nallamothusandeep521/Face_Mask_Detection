import tkinter
from detect_mask_video import *
win = tkinter.Tk()

Btn = tkinter.Button(text = "Hi",Onclick = detect_and_predict_mask)
Btn.pack()

win.mainloop()
