import tkinter as tk
from tkinter import messagebox
import mysql.connector
from operator import itemgetter
import random
from string import ascii_letters, digits
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

root = tk.Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("%dx%d" % (sw, sh))
root.resizable(0, 0)


def db1(name, parameters):
    mydb = mysql.connector.connect(host='localhost', user='root', password='188717', database='quiz')
    mycursor = mydb.cursor()
    mycursor.callproc(name, parameters)
    result = None
    for res in mycursor.stored_results():
        result = res.fetchall()
        print(result)
    mydb.commit()
    mydb.close()
    return result


uanm = ""
uarl = ""


class StartWindow:
    def __init__(self, master):
        self.sw = tk.Frame(master)
        self.sw.place(width=sw, height=sh)
        self.userlogin = tk.Button(self.sw, text='login', font=('arial', 25), bd=1, width=20, command=self.nextframe,
                                   fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.userlogin.place(x=550, y=250)
        self.adminlogin = tk.Button(self.sw, text='register', font=('arial', 25), bd=1, width=20,
                                    fg='white', bg='darkblue', command=self.registerframe,
                                    activeforeground='white', activebackground='blue')
        self.adminlogin.place(x=550, y=350)

    def nextframe(self):
        self.sw.destroy()
        SelectLogin(root)

    def registerframe(self):
        self.sw.destroy()
        RegisterWindow(root)


class SelectLogin:
    def __init__(self, master):
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=sh)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.userlogin = tk.Button(self.sf, text='user login', font=('arial', 25), bd=1, width=20, command=self.ulogin,
                                   fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.userlogin.place(x=550, y=250)
        self.adminlogin = tk.Button(self.sf, text='admin login', font=('arial', 25), bd=1, width=20,
                                    command=self.alogin, fg='white', bg='darkblue',
                                    activeforeground='white', activebackground='blue')
        self.adminlogin.place(x=550, y=350)

    def back(self):
        self.sf.destroy()
        StartWindow(root)

    def ulogin(self):
        self.sf.destroy()
        ULoginWindow(root)

    def alogin(self):
        self.sf.destroy()
        ALoginWindow(root)


class ALoginWindow:
    def __init__(self, master):
        self.lf = tk.Frame(master)
        self.lf.place(width=sw, height=sh)
        self.vadminname = None
        self.vpassword = None
        self.bckbtn = tk.Button(self.lf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.ladminname = tk.Label(self.lf, text='admin name:', font=('arial', 25), bd=1)
        self.ladminname.place(x=550, y=100)
        self.eadminname = tk.Entry(self.lf, font=('arial', 25), bd=1)
        self.eadminname.place(x=550, y=150)
        self.lpassword = tk.Label(self.lf, text='password:', font=('arial', 25), bd=1)
        self.lpassword.place(x=550, y=200)
        self.epassword = tk.Entry(self.lf, font=('arial', 25), bd=1, show="*")
        self.epassword.place(x=550, y=250)
        self.blogin = tk.Button(self.lf, text='login', command=self.quiz, font=('arial', 25), bd=1, width=19,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.blogin.place(x=550, y=320)
        self.label = None

    def back(self):
        self.lf.destroy()
        StartWindow(root)

    def quiz(self):
        global uanm, uarl
        self.vadminname = self.eadminname.get()
        self.vpassword = self.epassword.get()
        proname = 'admin_login', [self.vadminname, self.vpassword]
        validation = db1(proname[0], proname[1])
        if validation:
            self.lf.destroy()
            vrl = 'ver_role', [self.vadminname]
            uarl = db1(vrl[0], vrl[1])[0][0]
            print(uarl)
            uanm = self.vadminname
            AdminWindow(root)
        else:
            self.label = tk.Label(self.lf, text='invalid username or password', font=('arial', 25), bd=1)
            self.label.place(x=530, y=390)
            print("invalid username or password")


class ULoginWindow:
    def __init__(self, master):
        self.lf = tk.Frame(master)
        self.lf.place(width=sw, height=sh)
        self.vusername = None
        self.vpassword = None
        self.bckbtn = tk.Button(self.lf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.lusername = tk.Label(self.lf, text='username:', font=('arial', 25), bd=1)
        self.lusername.place(x=550, y=100)
        self.eusername = tk.Entry(self.lf, font=('arial', 25), bd=1)
        self.eusername.place(x=550, y=150)
        self.lpassword = tk.Label(self.lf, text='password:', font=('arial', 25), bd=1)
        self.lpassword.place(x=550, y=200)
        self.epassword = tk.Entry(self.lf, font=('arial', 25), bd=1, show="*")
        self.epassword.place(x=550, y=250)
        self.blogin = tk.Button(self.lf, text='login', command=self.quiz, font=('arial', 25), bd=1, width=12,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.blogin.place(x=600, y=320)
        self.label = None

    def back(self):
        self.lf.destroy()
        SelectLogin(root)

    def quiz(self):
        global uanm, uarl
        self.vusername = self.eusername.get()
        self.vpassword = self.epassword.get()
        proname = 'user_login', [self.vusername, self.vpassword]
        validation = db1(proname[0], proname[1])
        if validation:
            self.lf.destroy()
            vrl = 'ver_role', [self.vusername]
            uarl = db1(vrl[0], vrl[1])[0][0]
            print(uarl)
            uanm = self.vusername
            UserHome(root)
        else:
            self.label = tk.Label(self.lf, text='invalid username or password', font=('arial', 25), bd=1)
            self.label.place(x=530, y=390)
            print("invalid username or password")


class RegisterWindow:
    def __init__(self, master):
        self.rf = tk.Frame(master)
        self.rf.place(width=sw, height=sh)
        self.runame = None
        self.rpass = None
        self.rcpasss = None
        self.bckbtn = tk.Button(self.rf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.luname = tk.Label(self.rf, text='username:', font=('arial', 25), bd=1)
        self.luname.place(x=550, y=100)
        self.euname = tk.Entry(self.rf, font=('arial', 25), bd=1)
        self.euname.place(x=550, y=150)
        self.lpass = tk.Label(self.rf, text='password:', font=('arial', 25), bd=1)
        self.lpass.place(x=550, y=200)
        self.epass = tk.Entry(self.rf, font=('arial', 25), bd=1)
        self.epass.place(x=550, y=250)
        self.lcpass = tk.Label(self.rf, text='confirm password:', font=('arial', 25), bd=1)
        self.lcpass.place(x=550, y=300)
        self.ecpass = tk.Entry(self.rf, font=('arial', 25), bd=1)
        self.ecpass.place(x=550, y=350)
        self.role_selected = tk.StringVar()
        self.role_selected.set("student")
        print(self.role_selected.get())
        self.role1 = tk.Radiobutton(self.rf, text="student", variable=self.role_selected, value="student",
                                    font=('arial', 25), bd=1)
        self.role1.place(x=550, y=400)
        self.role2 = tk.Radiobutton(self.rf, text="teacher", variable=self.role_selected, value="teacher",
                                    font=('arial', 25), bd=1)
        self.role2.place(x=550, y=450)
        self.breg = tk.Button(self.rf, text='register', command=self.reg, font=('arial', 25), bd=1, width=12,
                              fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.breg.place(x=600, y=520)
        self.label = tk.Label(self.rf, text="", font=('arial', 25), bd=1)
        self.label.place(x=500, y=490)

    def back(self):
        self.rf.destroy()
        StartWindow(root)

    def reg(self):
        rl = self.role_selected.get()
        self.runame = self.euname.get()
        self.rpass = self.epass.get()
        self.rcpasss = self.ecpass.get()
        proc = 'user_ver', [self.runame]
        res = db1(proc[0], proc[1])
        proc2 = 'user_reg', [self.runame, self.rpass, rl]
        if self.runame == "" or self.rpass == "":
            self.label['text'] = "username or password cannot be empty"
        else:
            if not res:
                if self.rpass == self.rcpasss:
                    db1(proc2[0], proc2[1])
                    self.rf.destroy()
                    StartWindow(root)
                else:
                    self.label['text'] = "passwords do not match"
            else:
                self.label['text'] = "username already exists"


class UserHome:
    def __init__(self, master):
        self.uh = tk.Frame(master)
        self.uh.place(width=sw, height=sh)
        self.lobtn = tk.Button(self.uh, text='logout', font=('arial', 25), bd=1, width=10, command=self.lgout,
                               fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.lobtn.place(x=20, y=20)
        self.select_class = tk.Button(self.uh, text='play quiz', font=('arial', 25), bd=1, width=20,
                                      command=self.quiz,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.select_class.place(x=550, y=250)
        self.join_class = tk.Button(self.uh, text='join exam', font=('arial', 25), bd=1, width=20,
                                    fg='white', bg='darkblue', command=self.joinclass,
                                    activeforeground='white', activebackground='blue')
        self.join_class.place(x=550, y=350)

    def lgout(self):
        self.uh.destroy()
        StartWindow(root)

    def quiz(self):
        self.uh.destroy()
        ClassWindow(root)

    def joinclass(self):
        self.uh.destroy()
        UserClass(root)


class UserClass:
    def __init__(self, master):
        self.uc = tk.Frame(master)
        self.uc.place(width=sw, height=sh)
        self.bckbtn = tk.Button(self.uc, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.luclasscode = tk.Label(self.uc, text='examcode code:', font=('arial', 25), bd=1)
        self.luclasscode.place(x=550, y=100)
        self.euclasscode = tk.Entry(self.uc, font=('arial', 25), bd=1)
        self.euclasscode.place(x=550, y=150)
        self.join = tk.Button(self.uc, text='join', font=('arial', 25), bd=1, width=16, fg='white', bg='darkblue',
                              activeforeground='white', activebackground='blue', command=self.joinclass)
        self.join.place(x=570, y=220)
        self.lerror = tk.Label(self.uc, text='', font=('arial', 25), bd=1)

    def back(self):
        self.uc.destroy()
        UserHome(root)

    def joinclass(self):
        eclass = self.euclasscode.get()
        vercls = 'ver_class', [eclass, uanm]
        vvercls = db1(vercls[0], vercls[1])
        vercls2 = 'ver_class2', [eclass]
        vvercls2 = db1(vercls2[0], vercls2[1])
        if vvercls2:
            if vvercls:
                self.lerror['text'] = "you have already joined this exam"
                self.lerror.place(x=510, y=290)
                print(vvercls)
            else:
                insexinf = 'insert_examinfo', [eclass, uanm]
                self.lerror['text'] = "you joined "+eclass
                self.lerror.place(x=570, y=290)
                db1(insexinf[0], insexinf[1])
        elif eclass == "":
            self.lerror['text'] = "please enter correct code"
            self.lerror.place(x=550, y=290)
        else:
            self.lerror['text'] = "please enter correct code"
            self.lerror.place(x=510, y=290)


class ClassWindow:
    def __init__(self, master):
        self.cw = tk.Frame(master)
        self.cw.place(x=550, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.selected_quiz = tk.StringVar()
        self.gep = 'get_exam', [uanm]
        self.ge = list(map(itemgetter(0), db1(self.gep[0], self.gep[1])))
        print(self.ge)
        self.gecp = 'get_examcode', [uanm]
        self.gec = list(map(itemgetter(0), db1(self.gecp[0], self.gecp[1])))
        print(self.gec)
        self.exmlis = [self.ge[i] + "   ||   " + self.gec[i] for i in range(len(self.ge))]
        if len(self.ge) < 1:
            self.lerror = tk.Label(self.cw, text="join an examination to attempt it", font=('arial', 25), bd=1)
            self.lerror.grid(row=0)
        else:
            self.selected_quiz.set(self.exmlis[0])
            self.exname = tk.Label(self.cw, text='exam name   ||   exam code', font=('arial', 25), bd=1)
            self.exname.grid(row=0)
            self.select_button = tk.OptionMenu(self.cw, self.selected_quiz, *self.exmlis)

            self.select_button.grid(row=1, sticky="ew")

            self.select_button.config(font=('arial', 25), bd=1,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.select_button["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
            self.play_button = tk.Button(self.cw, text="select exam", font=('arial', 25),
                                         bd=1, command=self.quiz,
                                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button.grid(row=2)

    def back(self):
        self.cw.destroy()
        self.sf.destroy()
        print(uarl)
        if uarl == "student":
            UserHome(root)
        else:
            AdminWindow(root)

    def quiz(self):
        txt = self.selected_quiz.get()
        txtspl = txt.split("   ||   ")
        print(txtspl)
        ge2p = 'get_exam2', [txtspl[1]]
        ge2 = int(db1(ge2p[0], ge2p[1])[0][0])
        print(ge2)
        UserWindow(root, txtspl[1])
        self.cw.destroy()
        self.sf.destroy()


class UserWindow:
    def __init__(self, master, exm):
        print(exm)
        self.exam = exm
        self.uf = tk.Frame(master)
        self.uf.place(x=550, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.selected_quiz = tk.StringVar()
        self.gqp = 'get_quiz', [exm]
        self.gq = list(map(itemgetter(0), db1(self.gqp[0], self.gqp[1])))
        print(self.gq)
        if len(self.gq) < 1:
            self.lerror = tk.Label(self.uf, text='no subjects available', font=('arial', 25), bd=1)
            self.lerror.grid(row=0)
        else:
            self.selected_quiz.set(self.gq[0])
            self.select_button = tk.OptionMenu(self.uf, self.selected_quiz, *self.gq)
            self.select_button.grid(row=0, sticky="ew")
            self.select_button.config(font=('arial', 25), bd=1,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.select_button["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
            self.play_button = tk.Button(self.uf, text="start quiz", command=self.quiz, font=('arial', 25),
                                         bd=1, width=12,
                                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button.grid(row=1)

    def back(self):
        self.uf.destroy()
        self.sf.destroy()
        ClassWindow(root)

    def quiz(self):
        quizselected = self.selected_quiz.get()
        gsip = 'get_subjectid', [self.exam, self.selected_quiz.get()]
        gsi = db1(gsip[0], gsip[1])[0][0]
        print(gsi)
        vqts2p = 'ver_questions2', [self.exam, gsi]
        vqts2 = db1(vqts2p[0], vqts2p[1])[0][0]
        if vqts2 < 1:
            messagebox.showinfo("info", "admin failed to insert questions in this subject")
        else:
            self.uf.destroy()
            self.sf.destroy()
            QuizFrame(root, quizselected, gsi)


class AdminWindow:
    def __init__(self, master):
        print(uanm)
        self.af = tk.Frame(master)
        self.af.place(x=600, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.lobtn = tk.Button(self.sf, text='logout', font=('arial', 25), bd=1, width=10, command=self.lgout,
                               fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.lobtn.place(x=20, y=20)
        self.create_quiz = tk.Button(self.af, text="create test", width=12, font=('arial', 25), bd=1,
                                     command=self.createquiz, fg='white', bg='darkblue', activeforeground='white',
                                     activebackground='blue')
        self.create_quiz.grid(row=0, pady=10)
        self.play_quiz = tk.Button(self.af, text="play quiz", width=12, font=('arial', 25), bd=1,
                                   command=self.playquiz, fg='white', bg='darkblue', activeforeground='white',
                                   activebackground='blue')
        self.play_quiz.grid(row=1, pady=10)
        self.join_class2 = tk.Button(self.af, text='join exam', font=('arial', 25), bd=1, width=12,
                                     command=self.joinclass,
                                     fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.join_class2.grid(row=2, pady=10)
        self.stats = tk.Button(self.af, text='user stats', font=('arial', 25), bd=1, width=12,
                               command=self.statswin,
                               fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.stats.grid(row=3, pady=10)

    def lgout(self):
        self.af.destroy()
        self.sf.destroy()
        StartWindow(root)

    def createquiz(self):
        self.sf.destroy()
        self.af.destroy()
        ClassWindow2(root)

    def playquiz(self):
        self.sf.destroy()
        self.af.destroy()
        ClassWindow(root)

    def joinclass(self):
        self.sf.destroy()
        self.af.destroy()
        AdminClass(root)

    def statswin(self):
        self.sf.destroy()
        self.af.destroy()
        StatsWindow1(root)


class AdminClass:
    def __init__(self, master):
        self.ac = tk.Frame(master)
        self.ac.place(width=sw, height=sh)
        self.bckbtn = tk.Button(self.ac, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.luclasscode2 = tk.Label(self.ac, text='exam code:', font=('arial', 25), bd=1)
        self.luclasscode2.place(x=550, y=100)
        self.euclasscode2 = tk.Entry(self.ac, font=('arial', 25), bd=1)
        self.euclasscode2.place(x=550, y=150)
        self.join2 = tk.Button(self.ac, text='join', font=('arial', 25), bd=1, width=16, fg='white', bg='darkblue',
                               activeforeground='white', activebackground='blue', command=self.joinclass)
        self.join2.place(x=570, y=220)
        self.create = tk.Button(self.ac, text="create new", font=('arial', 20), bd=1, command=self.newclass,
                                width=10, fg='white', bg='darkblue', activeforeground='white',
                                activebackground='blue')
        self.create.place(x=1300, y=10)
        self.lerror = tk.Label(self.ac, text='', font=('arial', 25), bd=1)

    def back(self):
        self.ac.destroy()
        AdminWindow(root)

    def newclass(self):
        self.ac.destroy()
        AdminClass2(root)

    def joinclass(self):
        eclass = self.euclasscode2.get()
        vercls = 'ver_class', [eclass, uanm]
        vvercls = db1(vercls[0], vercls[1])
        vercls2 = 'ver_class2', [eclass]
        vvercls2 = db1(vercls2[0], vercls2[1])
        if vvercls2:
            if vvercls:
                self.lerror['text'] = "you are already admin of this exam"
                self.lerror.place(x=510, y=290)
                print(vvercls)
            else:
                insexinf = 'insert_examinfo', [eclass, uanm]
                self.lerror['text'] = "u r now admin of "+eclass
                self.lerror.place(x=510, y=290)
                db1(insexinf[0], insexinf[1])
        elif eclass == "":
            self.lerror['text'] = "please enter correct code"
            self.lerror.place(x=510, y=290)
        else:
            self.lerror['text'] = "please enter correct code"
            self.lerror.place(x=510, y=290)


class AdminClass2:
    def __init__(self, master):
        print(uanm)
        self.ac2 = tk.Frame(master)
        self.ac2.place(x=200, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)

        self.cnm = 'class'

        self.examcode2 = None
        self.gcod = 'gencode', []
        self.cod = list(map(itemgetter(0), db1(self.gcod[0], self.gcod[1])))
        print(self.cod)
        self.randomgenerate(self.cod)

        self.examname = tk.Label(self.ac2, text="exam name:", font=('arial', 25), bd=1, pady=20, padx=10)
        self.examname.grid(row=0, column=0, sticky='W')
        self.eexamname = tk.Entry(self.ac2, font=('arial', 25), bd=1, width=20)
        self.eexamname.grid(row=0, column=1, sticky='W')

        self.examcode = tk.Label(self.ac2, text="exam code:", font=('arial', 25), bd=1, pady=20, padx=10)
        self.examcode.grid(row=1, column=0, )

        self.createexam = tk.Button(self.ac2, text="next", width=12, font=('arial', 25), bd=1, command=self.createexam,
                                    fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.createexam.grid(row=2, column=1, sticky='W')
        print(self.examcode2['text'])

    def back(self):
        self.sf.destroy()
        self.ac2.destroy()
        AdminClass(root)

    def randomgenerate(self, cod):
        x = ascii_letters + digits + '+/'
        random_ = ''.join(list((random.choice(x) for _ in range(6))))
        while random_ in cod:
            random_ = ''.join(list((random.choice(x) for _ in range(6))))
        print(random_)
        self.examcode2 = tk.Label(self.ac2, text=random_, font=('arial', 25), bd=1)
        self.examcode2.grid(row=1, column=1, sticky='W')
        return self.examcode2

    def createexam(self):
        global uanm
        ename = self.eexamname.get()
        eclass = self.examcode2['text']
        insexm = 'insert_exam', [ename, eclass]
        db1(insexm[0], insexm[1])
        insexinf = 'insert_examinfo', [eclass, uanm]
        db1(insexinf[0], insexinf[1])
        self.ac2.destroy()
        AdminWindow(root)


class ClassWindow2:
    def __init__(self, master):
        self.cw2 = tk.Frame(master)
        self.cw2.place(x=550, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.selected_quiz = tk.StringVar()
        self.gep = 'get_exam', [uanm]
        self.ge = list(map(itemgetter(0), db1(self.gep[0], self.gep[1])))
        print(self.ge)
        self.gecp = 'get_examcode', [uanm]
        self.gec = list(map(itemgetter(0), db1(self.gecp[0], self.gecp[1])))
        print(self.gec)
        self.exmlis = [self.ge[i] + "   ||   " + self.gec[i] for i in range(len(self.ge))]
        if len(self.ge) < 1:
            self.lerror = tk.Label(self.cw2, text="join an examination to create quiz", font=('arial', 25), bd=1)
            self.lerror.grid(row=0)
        else:
            self.exname = tk.Label(self.cw2, text='exam name   ||   exam code', font=('arial', 25), bd=1)
            self.exname.grid(row=0)
            self.selected_quiz.set(self.exmlis[0])
            self.select_button = tk.OptionMenu(self.cw2, self.selected_quiz, *self.exmlis)
            self.select_button.grid(row=1, sticky="ew")
            self.select_button["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
            self.select_button.config(font=('arial', 25), bd=1,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button = tk.Button(self.cw2, text="select exam", font=('arial', 25),
                                         bd=1, width=12, command=self.quiz,
                                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button.grid(row=2)

    def back(self):
        self.cw2.destroy()
        self.sf.destroy()
        AdminWindow(root)

    def quiz(self):
        self.sf.destroy()
        txt = self.selected_quiz.get()
        txtspl = txt.split("   ||   ")
        print(txtspl)
        ge2p = 'get_exam2', [txtspl[1]]
        ge2 = int(db1(ge2p[0], ge2p[1])[0][0])
        print(ge2)
        CreateQuiz1(root, ge2)
        self.cw2.destroy()


class CreateQuiz1:
    def __init__(self, master, eid):
        self.exid = eid
        self.cq1 = tk.Frame(master)
        self.cq1.place(x=200, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)

        self.subname = None
        self.subtime = None
        self.subid = None

        self.quizname = tk.Label(self.cq1, text="subject name:", font=('arial', 25), bd=1, pady=20, padx=10)
        self.quizname.grid(row=0, column=0, sticky='W')
        self.equizname = tk.Entry(self.cq1, font=('arial', 25), bd=1, width=30)
        self.equizname.grid(row=0, column=1, sticky='W')

        self.time_min = tk.Label(self.cq1, text="time(minutes):", font=('arial', 25), bd=1, pady=20, padx=10)
        self.time_min.grid(row=1, column=0, sticky='W')
        self.etime_min = tk.Entry(self.cq1, font=('arial', 25), bd=1, width=20)
        self.etime_min.grid(row=1, column=1, sticky='W')

        self.nextques = tk.Button(self.cq1, text="next", width=12, font=('arial', 25), bd=1, command=self.nextframe,
                                  fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.nextques.grid(row=2, column=1, sticky='W')

        self.lerror = tk.Label(self.cq1, text="", font=('arial', 25), bd=1, pady=20, padx=10)
        self.lerror.grid(row=3, columnspan=2)

    def back(self):
        self.cq1.destroy()
        self.sf.destroy()
        ClassWindow2(root)

    def nextframe(self):
        self.subname = self.equizname.get()
        self.subtime = self.etime_min.get()
        if self.subname == "" or self.subtime == "":
            self.lerror['text'] = "please enter all details"
        else:
            try:
                self.subtime = int(self.etime_min.get())
            except ValueError:
                self.lerror['text'] = "please enter time in minutes"
            else:
                vsp = 'ver_subject', [self.subname, self.exid]
                vs = db1(vsp[0], vsp[1])
                if vs:
                    self.lerror['text'] = "" + self.subname + " already exists in this exam"
                else:
                    self.sf.destroy()
                    self.cq1.destroy()
                    CreateQuiz2(root, self.exid, self.subname, self.subtime)


class CreateQuiz2:
    def __init__(self, master, exid, subname, subtime):
        self.ins_sub = 'insert_subject', [subname, subtime, exid]
        self.subid = db1(self.ins_sub[0], self.ins_sub[1])[0][0]
        print(self.subid)

        self.sq = tk.Frame(master)
        self.sq.place(width=sw, height=150, y=0)

        self.submitqts = tk.Button(self.sq, text="finish", font=('arial', 20), bd=1, command=self.closewin,
                                   width=10, fg='white', bg='darkblue', activeforeground='white',
                                   activebackground='blue')
        self.submitqts.place(x=1300, y=50)

        self.cq = tk.Frame(master)
        self.cq.place(x=200, y=150)

        self.op_lis = [1, 2, 3, 4]
        self.coropt = tk.IntVar()
        self.coropt.set(self.op_lis[0])

        self.qquestion = tk.Label(self.cq, text="question:", font=('arial', 25), bd=1, pady=20)
        self.qquestion.grid(row=0, column=0, sticky='W')
        self.eqquestion = tk.Entry(self.cq, font=('arial', 25), bd=1, width=40)
        self.eqquestion.grid(row=0, column=1, sticky='W')

        self.qoption1 = tk.Label(self.cq, text="option1:", font=('arial', 25), bd=1, pady=20)
        self.qoption1.grid(row=1, column=0, sticky='W')
        self.eqoption1 = tk.Entry(self.cq, font=('arial', 25), bd=1)
        self.eqoption1.grid(row=1, column=1, sticky='W')

        self.qoption2 = tk.Label(self.cq, text="option2:", font=('arial', 25), bd=1, pady=20)
        self.qoption2.grid(row=2, column=0, sticky='W')
        self.eqoption2 = tk.Entry(self.cq, font=('arial', 25), bd=1)
        self.eqoption2.grid(row=2, column=1, sticky='W')

        self.qoption3 = tk.Label(self.cq, text="option3:", font=('arial', 25), bd=1, pady=20)
        self.qoption3.grid(row=3, column=0, sticky='W')
        self.eqoption3 = tk.Entry(self.cq, font=('arial', 25), bd=1)
        self.eqoption3.grid(row=3, column=1, sticky='W')

        self.qoption4 = tk.Label(self.cq, text="option4:", font=('arial', 25), bd=1, pady=20)
        self.qoption4.grid(row=4, column=0, sticky='W')
        self.eqoption4 = tk.Entry(self.cq, font=('arial', 25), bd=1)
        self.eqoption4.grid(row=4, column=1, sticky='W')

        self.qcoropt = tk.Label(self.cq, text="correct option:", font=('arial', 25), bd=1, pady=20)
        self.qcoropt.grid(row=5, column=0, sticky='W')
        self.ocoropt = tk.OptionMenu(self.cq, self.coropt, *self.op_lis)
        self.ocoropt.grid(row=5, column=1, sticky='W')
        self.ocoropt.config(font=('arial', 25), bd=1, width=11,
                            fg='white', bg='darkblue', activeforeground='white', activebackground='blue')

        self.nextques = tk.Button(self.cq, text="insert", width=12, font=('arial', 25), bd=1, command=self.insertques,
                                  fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.nextques.grid(row=6, column=1, sticky='W')
        self.lerror = tk.Label(self.cq, text="", font=('arial', 25), bd=1, pady=20)
        self.lerror.grid(row=7, columnspan=2)

    def closewin(self):
        vqtsp = 'ver_questions', [self.subid]
        vqts = db1(vqtsp[0], vqtsp[1])[0][0]
        print(vqts)
        if vqts > 0:
            self.sq.destroy()
            self.cq.destroy()
            AdminWindow(root)
        else:
            messagebox.showinfo("info", "please insert at least one question")

    def insertques(self):
        q = self.eqquestion.get()
        o1 = self.eqoption1.get()
        o2 = self.eqoption2.get()
        o3 = self.eqoption3.get()
        o4 = self.eqoption4.get()
        co = self.coropt.get()
        if q == "" or o1 == "" or o2 == "" or o3 == "" or o4 == "":
            self.lerror['text'] = "please  enter all the details"
        else:
            self.lerror['text'] = ''
            ins = 'insert_questions', [q, o1, o2, o3, o4, co, self.subid]
            db1(ins[0], ins[1])
            self.eqquestion.delete(0, 'end')
            self.eqoption1.delete(0, 'end')
            self.eqoption2.delete(0, 'end')
            self.eqoption3.delete(0, 'end')
            self.eqoption4.delete(0, 'end')


class QuizFrame:
    def __init__(self, master, quizselected, subid):
        print(subid)
        self.subjid = subid
        print(type(subid))
        print(quizselected)
        self.qf = tk.Frame(master)
        self.qf.place(x=200, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)

        self.submitbtn = tk.Button(self.sf, text="submit", command=self.subqts, font=('arial', 20), bd=1,
                                   width=10, fg='white', bg='darkblue', activeforeground='white',
                                   activebackground='blue')
        self.submitbtn.place(x=1300, y=10)
        self.topic = tk.Label(self.sf, text=quizselected.upper(), font=('arial', 25), bd=20, fg="darkblue")
        self.topic.pack()
        self.timer = tk.Label(self.sf, text=" ", font=('arial', 25), bd=20, fg="red")
        self.timer.pack()

        self.qtp = 'quiz_time', [subid]
        self.qt = db1(self.qtp[0], self.qtp[1])[0][0]*60
        self.set_idle_timer(self.qt)

        self.gqup = 'get_questions', [subid]
        self.gqu = list(map(itemgetter(0), db1(self.gqup[0], self.gqup[1])))
        self.qu_lis = list(range(1, len(self.gqu) + 1))
        print(self.gqu)

        self.gop = 'get_options', [subid]
        self.go = db1(self.gop[0], self.gop[1])
        print(self.go)

        self.gap = 'get_answers', [subid]
        self.ga = list(map(itemgetter(0), db1(self.gap[0], self.gap[1])))
        print(self.ga)

        self.gua = [0 for self.uas in range(0, len(self.ga))]
        print(self.gua)

        self.w = None
        self.bk = None
        self.ques_no = None
        self.selq = None

        self.btn = None
        self.opt_selected = tk.IntVar()
        self.q_selected = tk.IntVar()
        self.q_selected.set(self.qu_lis[0])
        self.qn = 0
        self.correct = 0

        self.ques = self.create_qustions(self.qf, self.qn)
        self.opts = self.create_options(self.qf, 4)
        self.display_questions(self.qn)

        self.nxtbtn = tk.Button(self.qf, text="next", command=self.next_button, font=('arial', 25), bd=1, width=7,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.nxtbtn.grid(row=6, column=2, sticky='W', padx=100)
        self.bckbtn = tk.Button(self.qf, text="back", command=self.back_button, font=('arial', 25), bd=1, width=7,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.grid(row=6, columnspan=2, sticky='W', padx=10)
        self.selq = tk.OptionMenu(self.qf, self.q_selected, *self.qu_lis, command=self.dropdownfun)
        self.selq["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
        self.selq.grid(row=0, column=0)
        self.selq.config(font=('arial', 20), bd=1, width=2,
                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')

    def set_idle_timer(self, t):
        try:
            hours, remainder = divmod(t, 3600)
            mins, secs = divmod(remainder, 60)
            timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
            self.timer['text'] = timeformat
            if t < 0:
                self.print_results()
                self.sf.destroy()
                self.qf.destroy()
            self.sf.master.after(1000, self.set_idle_timer, t - 1)
        except tk.TclError:
            pass

    def dropdownfun(self, value):
        self.bckbtn.configure(fg="white")
        self.nxtbtn.configure(fg="white")
        a = int(self.opt_selected.get())
        print(a)
        if self.opt_selected.get() > 0:
            self.selq["menu"].entryconfig(self.qn, background="green")
        self.gua[self.qn] = a
        print(self.gua)
        self.qn = value - 1
        self.display_questions(self.qn)

    def create_qustions(self, qf, qn):
        self.ques_no = tk.Label(qf, text=qn, font=('arial', 25), bd=20)
        self.ques_no.grid(row=0, column=1, sticky='E')
        self.w = tk.Label(qf, text=self.gqu[qn], font=('arial', 25), bd=20)
        self.w.grid(row=0, column=2, sticky='W')
        return self.w

    def create_options(self, qf, n):
        b_val = 0
        b = []
        r = 1
        while b_val < n:
            self.btn = tk.Radiobutton(qf, text=" ", variable=self.opt_selected, value=b_val + 1,
                                      font=('arial', 25), bd=18)
            b.append(self.btn)
            r += 1
            self.btn.grid(row=r, column=2, sticky="W")
            b_val += 1
        return b

    def display_questions(self, qn):
        b_val = 0
        qno = qn
        sqno = str(qno + 1)
        self.opt_selected.set(self.gua[self.qn])
        self.ques['text'] = self.gqu[qn]
        self.ques_no['text'] = sqno + ")"
        for op in self.go[qn]:
            self.opts[b_val]['text'] = op
            b_val += 1

    def subqts(self):
        sub = messagebox.askquestion("Submit", "are u sure u want to submit")
        if sub == "yes":
            self.print_results()
        else:
            if self.opt_selected.get() > 0:
                self.selq["menu"].entryconfig(self.qn, background="green")

    def print_results(self):
        a = int(self.opt_selected.get())
        print(a)
        self.gua[self.qn] = a
        print(self.gua)
        if self.gua[self.qn] == self.ga[self.qn]:
            print('correct')
        for i in range(0, len(self.ga)):
            if self.ga[i] == self.gua[i]:
                self.correct += 1
        print("result:", self.correct, "/", len(self.gqu))
        self.qf.destroy()
        self.sf.destroy()
        ScoreWindow(root, self.correct, len(self.gqu), self.subjid)

    def back_button(self):
        self.nxtbtn.configure(fg="white", activebackground="blue", activeforeground="white")
        a = int(self.opt_selected.get())
        print(a)
        if self.opt_selected.get() > 0:
            self.selq["menu"].entryconfig(self.qn, background="green")
        self.gua[self.qn] = a
        print(self.gua)
        self.qn -= 1
        if self.qn < 0:
            self.bckbtn.configure(fg="grey", activebackground="darkblue", activeforeground="grey")
            self.qn += 1
        else:
            self.bckbtn.configure(fg="white", activebackground="blue", activeforeground="white")
            self.q_selected.set(self.qn + 1)
            self.display_questions(self.qn)

    def next_button(self):
        self.bckbtn.configure(fg="white", activebackground="blue", activeforeground="white")
        a = int(self.opt_selected.get())
        print(a)
        self.gua[self.qn] = a
        print(self.gua)
        if self.opt_selected.get() > 0:
            self.selq["menu"].entryconfig(self.qn, background="green")
        if self.gua[self.qn] == self.ga[self.qn]:
            print('correct')
        else:
            print('wrong')
        self.qn += 1
        if self.qn >= len(self.gqu):
            self.qn -= 1
            self.nxtbtn.configure(fg="grey", activebackground="darkblue", activeforeground="grey")
        else:
            self.nxtbtn.configure(fg="white", activebackground="blue", activeforeground="white")
            self.q_selected.set(self.qn + 1)
            self.display_questions(self.qn)


class ScoreWindow:
    def __init__(self, master, obtainedmarks, totalmarks, subjid):
        self.subjectid = subjid
        self.obtmarks = obtainedmarks
        self.totmarks = totalmarks
        print(subjid)

        print(str(obtainedmarks) + "/" + str(totalmarks))
        self.guidp = 'get_userid', [uanm]
        self.guid = db1(self.guidp[0], self.guidp[1])[0][0]
        print(self.guid)
        self.gacp = 'get_attemptcount', [self.guid, subjid]
        self.gac = db1(self.gacp[0], self.gacp[1])[0][0] + 1
        print(self.gac)
        self.sw = tk.Frame(master)
        self.sw.place(width=sw, height=sh)
        self.atct = tk.Label(self.sw, text="attempt no.: " + str(self.gac),
                             font=('arial', 25), bd=1, pady=20)
        self.atct.pack(pady=20)
        self.score = tk.Label(self.sw, text="your score is: " + str(obtainedmarks) + "/" + str(totalmarks),
                              font=('arial', 25), bd=1, pady=20)
        self.score.pack(pady=20)

        self.home = tk.Button(self.sw, text="home", command=self.home, font=('arial', 25),
                              bd=1, width=12, fg='white', bg='darkblue', activeforeground='white',
                              activebackground='blue')
        self.home.pack(pady=20)
        self.ext = tk.Button(self.sw, text="exit", command=lambda: root.destroy(), font=('arial', 25),
                             bd=1, width=12, fg='white', bg='darkblue', activeforeground='white',
                             activebackground='blue')
        self.ext.pack(pady=20)

        self.insresp = 'insert_results', [self.guid, self.subjectid, self.gac, self.obtmarks, self.totmarks]
        db1(self.insresp[0], self.insresp[1])

    def home(self):
        self.sw.destroy()
        if uarl == "student":
            UserHome(root)
        else:
            AdminWindow(root)


class StatsWindow1:
    def __init__(self, master):
        self.cw = tk.Frame(master)
        self.cw.place(x=550, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.selected_quiz = tk.StringVar()
        self.gep = 'get_exam', [uanm]
        self.ge = list(map(itemgetter(0), db1(self.gep[0], self.gep[1])))
        print(self.ge)
        self.gecp = 'get_examcode', [uanm]
        self.gec = list(map(itemgetter(0), db1(self.gecp[0], self.gecp[1])))
        print(self.gec)
        self.exmlis = [self.ge[i] + "   ||   " + self.gec[i] for i in range(len(self.ge))]
        if len(self.ge) < 1:
            self.lerror = tk.Label(self.cw, text="join an examination to attempt it", font=('arial', 25), bd=1)
            self.lerror.grid(row=0)
        else:
            self.selected_quiz.set(self.exmlis[0])
            self.exname = tk.Label(self.cw, text='exam name   ||   exam code', font=('arial', 25), bd=1)
            self.exname.grid(row=0)
            self.select_button = tk.OptionMenu(self.cw, self.selected_quiz, *self.exmlis)

            self.select_button.grid(row=1, sticky="ew")

            self.select_button.config(font=('arial', 25), bd=1,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.select_button["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
            self.play_button = tk.Button(self.cw, text="select exam", font=('arial', 25),
                                         bd=1, command=self.quiz,
                                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button.grid(row=2)

    def back(self):
        self.cw.destroy()
        self.sf.destroy()
        print(uarl)
        if uarl == "student":
            UserHome(root)
        else:
            AdminWindow(root)

    def quiz(self):
        txt = self.selected_quiz.get()
        txtspl = txt.split("   ||   ")
        print(txtspl)
        ge2p = 'get_exam2', [txtspl[1]]
        ge2 = int(db1(ge2p[0], ge2p[1])[0][0])
        print(ge2)
        StatsWindow2(root, txtspl[1])
        self.cw.destroy()
        self.sf.destroy()


class StatsWindow2:
    def __init__(self, master, exm):
        print(exm)
        self.exam = exm
        self.uf = tk.Frame(master)
        self.uf.place(x=550, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.bckbtn = tk.Button(self.sf, text='back', font=('arial', 25), bd=1, width=10, command=self.back,
                                fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.bckbtn.place(x=20, y=20)
        self.selected_quiz = tk.StringVar()
        self.gqp = 'get_quiz', [exm]
        self.gq = list(map(itemgetter(0), db1(self.gqp[0], self.gqp[1])))
        print(self.gq)
        if len(self.gq) < 1:
            self.lerror = tk.Label(self.uf, text='no subjects available', font=('arial', 25), bd=1)
            self.lerror.grid(row=0)
        else:
            self.selected_quiz.set(self.gq[0])
            self.select_button = tk.OptionMenu(self.uf, self.selected_quiz, *self.gq)
            self.select_button.grid(row=0, sticky="ew")
            self.select_button.config(font=('arial', 25), bd=1,
                                      fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.select_button["menu"].config(font=('arial', 15), foreground='white', background="darkblue")
            self.play_button = tk.Button(self.uf, text="get stats", command=self.quiz, font=('arial', 25),
                                         bd=1, width=12,
                                         fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
            self.play_button.grid(row=1)

    def back(self):
        self.uf.destroy()
        self.sf.destroy()
        StatsWindow1(root)

    def quiz(self):
        quizselected = self.selected_quiz.get()
        gsip = 'get_subjectid', [self.exam, self.selected_quiz.get()]
        gsi = db1(gsip[0], gsip[1])[0][0]
        print(gsi)
        vqts2p = 'ver_questions2', [self.exam, gsi]
        vqts2 = db1(vqts2p[0], vqts2p[1])[0][0]
        if vqts2 < 1:
            messagebox.showinfo("info", "admin failed to insert questions in this subject")
        else:
            gres = 'get_results', [gsi]
            res = db1(gres[0], gres[1])
            print(res)
            un = np.array(list(map(itemgetter(0), res)))
            print(un)
            print(len(un))
            if len(un) < 1:
                messagebox.showinfo("info", "no one has attempted this quiz yet")
            else:
                mo = np.array(list(map(itemgetter(2), res)))
                print(mo)
                to = np.array(list(map(itemgetter(3), res)))
                print(to)
                mto = str(to[0])
                dat = {'users': un,
                       'marks_obtained': mo}
                df = pd.DataFrame(dat)
                dat2 = df.sort_values(by=['marks_obtained'], ascending=False)

                gr = sns.barplot(x="users", y="marks_obtained", data=dat2)
                for p in gr.patches:
                    gr.annotate(format(p.get_height(), '.1f'),
                                (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center',
                                size=15,
                                xytext=(0, 5),
                                textcoords='offset points')
                plt.xticks(rotation="vertical")
                plt.xlabel("username")
                plt.ylabel("marks obtained out of " + mto)
                plt.title(str(quizselected))
                plt.show()


run = StartWindow(root)
root.mainloop()
