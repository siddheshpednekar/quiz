import tkinter as tk
import mysql.connector
from operator import itemgetter

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
        self.userlogin = tk.Button(self.sf, text='user login', font=('arial', 25), bd=1, width=20, command=self.ulogin,
                                   fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.userlogin.place(x=550, y=250)
        self.adminlogin = tk.Button(self.sf, text='admin login', font=('arial', 25), bd=1, width=20,
                                    command=self.alogin, fg='white', bg='darkblue',
                                    activeforeground='white', activebackground='blue')
        self.adminlogin.place(x=550, y=350)

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

    def quiz(self):
        self.vadminname = self.eadminname.get()
        self.vpassword = self.epassword.get()
        proname = 'admin_login', [self.vadminname, self.vpassword]
        validation = db1(proname[0], proname[1])
        if validation:
            self.lf.destroy()
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

    def quiz(self):
        self.vusername = self.eusername.get()
        self.vpassword = self.epassword.get()
        proname = 'user_login', [self.vusername, self.vpassword]
        validation = db1(proname[0], proname[1])
        if validation:
            self.lf.destroy()
            UserWindow(root)
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
        self.breg = tk.Button(self.rf, text='register', command=self.reg, font=('arial', 25), bd=1, width=12,
                              fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.breg.place(x=600, y=420)
        self.label = tk.Label(self.rf, text="", font=('arial', 25), bd=1)
        self.label.place(x=500, y=490)

    def reg(self):
        self.runame = self.euname.get()
        self.rpass = self.epass.get()
        self.rcpasss = self.ecpass.get()
        proc = 'user_ver', [self.runame]
        res = db1(proc[0], proc[1])
        proc2 = 'user_reg', [self.runame, self.rpass]
        if self.runame == "" or self.rpass == "":
            self.label['text'] = "username or password cannot be empty"
        else:
            if not res:
                if self.rpass == self.rcpasss:
                    db1(proc2[0], proc2[1])
                    self.rf.destroy()
                    ULoginWindow(root)
                else:
                    self.label['text'] = "passwords do not match"
            else:
                self.label['text'] = "username already exists"


class UserWindow:
    def __init__(self, master):
        self.uf = tk.Frame(master)
        self.uf.pack(side=tk.TOP, pady=100)
        self.selected_quiz = tk.StringVar()
        self.gqp = 'get_quiz', []
        self.gq = list(map(itemgetter(0), db1(self.gqp[0], self.gqp[1])))
        print(self.gq)
        self.selected_quiz.set(self.gq[0])
        self.select_button = tk.OptionMenu(self.uf, self.selected_quiz, *self.gq)
        self.select_button.grid(row=0)
        self.select_button.config(font=('arial', 25), bd=1, width=11,
                                  fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.play_button = tk.Button(self.uf, text="play quiz", command=self.quiz, font=('arial', 25),
                                     bd=1, width=12,
                                     fg='white', bg='darkblue', activeforeground='white', activebackground='blue')
        self.play_button.grid(row=1)

    def quiz(self):
        quizselected = self.selected_quiz.get()
        self.uf.destroy()
        QuizFrame(root, quizselected)


class AdminWindow:
    def __init__(self, master):
        self.af = tk.Frame(master)
        self.af.pack(side=tk.TOP, pady=100)
        self.create_quiz = tk.Button(self.af, text="create quiz", width=12, font=('arial', 25), bd=1,
                                     command=self.createquiz, fg='white', bg='darkblue', activeforeground='white',
                                     activebackground='blue')
        self.create_quiz.grid(row=0, pady=10)
        self.play_quiz = tk.Button(self.af, text="play quiz", width=12, font=('arial', 25), bd=1,
                                   command=self.playquiz, fg='white', bg='darkblue', activeforeground='white',
                                   activebackground='blue')
        self.play_quiz.grid(row=1, pady=10)

    def createquiz(self):
        self.af.destroy()
        CreateQuiz1(root)

    def playquiz(self):
        self.af.destroy()
        UserWindow(root)


class CreateQuiz1:
    def __init__(self, master):
        self.cq1 = tk.Frame(master)
        self.cq1.place(x=200, y=150)

        self.qname = None
        self.qtime = None
        self.tid = None

        self.quizname = tk.Label(self.cq1, text="quiz name:", font=('arial', 25), bd=1, pady=20, padx=10)
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

    def nextframe(self):
        self.qname = self.equizname.get()
        self.qtime = int(self.etime_min.get())
        ins_top = 'insert_topic', [self.qname, self.qtime]
        self.tid = db1(ins_top[0], ins_top[1])[0][0]
        print(self.tid)
        self.cq1.destroy()
        CreateQuiz2(root, self.tid)


class CreateQuiz2:
    def __init__(self, master, tid):
        self.topid = tid

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

    def closewin(self):
        self.sq.destroy()
        self.cq.destroy()
        AdminWindow(root)

    def insertques(self):
        q = self.eqquestion.get()
        o1 = self.eqoption1.get()
        o2 = self.eqoption2.get()
        o3 = self.eqoption3.get()
        o4 = self.eqoption4.get()
        co = self.coropt.get()
        ins = 'insert_questions', [q, o1, o2, o3, o4, co, self.topid]
        db1(ins[0], ins[1])
        self.eqquestion.delete(0, 'end')
        self.eqoption1.delete(0, 'end')
        self.eqoption2.delete(0, 'end')
        self.eqoption3.delete(0, 'end')
        self.eqoption4.delete(0, 'end')


class QuizFrame:
    def __init__(self, master, quizselected):
        print(quizselected)
        self.qf = tk.Frame(master)
        self.qf.place(x=200, y=150)
        self.sf = tk.Frame(master)
        self.sf.place(width=sw, height=150, y=0)
        self.submitbtn = tk.Button(self.sf, text="submit", command=self.print_results, font=('arial', 20), bd=1,
                                   width=10, fg='white', bg='darkblue', activeforeground='white',
                                   activebackground='blue')
        self.submitbtn.place(x=1300, y=10)
        self.topic = tk.Label(self.sf, text=quizselected.upper(), font=('arial', 25), bd=20, fg="darkblue")
        self.topic.pack()
        self.timer = tk.Label(self.sf, text=" ", font=('arial', 25), bd=20, fg="red")
        self.timer.pack()

        self.qtp = 'quiztime', [quizselected]
        self.qt = db1(self.qtp[0], self.qtp[1])[0][0]*60
        self.set_idle_timer(self.qt)

        self.gqup = 'get_questions', [quizselected]
        self.gqu = list(map(itemgetter(0), db1(self.gqup[0], self.gqup[1])))
        self.qu_lis = list(range(1, len(self.gqu) + 1))
        print(self.gqu)

        self.gop = 'get_options', [quizselected]
        self.go = db1(self.gop[0], self.gop[1])
        print(self.go)

        self.gap = 'get_answers', [quizselected]
        self.ga = list(map(itemgetter(0), db1(self.gap[0], self.gap[1])))
        print(self.ga)

        self.gua = [0 for self.uas in range(0, len(self.ga))]
        print(self.gua)

        self.w = None
        self.bk = None
        self.ques_no = None
        self.selq = None

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
            btn = tk.Radiobutton(qf, text=" ", variable=self.opt_selected, value=b_val + 1,
                                 font=('arial', 25), bd=18)
            b.append(btn)
            r += 1
            btn.grid(row=r, column=2,
                     sticky="W")
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
        ScoreWindow(root, self.correct, len(self.gqu))

    def back_button(self):
        self.nxtbtn.configure(fg="white", activebackground="blue", activeforeground="white")
        a = int(self.opt_selected.get())
        print(a)
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
    def __init__(self, master, obtainedmarks, totalmarks):
        print(str(obtainedmarks) + "/" + str(totalmarks))
        self.sw = tk.Frame(master)
        self.sw.place(width=sw, height=150, y=0)
        self.score = tk.Label(self.sw, text="your score is: " + str(obtainedmarks) + "/" + str(totalmarks),
                              font=('arial', 25), bd=1, pady=20)
        self.score.pack()


run = StartWindow(root)
root.mainloop()
