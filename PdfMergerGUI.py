import tkinter as tk
from tkinter import filedialog, Text
import os
import os, PyPDF2
from os import chdir

root=tk.Tk()
root.title("PDF Merger")
#root.iconbitmap("seagull.ico"))
root.resizable(0, 0)




def addDir():
    Dirname=filedialog.askdirectory()
    print(Dirname)
    os.chdir(Dirname)
    

def runMerge():
    #Get all the PDF filenames
    pdf2merge = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf2merge.append(filename)
    
    pdfWriter = PyPDF2.PdfFileWriter()
    
    #loop through all PDFs
    for filename in pdf2merge:
    #rb for read binary
        pdfFileObj = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
    #save PDF to file, wb for write binary
    userfilename=str(entry1.get())
    pdfOutput = open(userfilename+'.pdf', 'wb')
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()
    popupmsg("Done")
    
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(anchor= "center", fill="x", pady=10)
    B1 = tk.Button(popup, text="Close", command = popup.destroy)
    B1.pack()
    popup.mainloop()



canvas=tk.Canvas(root, height=300, width=400, bg="#263D42")
entry1 = tk.Entry (root) 

label1 =tk.Label(root,text="Name of the merged file:", bg="white")
label2 =tk.Label(root,text="1.Select the directory where the pdf files are.", bg="white")
label3 =tk.Label(root,text="2.Type a name for the merged pdf.", bg="white")
label4 =tk.Label(root,text="3.Hit Run.", bg="white")

canvas.create_window(175,150,window=label2)
canvas.create_window(150,180,window=label3)
canvas.create_window(85,210,window=label4)


canvas.create_window(125,90,window=label1)
canvas.create_window(275,90, window=entry1)

canvas.pack()

openFile=tk.Button(root,text ="Select Directory", padx=10,pady=5,fg="white",bg="#263D42",command=addDir)
openFile.pack()

runFile=tk.Button(root,text = "Run",padx=15,pady=5,fg="white",bg="#263D42",command=runMerge )
runFile.pack()
root.mainloop()


#geektechstuff code combine with tkinter code






