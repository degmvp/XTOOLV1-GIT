print('''
#-----------------------------------------------
# ✅ X-TOOLV1
# ✅ Python 3.7.4 alterado: 23/02/2023
# ✅ Objetivo: New tool X-TOOLV1 Python
#-----------------------------------------------''')
import subprocess
from tkinter import *
from functools import partial
import tkinter as tk
import io
from contextlib import redirect_stdout
import time
import timeit
from time import strftime
import matp04
import random
import math
import turtle
import importlib
import os, sys
#import pypyodbc
from PIL import Image, ImageFilter, ImageOps
#--------------------------------------------------------
import builtins
import collections
from _collections import defaultdict
#--------------------------------------------------------
from _operator import *
from turtle import *
from datetime import datetime
#--------------------------------------------------------
#import pyodbc
#---------------------------------------------------------
#import PyTur001
#---------------------------------------------------------
import pandas as pd
import numpy as np
#---------------------------------------------------------
import matplotlib.pyplot as plt
from  matplotlib import pyplot as plt
#------------------------------------
# from mpl_toolkits.mplot3d import axes3d
from csv import reader
#---------------------------------------------------------
from glob import glob
#---------------------------------------------------------
import shutil
#---------------------------------------
listofiles = []
instancia = Tk()
menu = Menu(instancia)
instancia.config(menu=menu)

width = 800
height = 600
x = (menu.winfo_screenwidth() //  2) - (width // 2)
y = (menu.winfo_screenheight() // 2) - (height // 2)
instancia.geometry('{}x{}+{}+{}'.format(width, height, x, y))
instancia.title('--->Advanced Support Tool - X-TOOLV1 <---')
instancia['bg'] = '#006'
instancia.resizable(width=False, height=False)

global sql
#-----------------------------------------------------------------------------------
import psycopg2 as db
import csv
#***************INICIO X1SCREEN***************** 
import tkinter as tk  # python 3 
from tkinter import font  as tkfont  # python 3 
import io 
from contextlib import redirect_stdout 
 
class SampleApp(tk.Tk): 
 
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs) 
 
        self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold", slant="italic") 
 
        # the container is where we'll stack a bunch of frames 
        # on top of each other, then the one we want visible 
        # will be raised above the others 
        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True) 
        container.grid_rowconfigure(0, weight=1) 
        container.grid_columnconfigure(0, weight=1) 
 
        self.frames = {} 
        for F in (StartPage, PageOne, PageTwo, Page3): 
            page_name = F.__name__ 
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame 
 
            # put all of the pages in the same location; 
            # the one on the top of the stacking order 
            # will be the one that is visible. 
            frame.grid(row=0, column=0, sticky="nsew") 
 
        self.show_frame("StartPage") 
 
    def show_frame(self, page_name): 
        '''Show a frame for the given page name''' 
        frame = self.frames[page_name] 
        frame.tkraise() 
 
 
class StartPage(tk.Frame): 
 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg='#006') 
        self.controller = controller 
        label = tk.Label(self, bd=8, text="Gerenciador de Telas  X1CPYSQL ", bg='GOLDENROD', 
                         font=controller.title_font) 
        label.pack(side="top", fill="x", pady=10) 
 
        button1 = tk.Button(self, bd=16, text="Chama Tela 1", bg='GOLDENROD', fg='black', 
                            command=lambda: controller.show_frame("PageOne")) 
        button2 = tk.Button(self, bd=16, text="Chama Tela 2", bg='red', fg='black', 
                            command=lambda: controller.show_frame("PageTwo")) 
        button4 = tk.Button(self, bd=16, text="Chama Tela 3", bg='GOLDENROD', fg='black', 
                            command=lambda: controller.show_frame("Page3")) 

        button1.pack() 
        button2.pack() 
        button4.pack() 
   
 

 
class PageOne(tk.Frame): 
 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg='gray') 
        self.controller = controller 
        label = tk.Label(self, bd=16, text="Tela 1 - App X1CPYSQL", bg='red', font=controller.title_font) 
        label.pack(side="top", fill="x", pady=10) 
 
        bt3 = tk.Button(self, bd=16, text="Visual Tela", bg='#006', fg='#FFF',command=self.visual) 
        bt3.pack() 
        bt1 = tk.Button(self, bd=16, text="Ler texto", bg='#006', fg='#FFF',command=self.helpForm) 
        bt1.pack() 
        bt2 = tk.Button(self, bd=16, text="Del texto", bg='#006', fg='#FFF',command=self.clearForm) 
        bt2.pack() 
 
        bt4 = tk.Button(self, bd=16, text="Close-V", bg='#006', fg='#FFF',command=self.close) 
        bt4.pack() 
 
        button = tk.Button(self, bd=16, text="Gerenciador", bg='red', 
                           command=lambda: controller.show_frame("StartPage")) 
        button.pack() 
        # ---------------------------------------------------- 
 
    def visual(self): 
        self.wintxt = tk.Tk() 
        self.wintxt.title('Visualização de Texto   X-TOOLV1 - Tela 1') 
 
        scrollbar = tk.Scrollbar(self.wintxt) 
        c = tk.Canvas(self.wintxt, background='#006', yscrollcommand=scrollbar.set) 
        scrollbar.config(command=c.yview) 
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.elframe = tk.Frame(c) 
        width = 600 
        height = 600 
        x = (self.wintxt.winfo_screenwidth() // 2) - (width // 2) 
        y = (self.wintxt.winfo_screenheight() // 2) - (height // 2) 
 
        c.pack(side='left', fill='both', expand=True) 
        c.create_window(0, 0, window=self.elframe, anchor='ne') 
        self.wintxt.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
        self.labex = tk.Label(self.elframe, wraplength=16000, width=80, height=500, text=' ', bg='#006', fg='#FFF') 
        self.labex.pack() 
        self.wintxt.update() 
        c.config(scrollregion=c.bbox('all'))
        
    def helpForm(self): 
        vet = [] 
        arqv = 'm:\\area_pycode\\binN07.py' 
        if arqv != '': 
            with open(arqv) as f: 
                for i in f: 
                    vet.append(i) 
        # redirecionamento da função print() 
        file = io.StringIO() 
        with redirect_stdout(file): 
            for i, x in enumerate(vet): 
                print("{0:<0}".format(vet[i]), end="") 
            output = file.getvalue() 
            self.labex['text'] = output 
 
    def clearForm(self): 
        self.labex['text'] = ' ' 
 
    def close(self): 
        self.wintxt.destroy() 
 
 
class PageTwo(tk.Frame): 
 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg='gray') 
        self.controller = controller 
        label = tk.Label(self, bd=8, text="Tela 2  - App  X-TOOLV1 ", bg='red', font=controller.title_font) 
        label.pack(side="top", fill="x", pady=10) 
 
        bt3 = tk.Button(self, bd=8, text="Visual Tela", bg='#006', fg='#FFF',command=self.visual2) 
        bt3.pack() 
 
        bt1 = tk.Button(self, bd=8, text="Ler texto", bg='#006', fg='#FFF', command=self.fonte) 
        bt1.pack() 
        bt2 = tk.Button(self, bd=8, text="Del texto", bg='#006', fg='#FFF', command=self.clearForm2) 
        bt2.pack() 
 
        bt4 = tk.Button(self, bd=8, text="Close-V", bg='#006', fg='#FFF', command=self.close2) 
        bt4.pack() 
        button = tk.Button(self, bd=8, text="Gerenciador", bg='red', 
                           command=lambda: controller.show_frame("StartPage")) 
        button.pack() 
        # ------------------------------------------------------------ 
 
    def visual2(self): 
        self.wintxt = tk.Tk() 
        self.wintxt.title('Visualização de Texto X-TOOLV1 - Tela 2') 
 
        scrollbar = tk.Scrollbar(self.wintxt) 
        c = tk.Canvas(self.wintxt, background='#006', yscrollcommand=scrollbar.set) 
        scrollbar.config(command=c.yview) 
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.elframe = tk.Frame(c) 
        width = 600 
        height = 600 
        x = (self.wintxt.winfo_screenwidth() // 2) - (width // 2) 
        y = (self.wintxt.winfo_screenheight() // 2) - (height // 2) 
 
        c.pack(side='left', fill='both', expand=True) 
        c.create_window(0, 0, window=self.elframe, anchor='ne') 
        self.wintxt.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
        self.labex = tk.Label(self.elframe, wraplength=16000, width=80, height=500, text=' ', bg='#006', fg='#FFF') 
        self.labex.pack() 
        self.wintxt.update() 
        c.config(scrollregion=c.bbox('all')) 
 
    def fonte(self): 
        vet = [] 
        arqv = 'm:\\XPYTOOLV1\\X1RDSQL.py' 
        if arqv != '': 
            with open(arqv) as f: 
                for i in f: 
                    vet.append(i) 
        # redirecionamento da função print() 
        file = io.StringIO() 
        with redirect_stdout(file): 
            for i, x in enumerate(vet): 
                print("{0:<0}".format(vet[i]), end="") 
            output = file.getvalue() 
            self.labex['text'] = output 
 
    def clearForm2(self): 
        self.labex['text'] = ' ' 
 
    def close2(self): 
        self.wintxt.destroy() 
 
 
class Page3(tk.Frame): 
 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg='gray') 
        self.controller = controller 
        label = tk.Label(self, bd=8, text="Tela 3  - App  X-TOOLV1 ", bg='red', font=controller.title_font) 
        label.pack(side="top", fill="x", pady=10) 
 
        bt3 = tk.Button(self, bd=8, text="Visual Tela", bg='#006', fg='#FFF',command=self.visual3) 
        bt3.pack() 
 
        bt1 = tk.Button(self, bd=8, text="Ler texto", bg='#006', fg='#FFF', command=self.fonte) 
        bt1.pack() 
        bt2 = tk.Button(self, bd=8, text="Del texto", bg='#006', fg='#FFF', command=self.clearForm3) 
        bt2.pack() 
 
        bt4 = tk.Button(self, bd=8, text="Close-V", bg='#006', fg='#FFF', command=self.close3) 
        bt4.pack() 
        button = tk.Button(self, bd=8, text="Gerenciador", bg='red', 
                           command=lambda: controller.show_frame("StartPage")) 
        button.pack() 
 
        # ------------------------------------------------------------ 
 
    def visual3(self): 
        self.wintxt = tk.Tk() 
        self.wintxt.title('Visualização de Texto   X-TOOLV1 - Tela 3') 
 
        scrollbar = tk.Scrollbar(self.wintxt) 
        c = tk.Canvas(self.wintxt, background='#006', yscrollcommand=scrollbar.set) 
        scrollbar.config(command=c.yview) 
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.elframe = tk.Frame(c) 
        width = 600 
        height = 600 
        x = (self.wintxt.winfo_screenwidth() // 2) - (width // 2) 
        y = (self.wintxt.winfo_screenheight() // 2) - (height // 2) 
 
        c.pack(side='left', fill='both', expand=True) 
        c.create_window(0, 0, window=self.elframe, anchor='ne') 
        self.wintxt.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
        self.labex = tk.Label(self.elframe, wraplength=16000, width=80, height=500, text=' ', bg='#006', fg='#FFF') 
        self.labex.pack() 
        self.wintxt.update() 
        c.config(scrollregion=c.bbox('all')) 
 
    def fonte(self): 
        vet = [] 
        arqv = 'm:\\XPYTOOLV1\\matp04.py' 
        if arqv != '': 
            with open(arqv) as f: 
                for i in f: 
                    vet.append(i) 
        # redirecionamento da função print() 
        file = io.StringIO() 
        with redirect_stdout(file): 
            for i, x in enumerate(vet): 
                print("{0:<0}".format(vet[i]), end="") 
            output = file.getvalue() 
            self.labex['text'] = output 
 
    def clearForm3(self): 
        self.labex['text'] = ' ' 
 
    def close3(self): 
        self.wintxt.destroy()  
#***************FINAL X1SCREEN*****************
class ooptxt(object):
    def __init__(self, instancia):
        self.font = ('Times New Roman', '12', 'bold')

        #Frame que contem os checkbuttons
        self.frame1 = Frame(instancia)
        self.frame4 = Frame(instancia)
        self.frame4.pack(side = RIGHT)

        #Frame que contem os botões especificos
        self.frame2 = Frame(instancia)
        self.frame2['bg'] = 'salmon4'
        self.frame3 = Frame(instancia)
        
        #Empacotamos as nossas frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        #Checkbutton----------------------------------------------------------------
        self.frame1.rel = tk.Button(relief=SUNKEN)
        self.frame1.rel['text'] = '00:00:00'
        self.frame1.rel.place(x=10,y=15)
        self.frame1.rel['font'] = 'Helvetica 12 bold'
        self.frame1.rel['bd'] = 16
        self.frame1.rel['bg'] = '#D4C4A8'
        self.frame1.rel['fg'] = 'black'

        #**************Toolbar ****************
        self.status = Label(instancia,text='Preparing status bar...',bg='salmon4',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************

        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'Salmon4',font = self.font,bd=16,command = self.tac)
        self.bhead.pack()

        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'salmon4',font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()

    
 
        #Botão Area-txt
        self.txt = Button(self.frame4, text = "Area-txt",\
                           bg = "#A9ACB6",pady=0,command = self.tela,bd=16, font = self.font)
        self.txt.pack()

        global botões
        botões = ('texto','Clock',\
                  'G3D', 'G1D',\
                  'G2D','GD4',\
                  'Goff', 'W-spool',\
                  'Read 0/99', 'Read-Dir',\
                  'IMAGE','CLOSE'\
                  )
        #Indexação de botões em frame-------------------------------------------------------
        for i in range(12):            
            if i % 2 == 0:
                 subframe = Frame(self.frame2)
                 subframe['bg'] = '#6A5D1B'
                 subframe.pack()                 
            a = Button(subframe,relief=SUNKEN,bd=16, text = botões[i],bg = '#D4C4A8', width = 10, padx = 5, \
                       command = partial(self.ColocaTexto, botões[i]))
            a['font'] = 'Helvetica 10 bold'
            a['fg'] = 'Navy'                         #'#6A5D1B'
            a.pack(side = LEFT,padx=4,pady=5)
        self.bt1 = Button(subframe,bd=16, text = 'Backup', bg = '#A9ACB6', width = 10, padx = 5,\
                           command = self.Bkp)
        self.bt1.pack(side = LEFT,padx=4,pady=5)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        subMenu = Menu(menu)
        subMenu ['bg'] = 'salmon4'
        subMenu ['fg'] = 'white'

        menu.add_cascade(label='Themes',menu=subMenu)
        subMenu.add_command(label='Orange      Skin As..', command=self.pr_new)
        subMenu.add_separator()
        subMenu.add_command(label='DodgerBlue  Skine..', command=self.pr_open)
        subMenu.add_separator()
        subMenu.add_command(label='salmon4     Skin As..', command=self.pr_projet)
        subMenu.add_separator()
        subMenu.add_command(label='YellowGreen Skin As..', command=self.pr_save)
        subMenu.add_separator()
        subMenu.add_command(label='Coral       Skin As..', command=self.pr_rec)
        subMenu.add_separator()
        subMenu.add_command(label='BurlyWood   Skin As ..', command=self.pr_newor)
        subMenu.add_separator()
        subMenu.add_command(label='Change      Image..', command=self.r_snake)
        subMenu.add_separator()
        subMenu.add_command(label='Read from  index 0 to 99..', command=self.pyc1)
        subMenu.add_separator()
        subMenu.add_command(label='Copy App to Backup..', command=self.DskBkp)
        subMenu.add_separator()
        subMenu.add_separator()
        subMenu.add_command(label='Exit', command=self.Final)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        oopMenu = Menu(menu)
        oopMenu ['bg'] = 'Orange'
        oopMenu ['fg'] = 'black'
        menu.add_cascade(label='GRAPH-Turtle', menu=oopMenu)
        oopMenu.add_command(label='Call Graph1..', command=self.r_ninja)
        oopMenu.add_separator()
        oopMenu.add_separator()
        oopMenu.add_command(label='Call fish..', command=self.r_fish)
        oopMenu.add_separator()
        oopMenu.add_command(label='Call Graph2..', command=self.r_ninja1)
        oopMenu.add_separator()
        oopMenu.add_separator()


        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        pdMenu = Menu(menu)
        pdMenu ['bg'] = 'DodgerBlue'
        pdMenu ['fg'] = 'white'

        menu.add_cascade(label='MOD1-PANDAS', menu=pdMenu)
        pdMenu.add_command(label='DataFrame Operations ')
        pdMenu.add_separator()
        pdMenu.add_separator()      
        pdMenu.add_command(label='T-Pandas 01 CMD..', command=self.xpan)
        pdMenu.add_separator()        
        pdMenu.add_command(label='T-Pandas 02 CMD....', command=self.r_pd2)
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 03 CMD....', command=self.r_pd3)
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 04 CMD....', command=self.r_pd4)
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 05 CMD....', command=self.r_pd5)
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 06 CMD....', command=self.r_pd6)
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 07 CMD....', command=self.r_pd7)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 08 CMD....', command=self.r_pd8)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 09 CMD....', command=self.r_pd9)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 10 CMD....', command=self.r_pd10)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 11 CMD....', command=self.r_pd11)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 12 CMD....', command=self.r_pd12)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 13 CMD....', command=self.r_pd13)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 14 CMD....', command=self.r_pd14)        
        pdMenu.add_separator()
        pdMenu.add_command(label='T-Pandas 15 CMD....', command=self.r_pd15)        
        pdMenu.add_separator() 
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        npMenu = Menu(menu)
        npMenu ['bg'] = 'salmon4'
        npMenu ['fg'] = 'white'

        menu.add_cascade(label='CMD-NUMPY', menu=npMenu)
        npMenu.add_command(label='Numpy Array Guide1..', command=self.r_np1)
        npMenu.add_separator()        
        npMenu.add_command(label='Numpy Array Guide2..', command=self.r_np2)
        npMenu.add_separator()     
        npMenu.add_command(label='Numpy Array Guide3..', command=self.r_np3)
        npMenu.add_separator()  
        npMenu.add_command(label='Numpy Array Guide4..', command=self.r_np4)
        npMenu.add_separator()     
        npMenu.add_command(label='Numpy Array Guide5..', command=self.r_np5)
        npMenu.add_separator()     
        npMenu.add_command(label='Numpy Array Guide6..', command=self.r_np6)
        npMenu.add_separator()
        npMenu.add_command(label='Numpy Array Guide7..', command=self.r_np7)
        npMenu.add_separator()
        npMenu.add_command(label='Numpy Array Guide8..', command=self.r_np8)
        npMenu.add_separator()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        viewMenu = Menu(menu)
        viewMenu ['bg'] = 'DodgerBlue'
        viewMenu ['fg'] = 'white'

        menu.add_cascade(label='PY-LOOP', menu=viewMenu)
        viewMenu.add_command(label='Looping Over a Range..', command=self.for_num)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over a Collection..', command=self.for_col)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over a Backwards..', command=self.for_bac)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over a Col-Indexes..', command=self.for_cix)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over 2 Collections..', command=self.for_twc)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over Sorted Order..', command=self.for_srt)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over Dic Keys Values..', command=self.for_dkv)
        viewMenu.add_separator()       
        viewMenu.add_command(label='Looping Over a Function..', command=self.for_fun)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over Enumerate..', command=self.for_enu)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Merge two Dics..', command=self.for_dfp)
        viewMenu.add_separator()
        viewMenu.add_command(label='Looping Over a List..', command=self.for_lst)
        viewMenu.add_separator()
        viewMenu.add_separator()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        winMenu = Menu(menu)
        winMenu ['bg'] = 'DodgerBlue'
        winMenu ['fg'] = 'white'

        menu.add_cascade(label='UTILITIES', menu=winMenu)
        winMenu.add_command(label='Screen.....', command=self.tela)
        winMenu.add_separator()
        winMenu.add_separator()
        winMenu.add_command(label='Call Prompt....', command=self.pr_callprompt)
        winMenu.add_separator()
        winMenu.add_command(label='Call Notepad.....', command=self.pr_call)
        winMenu.add_separator()
        winMenu.add_command(label='Call Explorer.....', command=self.pr_callie)
        winMenu.add_separator()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        wnMenu = Menu(menu)
        wnMenu ['bg'] = 'DodgerBlue'
        wnMenu ['fg'] = 'white'

        menu.add_cascade(label=' IPYTHON..  ', menu=wnMenu)
        wnMenu.add_command(label='Interactive Internet Connection!')
        wnMenu.add_separator()
        wnMenu.add_command(label='Jupyter Notebook online..', command=self.jup)
        wnMenu.add_separator()
        wnMenu.add_command(label='Ipython Local-online.....', command=self.ypy)
        wnMenu.add_separator()
        wnMenu.add_command(label='Screen Manage read-files txt..', command=self.screen)
        wnMenu.add_separator()
        wnMenu.add_separator()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       
        bwMenu = Menu(menu)
        bwMenu ['bg'] = 'DodgerBlue'
        bwMenu ['fg'] = 'white'

        menu.add_cascade(label=' MOD2-PANDAS ..  ', menu=bwMenu)
        bwMenu.add_command(label='DataFrame Operations ')
        bwMenu.add_separator()
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 01 Jupyter ', command=self.cli01)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 02 Jupyter ', command=self.cli02)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 03 Jupyter ', command=self.cli03)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 04 Jupyter ', command=self.cli04)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 05 Jupyter ', command=self.cli05)        
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 06 Jupyter ', command=self.cli06)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 07 Jupyter ', command=self.cli07)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 08 Jupyter', command=self.cli08)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 09 Jupyter', command=self.cli09)
        bwMenu.add_separator()
        bwMenu.add_command(label='Pandas 10 Jupyter', command=self.cli10)    

        bwMenu = Menu(menu)
        bwMenu ['bg'] = 'DodgerBlue'
        bwMenu ['fg'] = 'white'

        menu.add_cascade(label='MOD3-PANDAS', menu=bwMenu)
        bwMenu.add_command(label='Tricks Jupyter Repository')
        bwMenu.add_separator()
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 1-Create DataFrame', command=self.trick01)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 2-Rename columns', command=self.trick02)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 3-Reverse row order', command=self.trick03)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 4-Reverse column order', command=self.trick04)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 5-Select column by data type', command=self.trick05)
        bwMenu.add_separator() 
        bwMenu.add_command(label='trick 6-Convert strings to numbers', command=self.trick06)
        bwMenu.add_separator() 
        bwMenu.add_command(label='trick 7-Reduce DataFrame size', command=self.trick07)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 8-Select multiple slices', command=self.trick08)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 9-Build DF from multiplefiles(row-wise)', command=self.trick09)
        bwMenu.add_separator()
        bwMenu.add_command(label='trick 10 Build DF from multiplefiles(col-wise)', command=self.trick10)
        bwMenu.add_separator()
        global pyc 
        pyc = ['PYC001','PYC002','PYC003','PYC004','PYC005','PYC006','PYC007','PYC008','PYC009','PYC010',
               'PYC011','PYC012','PYC013','PYC014','PYC015','PYC016','PYC017','PYC018','PYC019','PYC020',
               'PYC021','PYC022','PYC023','PYC024','PYC025','PYC026','PYC027','PYC028','PYC029','PYC030',
               'PYC031','PYC032','PYC033','PYC034','PYC035','PYC036','PYC037','PYC038','PYC039','PYC040',
               'PYC041','PYC042','PYC043','PYC044','PYC045','PYC046','PYC047','PYC048','PYC049','PYC050',
               'PYC051','PYC052','PYC053','PYC054','PYC055','PYC056','PYC057','PYC058','PYC059','PYC060',
               'PYC061','PYC062','PYC063','PYC064','PYC065','PYC066','PYC067','PYC068','PYC069','PYC050',
               'PYC071','PYC072','PYC073','PYC074','PYC075','PYC076','PYC077','PYC078','PYC079','PYC050',
               'PYC081','PYC082','PYC083','PYC084','PYC085','PYC086','PYC087','PYC088','PYC089','PYC050',
               'PYC091','PYC092','PYC093','PYC094','PYC095','PYC096','PYC097','PYC098','PYC099','PYC100']

    def r_ninja(self):
        ninja = turtle.Turtle()
        ninja.speed(0)
        t=ninja

        for i in range(180):
            ninja.forward(100)           
            ninja.color('red')
            ninja.right(30)
            ninja.forward(20)
            ninja.left(60)
            ninja.forward(50)
            ninja.right(30)
    
            ninja.penup()
            ninja.setposition(0, 0)
            ninja.pendown()
    
            ninja.right(2)
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            ninja.color('YellowGreen')

    def r_ninja1(self):
        ninja1 = turtle.Turtle()
        ninja1.speed(0)
        t=ninja1
        for i in range(180):
            ninja1.forward(100)
            ninja1.color('red')
            ninja1.right(30)
            ninja1.forward(20)
            ninja1.left(60)
            ninja1.forward(50)
            ninja1.right(30)
    
            ninja1.penup()
            ninja1.setposition(0, 0)
            ninja1.pendown()
    
            ninja1.right(2)

    def pyc1(self):
        global spool_output
        #-------------------------------------------------
        #leitura do repositorio Python PYC001 a PYC100
        #-------------------------------------------------
        ix = int(input('Digite indice 0..99-->>'))
        sk = pyc[ix]+'.txt'
        #redirecionamento da função print()
        file = io.StringIO()
        with redirect_stdout(file):
            with open('m:\\area_51_python\\'+ sk,'r') as f:
                print(f.read())
                output = file.getvalue()
                self.status['text']= 'Processing --> python_learning.txt! '
                spool_output = output
                print(output)
                
 

            
    def trick01(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK01.txt','r') as f:
            print(f.read()) 

    def trick02(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK02.txt','r') as f:
            print(f.read())
   
    def trick03(self):
          with open('M:\\area_wpython3\\@@pantrick\\X1TRICK03.txt','r') as f:
            print(f.read())      

    def trick04(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK04.txt','r') as f:
            print(f.read())

    def trick05(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK05.txt','r') as f:
            print(f.read())
 
    def trick06(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK06.txt','r') as f:
            print(f.read())
   
    def trick07(self):        
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK07.txt','r') as f:
            print(f.read())
     
    def trick08(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK08.txt','r') as f:
            print(f.read())
   
        
    def trick09(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK09.txt','r') as f:
            print(f.read())
   
        
    def trick10(self):
        with open('M:\\area_wpython3\\@@pantrick\\X1TRICK10.txt','r') as f:
            print(f.read())
   
        

    def r_np1(self):
        global spool_output
        self.tela()
        vet = []
        arqv = 'm:\\area_wpython3\@@numpy\\np1data.txt'

        if arqv != '':
            with open(arqv) as f:
                for i in f:
                    vet.append(i)
                    #redirecionamento da função print()
                    file = io.StringIO()
                    with redirect_stdout(file):
                        for i,x in enumerate(vet):
                            print("{0:<0}".format(vet[i]),end="")
                        output = file.getvalue()
                        self.wintxt.labex['text']= output
                        self.status['text']= 'Processing --> rv_spool.txt! '
                        spool_output = output
                        print(output)
        
        print('CMD - Lib-Numpy Array Guide1 \n')
        with open('m:\\area_wpython3\@@numpy\\np1data.txt','r') as f:
            print(f.read())



            

    def r_np2(self):
        global spool_output
        self.tela()
        vet = []
        arqv = 'm:\\area_wpython3\@@numpy\\np2data.txt'

        if arqv != '':
            with open(arqv) as f:
                for i in f:
                    vet.append(i)
                    #redirecionamento da função print()
                    file = io.StringIO()
                    with redirect_stdout(file):
                        for i,x in enumerate(vet):
                            print("{0:<0}".format(vet[i]),end="")
                        output = file.getvalue()
                        self.wintxt.labex['text']= output
                        self.status['text']= 'Processing --> rv_spool.txt! '
                        spool_output = output
                        print(output)
                        
        print('CMD - Lib-Numpy Array Guide2 \n')
        with open('m:\\area_wpython3\@@numpy\\np2data.txt','r') as f:
            print(f.read())  

    def r_np3(self):
        print('CMD - Lib-Numpy Array Guide3\n')
        with open('m:\\area_wpython3\@@numpy\\np3data.txt','r') as f:
            print(f.read())  

              
    def r_np4(self):
        print('CMD - Lib-Numpy Array Guide4\n')
        with open('m:\\area_wpython3\@@numpy\\np4data.txt','r') as f:
            print(f.read())


            
    def r_np5(self):
        print('CMD - Lib-Numpy Array Guide5\n')
        with open('m:\\area_wpython3\@@numpy\\np5data.txt','r') as f:
            print(f.read())

    def r_np6(self):
        print('CMD - Lib-Numpy Array Guide6\n')
        with open('m:\\area_wpython3\@@numpy\\np6data.txt','r') as f:
            print(f.read())

            
    def r_np7(self):
        print('CMD - Lib-Numpy Array Guide7\n')
        with open('m:\\area_wpython3\@@numpy\\np7data.txt','r') as f:
            print(f.read())

    def r_np8(self):
        print('CMD - Lib-Numpy Array Guide8\n')
        with open('m:\\area_wpython3\@@numpy\\np8data.txt','r') as f:
            print(f.read())

            
        
    def cli01(self):
        print('Pandas 01 Jupyter\n')
        with open('M:\\area_wpython3\\@@dscience\\X1DSC01.txt','r') as f:
            print(f.read())

    def cli02(self):
        print('Pandas 02 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC02.txt','r') as f:
            print(f.read())

    def cli03(self):
        print('Pandas 03 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC03.txt','r') as f:
            print(f.read())


    def cli04(self):
        print('Pandas 04 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC04.txt','r') as f:
            print(f.read())
            
    def cli05(self):
        print('Pandas 05 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC05.txt','r') as f:
            print(f.read())

    def cli06(self):
        print('Pandas 06 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC06.txt','r') as f:
            print(f.read())

            
    def cli07(self):
        print('Pandas 07 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC07.txt','r') as f:
            print(f.read())
            
    def cli08(self):
        print('Pandas 08 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC08.txt','r') as f:
            print(f.read())
            
    def cli09(self):
        print('Pandas 09 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC09.txt','r') as f:
            print(f.read())
            
    def cli10(self):
        print('Pandas 10 Jupyter\n')
        with open('m:\\area_wpython3\\@@dscience\\X1DSC10.txt','r') as f:
            print(f.read())

    def change_steelor(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'BurlyWood', font = self.font,bd=16)
        self.bhead.pack()        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def change_steel(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'Orange', font = self.font,bd=16)
        self.bhead.pack()        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def change_blue(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'DodgerBlue', font = self.font,bd=16)
        self.bhead.pack()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def change_projet(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'salmon4',font = self.font,bd=16)
        self.bhead.pack()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def change_ygreen(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'YellowGreen',font = self.font,bd=16)
        self.bhead.pack()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def change_coral(self):
        self.bhead.destroy() 
        self.bhead = Button(self.frame1, text = 'X-TOOLV1',\
                                      bg = 'Coral',font = self.font,bd=16)
        self.bhead.pack()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

       
    def Final(self):
        instancia.destroy()




        #------------------------------------------------------------
        # PANDAS - Tutorial Guide1  X1PAN01
        #------------------------------------------------------------
    def r_pd1(self):
        
        alunos = {'Nome':['Ricardo','Pedro','Degmar','Lawrence'],
                  'Nota':[4,7,5.5,9],
                  'Aprovado':['Nao','Sim','Nao','Sim']}
        df = pd.DataFrame(alunos)
        print(df)
        
        #with open('m:\\XPANDAS\\@@pandas\\X1PAN01.txt','r') as f:
        #    print(f.read())
            

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide2
        #------------------------------------------------------------
    def r_pd2(self):
        with open('m:\\area_wpython3\@@pandas\\X1PAN02.txt','r') as f:
            print(f.read())
        
        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide3      
        #------------------------------------------------------------
    def r_pd3(self):
        with open('m:\\area_wpython3\@@pandas\\X1PAN03.txt','r') as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide4
        
        #------------------------------------------------------------
    def r_pd4(self):
        with open('m:\\area_wpython3\@@pandas\\X1PAN04.txt','r') as f:
            print(f.read())
        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide5        
        #------------------------------------------------------------
    def r_pd5(self):
        with open('m:\\area_wpython3\@@pandas\\X1PAN05.txt','r') as f:
            print(f.read())        
        

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide6        
        #------------------------------------------------------------
    def r_pd6(self):
        with open('m:\\area_wpython3\@@pandas\\X1PAN06.txt','r') as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide7        
        #------------------------------------------------------------
    def r_pd7(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN07.txt','r', encoding="utf8") as f:
            print(f.read())
        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide8       
        #------------------------------------------------------------
    def r_pd8(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN08.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide9      
        #------------------------------------------------------------
    def r_pd9(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN09.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide10      
        #------------------------------------------------------------
    def r_pd10(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN10.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide11      
        #------------------------------------------------------------
    def r_pd11(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN11.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide12      
        #------------------------------------------------------------
    def r_pd12(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN12.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide13      
        #------------------------------------------------------------
    def r_pd13(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN13.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide14      
        #------------------------------------------------------------
    def r_pd14(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN14.txt','r', encoding="utf8") as f:
            print(f.read())

        #------------------------------------------------------------
        # PANDAS - Tutorial Pandas Guide15      
        #------------------------------------------------------------
    def r_pd15(self):        
        with open('m:\\area_wpython3\@@pandas\\X1PAN15.txt','r', encoding="utf8") as f:
            print(f.read())


        #------------------------------------------------------------
        #Library Turtle the circle command
        #------------------------------------------------------------
    def yin(self,radius, color1, color2):
        width = 3
        color("navy", color1)
        begin_fill()
        circle(radius/2., 180)
        circle(radius, 180)
        left(180)
        circle(-radius/2., 180)
        end_fill()
        left(90)
        up()
        forward(radius*0.35)
        right(90)
        down()
        color(color1, color2)
        begin_fill()
        circle(radius*0.15)
        end_fill()
        left(90)
        up()
        backward(radius*0.35)
        down()
        left(90)
        
    def r_fish(self):
        self.yin(200, "navy", "green")
        self.yin(200, "white", "navy")

            

        #------------------------------------------------------------
        #Library Turtle G2D with source code
        #------------------------------------------------------------
    def r_pygcode2(self):
        print('><><><--->Library Turtle G2D with source code<---><><><')
        

    def r_pym(self):
        turtle.speed(0)
        turtle.color('navy')
        turtle.up()
        phi = (1+math.sqrt(5))/2
        i=360/math.pi*(phi)
        t=turtle
        t.setup(450,450)
        t.down()
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            turtle.color('orange')
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            turtle.color('green') 
    

    

        #------------------------------------------------------------
        #Looping Over many - range of numbers
        #------------------------------------------------------------
    def for_num(self):
        print('><><><--->LOOPING OVER A RANGE OF NUMBERS<---><><><')
        print('''--Python Code--\n
        for i in [0,1,2,3,4,5]:
            print(i**2)

        for i in range(6):
            print(i**2)
            
        --Python result--)
''')
        print('><' * 32)
        for i in [0,1,2,3,4,5]:
            print(i**2)
            
        print('><' * 32)
        for i in range(6):
            print(i**2)
            
        print('><' * 32)
        #------------------------------------------------------------
        #Looping Over many - a collection
        #------------------------------------------------------------
    def for_col(self):
        print('><><><--->LOOPING OVER A COLLECTION<---><><><')
        print('''--Python Code--\n
        colors = ['red', 'green', 'blue', 'yellow']
        for i in range(len(colors)):
            print(colors[i])
        
        for i in reversed(colors):
            print (i)
        for i in range(len(colors)-1, -1, -1):
            print (colors[i])
        for i in reversed(colors):
            print (i)
            
        --Python result--)
''')
        print('><' * 32)
        colors = ['red', 'green', 'blue', 'yellow']
        for i in range(len(colors)):
            print(colors[i])

        print('><' * 32)
        for i in reversed(colors):
            print (i)

        print('><' * 32)
        

    def for_bac(self):
        print('><><><--->LOOPING BACKWARDS<---><><><')
        print('''--Python Code--\n
        colors = ['red', 'green', 'blue', 'yellow']
        
        for i in range(len(colors)-1, -1, -1):
            print (colors[i])
            
        for i in reversed(colors):
            print (i)
''')
        colors = ['red', 'green', 'blue', 'yellow']
        for i in range(len(colors)-1, -1, -1):
            print (colors[i])
        for i in reversed(colors):
            print (i)
        print('><' * 32)

      
        #------------------------------------------------------------
        #Looping Over many - a collection and Indexes
        #------------------------------------------------------------
    def for_cix(self):
        print('><><><--->LOOPING OVER A COLLECTION AND INDICES<---><><><')
        print('''--Python Code--\n
        colors = ['red', 'green', 'blue', 'yellow']


        for i in range(len(colors)):
            print (i, '--->', colors[i])

        for i, color in enumerate(colors):
            print (i, '--->', color)
        print('><' * 32)
        
        --Python result--)

''')
        colors = ['red', 'green', 'blue', 'yellow']


        for i in range(len(colors)):
            print (i, '--->', colors[i])

        for i, color in enumerate(colors):
            print (i, '--->', color)
            
        print('><' * 32)
        


        #------------------------------------------------------------
        #Looping Over many - 2 collections
        #------------------------------------------------------------
    def for_twc(self):
        print('><><><--->LOOPING OVER TWO COLLECTIONS<---><><><')
        print('''--Python Code--\n
        names =  ['raymond', 'rachel', 'matthew','deg']
        colors = ['red', 'green', 'blue', 'yellow']

        n = min(len(names), len(colors))
        for i in range(n):
            print (names[i], '--->', colors[i])
  
        for name, color in zip(names, colors):
            print (name, '--->', color)
            
        --Python result--)
            
''')
        names =  ['raymond', 'rachel', 'matthew','deg']
        colors = ['red', 'green', 'blue', 'yellow']

        n = min(len(names), len(colors))
        for i in range(n):
            print (names[i], '--->', colors[i])
        print('><' * 32)
        for name, color in zip(names, colors):
            print (name, '--->', color)
        print('><' * 32)
        
        #------------------------------------------------------------
        #Looping Over many - In Sorted Order
        #------------------------------------------------------------
    def for_srt(self):
        print('><><><--->LOOPING IN SORTED ORDER<---><><><')
        print('''--Python Code--\n
        colors = ['yellow','red', 'green', 'blue', 'yellow']
        print (sorted(colors, key=len))

        --Python result--)
''')

        colors = ['yellow','red', 'green', 'blue', 'yellow']
        print (sorted(colors, key=len))
        
        print('><' * 32)    
               
        #------------------------------------------------------------
        #Looping Over many - Dic Keys an Values
        #------------------------------------------------------------
    def for_dkv(self):
        print('><><><--->LOOPING OVER DICTIONARY KEYS AND VALUES---><><><')
        print('''--Python Code--\n
        d = {'01': 'blue', '02': 'green', '03': 'red'}

        for k in d:
            print (k,'indices do dicionario--->')

        for k in d.keys():
            print ('--->',k,d[k])
        print (d.keys())
        
        --Python result--)

''')

        d = {'01': 'blue', '02': 'green', '03': 'red'}

        for k in d:
            print (k,'indices do dicionario--->')

        for k in d.keys():
            print ('--->',k,d[k])
        print (d.keys())
        
        print('><' * 32) 


        
        #------------------------------------------------------------
        #Looping Over many - enumerate
        #------------------------------------------------------------
    def for_enu(self):
        print('><><><--->LOOPING OVER Func enumerate)---><><><')
        print('''--Python Code--\n

        print('Impressão e geração da tabuada de 7')
        print('-----------------------------------')
        tab = []
        tab = [x * 7 for x in range(1,11)]
        for r1, r2 in enumerate(tab):
                r1 += 1
                if r1 < 10: print('7 x ',r1,r2) 
        print('7 x',r1,r2)        
        print('-----------------------------------')
    
        --Python result--)
    
''')
       
        print('Impressão e geração da tabuada de 7')
        print('-----------------------------------')
        tab = []
        tab = [x * 7 for x in range(1,11)]
        for r1, r2 in enumerate(tab):
                r1 += 1
                if r1 < 10: print('7 x ',r1,r2) 
        print('7 x',r1,r2)        
        print('-----------------------------------')
        print('><' * 32) 

        
        #------------------------------------------------------------
        #Looping Over many - funtions
        #------------------------------------------------------------
    def for_fun(self):
        print('><><><--->LOOPING OVER Func enumerate)---><><><')
        print('''--Python Code--\n
        def hshow(msg):
            s = ''
            for c in msg: s += chr(ord(c) - 30000)
            return print(s)

        def hide(msg):
            s = ''
            for c in msg: s += chr(ord(c) + 30000)
            return print(s)
        hide('degmar gomes barbosa')
        hshow('疔疕疗疝疑疢畐疗疟疝疕疣畐疒疑疢疒疟疣疑')

        --Python result--)
''')
        
        def hshow(msg):
            s = ''
            for c in msg: s += chr(ord(c) - 30000)
            return print(s)

        def hide(msg):
            s = ''
            for c in msg: s += chr(ord(c) + 30000)
            return print(s)
        hide('degmar gomes barbosa')
        hshow('疔疕疗疝疑疢畐疗疟疝疕疣畐疒疑疢疒疟疣疑')

        #------------------------------------------------------------
        #Looping Over many - Merge two Dics
        #------------------------------------------------------------
    def for_dfp(self):
        print('><><><--->Looping Over many - Merge two Dics---><><><')
        print('''--Python Code--\n
        vix = ['00','01','02','03','04','05','06','07','08','09']
        vtxt= ['txt00','txt01','txt02','txt03','txt04','txt05','txt06','txt07','txt08','txt09']

        print('indices do dicionario')
        vdic= dict(zip(vix, vtxt))
        print(vdic.keys())
        print()
        print('indices: e :elementos do dicionario')
        print(vdic)
        print()
        print('listagem do conteudo por linha indices:elementos')
        for k in vdic.keys():
            print ('--->',k,vdic[k])
            
        --Python result--)
''')
        vix = ['00','01','02','03','04','05','06','07','08','09']
        vtxt= ['txt00','txt01','txt02','txt03','txt04','txt05','txt06','txt07','txt08','txt09']

        print('indices do dicionario')
        vdic= dict(zip(vix, vtxt))
        print(vdic.keys())
        print()
        print('indices: e :elementos do dicionario')
        print(vdic)
        print()
        print('listagem do conteudo por linha indices:elementos')
        for k in vdic.keys():
            print ('--->',k,vdic[k])
        #------------------------------------------------------------
        #Looping Over many - A List
        #------------------------------------------------------------
    def for_lst(self):
        print('><><><--->Looping Over a List---><><><')
        print('''--Python Code--\n
        names = ['mariaGorete', 'Degmar', 'kecio', 'wallace',
                 'edinalva', 'joao', 'mariadasgracas', 'lawrence']

        for i in range(len(names)):
            print(names[i])
            
        print('><' * 10)

        for i in names:
            print(i)
        print('><' * 10)

        d = {'ix1': 'blue', 'ix2': 'green', 'ix3': 'red'}

        while d:
            key, value = d.popitem()
            print (key, '-->', value)

        
        --Python result--)
''')

        names = ['mariaGorete', 'Degmar', 'kecio', 'wallace',
                 'edinalva', 'joao', 'mariadasgracas', 'lawrence']

        for i in range(len(names)):
            print(names[i])
            
        print('><' * 10)

        for i in names:
            print(i)
        print('><' * 10)

        d = {'ix1': 'blue', 'ix2': 'green', 'ix3': 'red'}

        while d:
            key, value = d.popitem()
            print (key, '-->', value)
        
        print('><' * 32)
        
    def op_cmp3(self):
        dic = {'1':'Bitwise Operator',
               '2':'~ Bitwise unary NOT',
               '3':'& Bitwise AND',
               '4':'| Bitwise OR',
               '5':'^ Bitwise XOR',
               '6':'>> Shift Right',
               '7':'<< Shift left',
               '8':'& = Bitwise AND Assignment',
               '9':'|=  Bitwise OR  Assignment',
               '10':'^=  Bitwise XOR Assignment',
               '11':'>>= Shift Right Assignment',
               '12':'<<= Shift Left  Assignment',
               '13':'-----------------------------------',
               '14':'-----------------------------------',
               '15':'The Left Shift byte a=8, b=24;',
               '16':'int c',
               '17':'c=a<<2; 00001000 << 2 = 00100000=32',
               '18':'The Right Shift byte a=8, b=24;',
               '19':'int c ',
               '20':'c=a>>2; 00001000 >> 2= 00000010=2'
              }          
        for ref, ref1 in dic.items():
            print (ref, '=>',ref1)
        

    def ColocaTexto(self, texto):
        if texto == 'texto':
            self.r_dic()
        else:            
            if texto == 'Clock':                
                self.tac()
            else:
                if texto == 'G3D':
                    self.mat04()
                else:
                    if texto =='G1D':
                        self.shape()
                    else:
                        if texto == 'G2D':
                            self.r_pym()
                        else:
                            if texto == 'GD4':
                                self.r_pym4()
                            else:
                                if texto == 'Goff':
                                    self.r_clear()
                                else:
                                    if texto == 'CLOSE':
                                        self.r_stop()
                                    else:
                                        if texto == 'W-spool':
                                            self.r_spool()
                                        else:
                                            if texto == 'Read 0/99':
                                                self.pyc1()
                                            else:
                                                if texto == 'Read-Dir':
                                                    self.read_txt()
                                                else:
                                                    if texto == 'IMAGE':
                                                        self.r_image()



      
                                        
    def r_image(self):
        logo = PhotoImage(file = 'M:\\area_pycode\\pylog.gif')
        #Logo do aplicativo
        self.logo = Label(self.frame3,bg='black')
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

            
            
        
    def tela(self):
        self.wintxt=tk.Tk()
        self.wintxt.title('Area de Visualização de Texto - X-TOOLV1')
        scrollbar=tk.Scrollbar(self.wintxt)
        c=tk.Canvas(self.wintxt,background='GOLDENROD',yscrollcommand=scrollbar.set)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.elframe=tk.Frame(c)
        width = 650
        height = 650
        x = (self.wintxt.winfo_screenwidth() //  2) - (width // 2)
        y = (self.wintxt.winfo_screenheight() // 2) - (height // 2)

        c.pack(side='left',fill='both',expand=True)
        c.create_window(0,0,window=self.elframe,anchor='ne')
        self.wintxt.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.wintxt.labex = tk.Label(self.elframe,wraplength=16000,width=90,height=800,text='',bg='#006',fg='white')
        self.wintxt.labex.pack()
        self.wintxt.update()
        c.config(scrollregion=c.bbox('all'))
        
    def r_dic(self):
        global spool_output
        self.tela()
        vet = []         
        arqv = 'M:\\area_51_python\\PYC029.txt' 
        if arqv != '':
            with open(arqv) as f:
                for i in f:
                    vet.append(i)
                #redirecionamento da função print()
                file = io.StringIO()
                with redirect_stdout(file):
                    for i,x in enumerate(vet):
                        print("{0:36}".format(vet[i]),end="")
                        #print(vet[i],end="")
                output = file.getvalue()
                self.wintxt.labex['text']= output
                print(output)
                #self.wintxt.labex.pack(side = LEFT)
                self.status['text']= 'Processing --> catalog.txt! '
                spool_output = output
                
    def tac(self):
        self.frame1.rel['text'] = strftime('%H:%M:%S')
        self.frame1.rel.after(1000,self.tac)

    def clock(self):
        self.tac()
        
    def mat04(self):
        matp04.graf()

    def r_sort(self):
        PyTur001.r_main()

        #------------------------------------------------------------
        #Code - Quick Sort 
        #------------------------------------------------------------
    def r_csort(self):
        print('<--->Code - Quick Sort---><')
        with open('tdata.txt','r') as f:
            print(f.read())  
       
    
        #------------------------------------------------------------
        #Area de operações da LIB - Kivy
        #------------------------------------------------------------
            
    def shape(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        t = turtle.Pen()
        turtle.setup(450,450)
        turtle.bgcolor('black')
        turtle.speed(0)
        for x in range(180):
            t.pencolor(colors[x%6])
            t.width(x/100 + 1)
            t.forward(x)
            t.left(59)
    def r_pym(self):
        turtle.speed(0)
        turtle.color('navy')
        turtle.up()
        phi = (1+math.sqrt(5))/2
        i=360/math.pi*(phi)
        t=turtle
        t.setup(450,450)
        t.down()
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            turtle.color('orange')
        for x in range(144):
            t.right(i)
            u=i
            t.forward(400)
            turtle.color('green') 
    
    def r_pym4(self):
        painter = turtle
        painter.speed(0)
        painter.setup(350,350)
        painter.bgcolor('black')
        painter.pencolor("yellow")
        painter.setup(350,350)
        for i in range(40):
            painter.forward(50)
            painter.left(123) # Let's go counterclockwise this time             
        painter.pencolor("green")
        for i in range(40):
            painter.forward(100)
            painter.left(123)

    def r_clear(self):
        turtle.clear()
        turtle.bye()

    def r_stop(self):
        self.wintxt.destroy()

    def r_spool(self):
        xnome = random.sample(['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't','u', 'v', 'x', 'w', 'y','z'],  4)
        xnum  = random.sample([1, 2, 3, 4, 5,6,7,8,9,0],  4)
        xfile = ''.join(xnome) + ''.join(map(str, xnum)) + '_rspool.txt'
        print(xfile)
        arqv = open(xfile,'w')
        arqv.write(spool_output)
        arqv.close()
        print('rotina de r_spool com sucesso!')


    def read_txt(self):
        global listofiles
        vet = []        
        directory = 'M:\\area_pycode'
        os.chdir(directory)
        #redirecionamento da função print()
        file = io.StringIO()
        with redirect_stdout(file):
                 for files in os.listdir(directory):
                     if files.endswith('py'):
                         listofiles.append(files)
                         print(listofiles)
                         listofiles = sorted(listofiles)
                    
        xfile = ','.join(listofiles)
        print(xfile)
        output = listofiles

        self.status['text']= 'Processing --> write_spool.txt! '
        arqv = open('FileTxt.txt','w')
        arqv.write(str(output))
        arqv.close()        
        print('Read-Dir com sucesso!')
        
    def DskBkp(self):
        import shutil
        source=r'M:\\XPYTOOLV1\\X-TOOLV1.py'
        destination=r'L:\\XPYTOOLV1\\X-TOOLV1.py'
        shutil.copyfile(source, destination)
        print('backup X-TOOLV1.py ==> L:\XPYTOOLV1')
        #----------------------------------------------------

    def Bkp(self):
        import shutil
        source=r'M:\\XPYTOOLV1\\X-TOOLV1.py'
        destination='C:\\BACKUP\\X-TOOLV1.py'
        shutil.copyfile(source, destination)
        print('backup X-TOOLV1.py ==> C:\BACKUP')
        #----------------------------------------------------
    def pr_projet(self):
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'salmon4', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()
        self.frame2['bg'] = 'salmon4'
        self.status.destroy()
        #**************Toolbar ****************
        self.status = Label(instancia,text='Preparing status bar...',bg='salmon4',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_projet()
        print('salmon4 skin frame2')

    def pr_new(self):
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'Orange', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()
        self.frame2['bg'] = 'Orange'
        self.status.destroy()
        self.status = Label(instancia,text='Preparing status bar...',bg='Orange',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_steel()
        print('Orange skin frame2! ')

    def pr_newor(self):
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'BurlyWood', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()        
        self.frame2['bg'] = 'BurlyWood'
        self.status.destroy()
        self.status = Label(instancia,text='Preparing status bar...',bg='BurlyWood',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_steelor()
        print('BurlyWood skin frame2! ')

        
    
    def pr_open(self):
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'DodgerBlue', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()
        self.frame2['bg'] = 'DodgerBlue'
        self.status.destroy()
        self.status = Label(instancia,text='Preparing status bar...',bg='DodgerBlue',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_blue()
        print('SteelBlue skin frame2! ')    
    
    def pr_save(self):        
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'YellowGreen', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()
        self.frame2['bg'] = 'YellowGreen'
        self.status.destroy()
        #**************Toolbar ****************
        self.status = Label(instancia,text='Preparing status bar...',bg='YellowGreen',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_ygreen()
        print('Aluminio skin frame2')

    def pr_rec(self):
        self.b_enc.destroy()
        self.b_enc = Button(self.frame4, text = 'Finish!',\
                                      bg = 'Coral', font = self.font,bd=16, command = self.Final)
        self.b_enc.pack()
        self.frame2['bg'] = 'Coral'
        self.status.destroy()
        #**************Toolbar ****************
        self.status = Label(instancia,text='Preparing status bar...',bg='Coral',bd=1,relief=SUNKEN,anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        #**************Toolbar ****************
        self.change_coral()
        print('Coral skin frame2')

    
    #---------------------------------------- 
    #----------------------------------------
    def pr_run(self):
        global spool_output
        #redirecionamento da função print()
        file = io.StringIO()
        with redirect_stdout(file):
            print('><' * 22)
            print('Operações Python CMD >>>')
            print('><' * 22)
            print('ASCII CHARACTER : - UPPERCASE ALPHABET\n')
            for i in range(65,91):
                print(chr(i), end = ' ')
    
            print('\n')

            print('ASCII CHARACTER : - LOWERCASE ALPHABET\n')
            for i in range(97,123):
                print(chr(i), end = ' ')
            output = file.getvalue()
            self.wintxt.labex['text']= output
            self.status['text']= 'Processing --> Operações Python CMD >>>! '
            spool_output = output
        #------------------------------------------------------------
        #PYSQL QUERY XPYDB - CODE
        #------------------------------------------------------------

    #----------------------------------------
    #Chamadas de Programas UTILITARIOS WINDOWS   
    #----------------------------------------

    def pr_callprompt(self):
        subprocess.call(["cmd.exe"])
        print('Prompt chamado com sucesso!')
        self.status['text']= 'Processing --> Cmd Prompt! '
        
    def pr_call(self):
        subprocess.call(["notepad.exe"])     
        print('notepad chamado com sucesso!')
        self.status['text']= 'Processing --> Notepad! '

    def pr_callie(self):
        subprocess.call(["explorer.exe"])     
        print('explorer chamado com sucesso!')
        self.status['text']= 'Processing --> Explorer! '

      

    def jup(self):
        subprocess.call(["jupyter-notebook.exe"])     
        print('jupyter-notebook chamado com sucesso!')
        self.status['text']= 'Processing --> jupyter-notebook!'


    def ypy(self):
        subprocess.call(["ipython.exe"])     
        print('ipython-notebook chamado com sucesso!')
        self.status['text']= 'Processing --> jupyter-notebook!'    
       
       
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------         
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
    def qry_spool(self):
        xnome = random.sample(['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't','u', 'v', 'x', 'w', 'y','z'],  4)
        xnum  = random.sample([1, 2, 3, 4, 5,6,7,8,9,0],  4)
        xfile = ''.join(xnome) + ''.join(map(str, xnum)) + '_qryspool.txt'
        arqv = open(xfile,'w')
        arqv.write(spool_output_qry)
        arqv.close()        
        print('rotina de qry_spool com sucesso!')
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
    def pr_imgoff(self):
        self.logo.destroy()
        logo = PhotoImage(file = 'M:\\area_pycode\pylog.GIF')
        #Logo do aplicativo
        self.logo = Label(self.frame3,bg='black')
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()
    #---------------------------------------------------------------------------
    def screen(self):
        app = SampleApp() 
        app.title('Container Frame') 
        app.geometry("512x412")
        app.resizable(width=False, height=False)
        app.mainloop()
        
    #---------------------------------------------------------------------------------        
    #-------------------------------------------------------------------------------------

    def r_snake(self):
        logo = PhotoImage(file = 'M:\\area_pycode\\pysnake.gif')
        #Logo do aplicativo
        self.logo = Label(self.frame4,bg='black')
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

    def prx1(self):
        print("python m:\\X1RDSQL.py")
        

    def xpan(self):
                alunos = {'Nome':['Ricardo','Pedro','Degmar','Lawrence'],
                  'Nota':[4,7,5.5,9],
                  'Aprovado':['Nao','Sim','Nao','Sim']}
                df = pd.DataFrame(alunos)
                print(df)

b = ooptxt(instancia)        
instancia.mainloop()
