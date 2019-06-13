#This code is messy, i couldn't find the time to make it cleaner.
#Proceed at your own risk
#----------------------------------------------

import tkinter
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import showerror, showinfo
import os
import nltk
import numpy as np
from nltk.util import ngrams
import time


#MAIN ----------------------------------------------
if __name__ == '__main__':

 root = tkinter.Tk()
 
 #GLOBAL VAR --------------------------------------------------------------------------------------------
 Dist_Path =tkinter.StringVar() 
 kgram = tkinter.StringVar()
 MatType = tkinter.StringVar()
 File_Path = tkinter.StringVar()
 MatFinal = None
 NbMotifs = 0                     
 Nb_Seq = 0          
 File_Desc = ""
 File_Size = ""
 sel_File_Nme = ""
 Dist_Path.set("")
 MatType.set("Boolean")
 kgram.set("3")
 Error_X = 0
 
 def Invalid_Struct () :
  global sel_File_Nme
  showerror("Bad File","invalid file structure !\nMake sure your file contains a description in it's first few rows")
  progressBar['value'] = 0
  progressBar.grid_forget()	
  File_Path.set("")
  sel_File_Nme = ""
  aboutLbl.configure(text = "Follow the steps and hit RUN")
  inFileTxt.configure(state = NORMAL )
  inFileTxt.delete(0,END)
  inFileTxt.configure(state = 'readonly' )
  runBtn.config(state=DISABLED)
  Matinit ()
  Error_X = 0
  
 def Matinit () :
  global Error_X
  global MatFinal
  global NbMotifs
  global Nb_Seq
  global sel_File_Nme
  MatFinal = None
  NbMotifs = 0                  
  Nb_Seq = 0 
  Error_X = 0
  exFileBtn.config(state=DISABLED)
  if not sel_File_Nme =="" :
   runBtn.config(state=NORMAL)
  
  
  
 def Concatenate_list_data(list):
     result= ''
     for element in list:
         result += str(element)
     return result
 
 def Distinct(seq, idfun=None): 
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

	
	
 def Sel_Mtype():

   print("You selected the option " + MatType.get())
   Matinit()
   
 def Sel_Kgrm():
   print("You chose: " + str(kgram.get())) 
   Matinit()

   
   
 def OpenSeqFile():
    global sel_File_Nme
    global File_Size
    try :
     local_pth_var = askopenfilename(filetypes =(("Text File", "*.txt"),("ALL Files","*.*")), title = "Choose a file.")
    except IOError as io :
     showerror("ERROR",io)
    if not local_pth_var == "" and os.path.basename(local_pth_var)[-4:] ==".txt":
     File_Path.set(local_pth_var)
     print (File_Path.get())
     sel_File_Nme = os.path.basename(File_Path.get())
     Matinit()
     aboutLbl.configure(text = "Follow the steps and hit RUN")
     inFileTxt.configure(state = NORMAL )
     inFileTxt.delete(0,END)
     inFileTxt.insert(0,sel_File_Nme)
     inFileTxt.configure(state='readonly')
     ln = os.stat(File_Path.get())
     if ln.st_size < 1024:
      File_Size = str(int(ln.st_size)) + " octets"
     else :
      File_Size = str(int(round(ln.st_size/1024))) + "Ko" 
    elif not os.path.basename(local_pth_var) == "" :
     showerror("Bad file type","Please select a supported file type")
    else : 
     print("notihng selected")
 
 def OpenDistFolder():
    local_dist_var = askdirectory()
    if not local_dist_var == "" :
     Dist_Path.set(local_dist_var)
     file_name = os.path.abspath(Dist_Path.get())
     outFileTxt.configure(state = NORMAL )
     outFileTxt.delete(0,END)
     outFileTxt.insert(0,file_name)
     outFileTxt.configure(state='readonly')
     exFileBtn.config(state=NORMAL)
     try:
       print ("file selected :", Dist_Path.get())
     except:                     
       showerror("Open Source File", "Failed to open file\n'%s'" % file_name)
    else : 
     print ("nothing selected")
    return 


	
 def OccMat(List1):
    global NbMotifs
    global Nb_Seq
    global Error_X
    global MatFinal
    with open(File_Path.get(), 'r') as corpus2:
     try :      
       lindex = 1
       k=0
       nbclasse = int(corpus2.readline())
       clss = - nbclasse
       for line in corpus2:
        Seq_i = line.rstrip("\n")
        if len(Seq_i) > 3 :                   #IGNORE if the line contains less than 3 char = it's not a valid seq        
         while k < NbMotifs :
          oc= Seq_i.count(List1[k])
          MatFinal[lindex][k] = str(oc)
          k = k + 1
         MatFinal[lindex][-1] = ('C%(number)s' %{"number": clss})
         lindex = lindex + 1
         k = 0
         progressBar['value'] += (75/Nb_Seq)
         progressBar.update()
        else :
         clss = clss +1
     except :
       Error_X = 1
	   
 def BoolMat(List1):
    global NbMotifs
    global Nb_Seq
    global Error_X
    global MatFinal
    with open(File_Path.get(), 'r') as corpus2:
      try :
        lindex = 1
        k=0
        nbclasse = corpus2.readline()
        clss = (int(nbclasse) * -1 )
        for line in corpus2:
         Seq_i = line.rstrip("\n")
         if len(Seq_i) > 3 :                   #IGNORE if the line contains less than 3 char = it's not a valid seq
          while k < NbMotifs :
            if List1[k] in Seq_i :
             MatFinal[lindex][k] = '1'
            else : 
             MatFinal[lindex][k] = '0'
            k = k + 1
          MatFinal[lindex][-1] = ('C%(number)s' %{"number": clss})
          lindex = lindex + 1
          k = 0
          progressBar['value'] += (75/Nb_Seq)
          progressBar.update()
         else :
          clss = clss +1
      except : 
        Error_X = 1
 
 def FreqMat(List1): 
    global NbMotifs
    global Nb_Seq
    global Error_X
    global MatFinal
    with open(File_Path.get(), 'r') as corpus2:
     try :
       lindex = 1
       k=0
       nbclasse = corpus2.readline()
       clss = (int(nbclasse) * -1 )
       for line in corpus2:
        Seq_i = line.rstrip("\n")
        if len(Seq_i) > 3 :                   #IGNORE if the line contains less than 3 char = it's not a valid seq
         nmotif = len(Seq_i)-int(kgram.get())+1
         while k < NbMotifs :
          oc= Seq_i.count(List1[k])
          MatFinal[lindex][k] = str(float("{:.4f}".format(oc/nmotif))).replace('.',',')
          k = k + 1
         MatFinal[lindex][-1] = ('C%(number)s' %{"number": clss})
         lindex = lindex + 1
         k = 0
         progressBar['value'] += (75/Nb_Seq)
         progressBar.update()
        else :
         clss = clss +1
     except : 
       Error_X = 1 
		 		 
 def TfIdfMat(List1):
    global NbMotifs
    global Nb_Seq
    global Error_X
    global MatFinal
    countm = np.zeros(NbMotifs)
    with open(File_Path.get(), 'r') as corpus2:
     try :
       lindex = 1
       k=0
       nbclasse = corpus2.readline()
       clss = (int(nbclasse) * -1 )
       for line in corpus2:
        Seq_i = line.rstrip("\n")
        if len(Seq_i) > 3 :                   #IGNORE if the line contains less than 3 char = it's not a valid seq
         nmotif = len(Seq_i)-int(kgram.get())+1
         while k < NbMotifs :
          if List1[k] in Seq_i : 
           countm[k] +=1
          oc= Seq_i.count(List1[k])
          MatFinal[lindex][k] = str(float("{:.4f}".format(oc/nmotif)))
          k = k + 1
         MatFinal[lindex][-1] = ('C%(number)s' %{"number": clss})
         lindex = lindex + 1
         k = 0
         progressBar['value'] += (65/Nb_Seq)
         progressBar.update()
        else :
         clss += 1
       for a in range(1, Nb_Seq+1) :
        for b in range(0, NbMotifs) :	
          MatFinal[a][b] = str(float(MatFinal[a][b]) * ((Nb_Seq-1) / countm[b])).replace('.',',')
        progressBar['value'] += 10/Nb_Seq
        progressBar.update()
     except IOError as ee:
       Error_X = 1
       print(ee)

	   
	   
 def Block () :
  outFileBtn.config(state=DISABLED)
  inFileBtn.config(state=DISABLED)
  KgrmUpMenu.config(state=DISABLED)
  R1.config(state=DISABLED)
  R2.config(state=DISABLED)
  R3.config(state=DISABLED)
  R4.config(state=DISABLED)
  runBtn.config(state=DISABLED)
 
 def Unblock() :
  outFileBtn.config(state=NORMAL)
  inFileBtn.config(state=NORMAL)
  KgrmUpMenu.config(state=NORMAL)
  R1.config(state=NORMAL)
  R2.config(state=NORMAL)
  R3.config(state=NORMAL)
  R4.config(state=NORMAL)
  runBtn.config(state=NORMAL)


  
 def Run() :
    global sel_File_Nme
    global Nb_Seq
    global NbMotifs
    global MatFinal
    global File_Desc
    global Error_X	
    Block()
    progressBar.grid(row=5, column = 6, columnspan = 7,sticky = "NE", padx = 7 , pady = 5)
    start_time = time.time()
    aboutLbl.configure(text = "Waiting ...")	
    #******************************************************************
    #Extracting Distinct Motifs from our file    
    #******************************************************************
    kgrm = int(kgram.get())
    with open(File_Path.get(), 'r') as corpus:
     All_Motifs_List = []
     for line in corpus:
      li = line.rstrip("\n")
      if len(li) > 3 :
       All_Motifs_List += list((ngrams(li, kgrm)))
       Nb_Seq += 1
    progressBar['value'] = 5
    progressBar.update()
    Dist_Motifs_List = Distinct(All_Motifs_List)
    progressBar['value'] = 10
    progressBar.update()
    #******************************************************************
    #Concatenate each motif in a single string and add it to Final_Motifs_List 
    #******************************************************************
    j = 0
    Final_Motifs_List = []
    l = len(Dist_Motifs_List)
    while j < l:
     Final_Motifs_List.append(Concatenate_list_data(Dist_Motifs_List[j]))
     j = j + 1
    progressBar['value'] = 15
    progressBar.update()
    #******************************************************************
    #Insert our distinct motifs in the first row of our matrix 
    #******************************************************************
    NbMotifs = len(Final_Motifs_List)  #number of motifs
    MatFinal = np.zeros((Nb_Seq+1, NbMotifs+1),dtype=str).tolist()
    for jk in range(0, NbMotifs):
     MatFinal[0][jk] = Final_Motifs_List[jk]
    MatFinal[0][-1] = "class"     
    progressBar['value'] = 20
    progressBar.update()
    if MatType.get() == "Boolean" :
     BoolMat(Final_Motifs_List)
    elif MatType.get() == "Frequency" :
     FreqMat(Final_Motifs_List)
    elif MatType.get() == "Occurrence" :
     OccMat(Final_Motifs_List)
    else :
     TfIdfMat(Final_Motifs_List)
    if Error_X == 0 :
     tm = str(round((time.time() - start_time),3)) + " s"
     progressBar.grid_forget()
     File_Desc = "\nName :        "+ sel_File_Nme + "\nSize :        "+ File_Size +"\nNB SEQ found :        " + str(Nb_Seq) +"\nK-gram :        "+ str(kgram.get()) +"\nNB Motifs found :        "+ str(NbMotifs) +"\nRSLT type :        "+ MatType.get() +" Table"+"\nExecution time :        "+tm
     aboutLbl.configure(text = File_Desc)
     progressBar['value'] = 100
     progressBar.update() 
     Unblock()
     if not Dist_Path.get() == "" :
      exFileBtn.config(state=NORMAL)
     runBtn.config(state=DISABLED)
     showinfo("Done","Run completed successfully!")
    else :	
     Invalid_Struct()
	 
 def export() :
    start_time = time.time()
    global MatFinal
   #if not Dist_Path.get() == "" :
    #******************************************************************
    #Filling the Excel file with result
    #******************************************************************
    finalpath = Dist_Path.get() + "/"+sel_File_Nme[:-4]+ "-" + MatType.get() + "-"+kgram.get() + ".txt"    
    try :
      progressBar['value'] = 10
      progressBar.grid(row=5, column = 6, columnspan = 7,sticky = "NE", padx = 7 , pady = 5)
      progressBar.update()
      np.savetxt(finalpath, MatFinal,delimiter='\t', newline='\n',fmt='%s')
      progressBar['value'] = 100
      progressBar.update()
      tm = str(round((time.time() - start_time),3)) + " s" 
      msginf = "- File location :  " + finalpath + "\nExported in : " + tm 
      progressBar.grid_forget()
      showinfo("Success", msginf)
    except IOError as e:
      showerror("Problem occured !","EROOR : %s"%e) 

 
  
 #---------------------------------------------------------- *** GUI INTERFACE *** ------------------------------------------------------------------------------------------------
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 root.wm_title('Motif Extractor - IDIAG M1')
 root.geometry("665x320")
 root.resizable(0, 0)
 
 
 #Step one
 stepOne = tkinter.LabelFrame(root, text=" 1. Choose the SEQ file: ")
 stepOne.grid(row=0, columnspan=7, sticky='WE', padx=7, pady=5, ipadx=5, ipady=5)

 #ABT
 aboutLf = tkinter.LabelFrame(root, text=" About this file ", width=215)
 aboutLf.grid(row=0, column=9, columnspan=4, rowspan=4, sticky='NSEW', padx=5, pady=5)
 aboutLf.grid_propagate(0)
 
 #Step 2
 stepTwo = tkinter.LabelFrame(root, text=" 2. Select the K-gram size: ")
 stepTwo.grid(row=2, columnspan=7, sticky='WE', padx=7, pady=5, ipadx=5, ipady=5)

 #Step 3
 stepThree = tkinter.LabelFrame(root, text=" 3. Pick the matrix type: ")
 stepThree.grid(row=3, columnspan=7, sticky='WE', padx=7, pady=5, ipadx=5, ipady=5)
 
 #Step 4
 stepFour = tkinter.LabelFrame(root, text=" 4. Export the results: ")
 stepFour.grid(row=4, columnspan=7, sticky='WE', padx=7, pady=5, ipadx=5, ipady=5)
 
 #Filling ABT
 aboutLbl = tkinter.Label(aboutLf, text="Choose a file and hit RUN", justify=LEFT)
 aboutLbl.grid(row=0)

 #Filling STEP 1
 inFileLbl = tkinter.Label(stepOne, text="Select the File:")
 inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

 inFileTxt = tkinter.Entry(stepOne, state = DISABLED)
 inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)


 inFileBtn = tkinter.Button(stepOne, text="Load  ", width=10, command = OpenSeqFile,compound='right')
 inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
 
 #Filling STEP 2 
 kgrmLbl = tkinter.Label(stepTwo, text="Specify motif's length:")
 kgrmLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)
 
 KgrmUpMenu = tkinter.Spinbox(stepTwo, from_=2, to=5, textvariable=kgram, command = Sel_Kgrm)
 KgrmUpMenu.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')
 
 #Filling STEP 3
 R1 = tkinter.Radiobutton(stepThree, text="Boolean", variable=MatType, value="Boolean",command=Sel_Mtype)
 R1.grid( row=7, column=0, sticky='W')

 R2 = tkinter.Radiobutton(stepThree, text="Occurrence", variable=MatType, value="Occurrence",command=Sel_Mtype)
 R2.grid( row=7, column=1, sticky='W')

 R3 = tkinter.Radiobutton(stepThree, text="Frequency", variable=MatType, value="Frequency",command=Sel_Mtype)
 R3.grid( row=7, column=2, sticky='W')
 
 R4 = tkinter.Radiobutton(stepThree, text="TF-IDF", variable=MatType, value="TF-IDF",command=Sel_Mtype)
 R4.grid( row=7, column=3, sticky='W')
 
 #Filling STEP 4
 outFileLbl = tkinter.Label(stepFour, text="Choose the Destination folder:")
 outFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)
 
 outFileTxt = tkinter.Entry(stepFour, state = DISABLED)
 outFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
 
 outFileBtn = tkinter.Button(stepFour, text="Location  ", command = OpenDistFolder, compound="right")
 outFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
 
 #FILLING ACTION BUTTONS
 runBtn = tkinter.Button(root, text="Run  ", command = Run,height=3, width=12, compound="right", state=DISABLED)
 runBtn.grid(row=4, column=9, padx=5, pady=3)
 

 exFileBtn = tkinter.Button(root, text="Export  ", command = export,height=3, width=12, state= DISABLED, compound="right")
 exFileBtn.grid(row=4, column=11, columnspan=3, padx=5, pady=3)
 
 #FILLING TIPS SECTIONS
 tips = tkinter.Label(root, text=" Tips : - to visualize the resulted table, try exporting it!\n           - to export a file ,choose a location first!",justify=LEFT)
 tips.grid(row=5, columnspan = 7, sticky = "SW", padx = 7, pady = 5)
 
 progressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=210, mode='determinate')

 root.mainloop()
