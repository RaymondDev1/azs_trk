nazvanie_topliva = ['  92 ', '  95 ', ' 100 ', '  ДТ ']
tsena_topliva = [55.9, 48.9, 54.2, 63.2]


class Kolonka:

    def __init__(self, number):
        self.vid_topliva = []
        self.max_rezervuar_kolonka = [5000, 5000, 5000, 5000]
        self.rezervuar_kolonka = []
        self.number_kolonka = number
        self.filename = "d:\\Dannye\_azs_mn_trk_graph\_rezervuar" + str(self.number_kolonka) + ".txt"
        print(self.filename)
        f1 = open(self.filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            self.rezervuar_kolonka.append(ch)
        print(self.rezervuar_kolonka)

        self.filename_toplivo = "d:\\Dannye\_azs_mn_trk_graph\_kolonka_toplivo" + str(self.number_kolonka) + ".txt"
        print(self.filename_toplivo)
        f1 = open(self.filename_toplivo, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            self.vid_topliva.append(ch)
        print(self.vid_topliva)

    def finance(self, vybor_topliva, kolvo_topliva):
        stoimost = kolvo_topliva * tsena_topliva[vybor_topliva]
        return stoimost

    def zapravka_kolonki(self, vybor_topliva_z, zapravka):
        self.rezervuar_kolonka[vybor_topliva_z] -= zapravka
        cena_zapravki = self.finance(vybor_topliva_z, zapravka)
        self.zapis_file()
        return cena_zapravki

    def info(self):
        return self.rezervuar_kolonka

    def popolnenie_rezervuara_kolonki(self, vyb_dei, vybor_topliva_popolnenie, dozapravka):
        if vyb_dei==1:
            self.rezervuar_kolonka[vybor_topliva_popolnenie] = self.max_rezervuar_kolonka[vybor_topliva_popolnenie]
        else:
            self.rezervuar_kolonka[vybor_topliva_popolnenie] += dozapravka
        self.zapis_file()

    def zapis_file(self):
        f1 = open(self.filename, "w")
        for i in range(4):
            f1.write(str(self.rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    def correct(self, vybor_topliva_cor, korr_value_kolonki):
        self.rezervuar_kolonka[vybor_topliva_cor] = korr_value_kolonki
        self.zapis_file()

    def sbros_kolonka(self):
        self.rezervuar_kolonka = [0, 0, 0, 0]
        self.zapis_file()

    def get_max_rezervuar_kolonka(self):
        return self.max_rezervuar_kolonka


class AZS:

    def __init__(self):
        f1 = open("d:\\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", "r")
        b = f1.readline()
        f1.close()
        self.kolvo_kolonok = int(b)

        f1 = open("d:\\Dannye\_azs_mn_trk_graph\_vyruchka.txt", "r")
        b = f1.readline()
        f1.close()
        self.vyruchka = float(b)
        self.mas_kolonki = []
        for i in range(self.kolvo_kolonok):
            a = Kolonka(i)
            self.mas_kolonki.append(a)

    def act_top(self, nom_kol):
        act_toplivo = []
        for i in range(4):
            if self.mas_kolonki[nom_kol - 1].vid_topliva[i] == 1:
                act_toplivo.append(nazvanie_topliva[i])
        return act_toplivo

    def update_uni(self, txt1, txt2, txt3, vers):
        txt1.config(text="Количество колонок: " + str(self.kolvo_kolonok) + " Выручка = " + str(self.vyruchka),
                     font=("Arial", 10))
        for ii in range(self.kolvo_kolonok):
            txt2[ii].config(text='Остаток топлива на данный момент в колонке №' + str(ii + 1), font=("Arial", 10))
            rez_kol = self.mas_kolonki[ii].info()
            if vers==2:
                for jj in range(4):
                    if self.mas_kolonki[ii].vid_topliva[jj] == 0:
                        txt3[jj + ii * 4].config(text="Вид " + str(nazvanie_topliva[jj]) + "\n нет в наличии", foreground="grey")
                    elif rez_kol[jj] <= 200:
                        txt3[jj + ii * 4].config(text="Вид " + str(nazvanie_topliva[jj]) + "\n " + str(rez_kol[jj]),
                                              foreground="red")
                    else:
                        txt3[jj + ii * 4].config(text="Вид " + str(nazvanie_topliva[jj]) + "\n " + str(rez_kol[jj]),
                                             foreground="black")
            else:
                for jj in range(4):
                    if self.mas_kolonki[ii].vid_topliva[jj] == 0:
                        txt3[jj + ii * 4].config(text=str(nazvanie_topliva[jj]) + " нет в наличии", foreground="grey")
                    elif rez_kol[jj] <= 200:
                        txt3[jj + ii * 4].config(text=str(nazvanie_topliva[jj]) + " " + str(rez_kol[jj]),
                                              foreground="red")
                    else:
                        txt3[jj + ii * 4].config(text=str(nazvanie_topliva[jj]) + " " + str(rez_kol[jj]),
                                             foreground="black")


    def struct_vyvod(self, window):
        txt2 = []
        txt3 = []
        for i in range(self.kolvo_kolonok):
            a = Label(window)
            a.pack()
            a.config(text=str(i))
            txt2.append(a)
            for j in range(4):
                b = Label(window)
                b.pack()
                b.config(text=str(j))
                txt3.append(b)
        txt = []
        txt.append(txt2)
        txt.append(txt3)
        return txt

    def info(self):

        def wclose2():
            wind2.destroy()

        wind2 = Tk()
        wind2.title("Вывод информации о АЗС")
        wind2.geometry("800x600+700+1")

        for i in range(7):
            wind2.rowconfigure(index=i, weight=1)
        for j in range(8):
            wind2.columnconfigure(index=j, weight=1)

        txt21 = Label(wind2)
        txt21.grid(row=0, column=0, columnspan=8)

        txt22 = []
        txt23 = []
        pb2 = []
        for i in range(self.kolvo_kolonok):
            a = Label(wind2)
            if i < 2:
                a.grid(row=1, column=i*4, columnspan=4)
            else:
                a.grid(row=3, column=i*4-8, columnspan=4)
            a.config(text=str(i))
            txt22.append(a)
            for j in range(4):
                b = Label(wind2)
                mrk = self.mas_kolonki[i].get_max_rezervuar_kolonka()
                c = ttk.Progressbar(wind2, orient="vertical", maximum=mrk[j])
                if i == 0 or i == 2:
                    b.grid(row=i+2, column=j, sticky=N)
                    c.grid(row=i+2, column=j, sticky=S)
                else:
                    b.grid(row=i+1, column=j+4, sticky=N)
                    c.grid(row=i+1, column=j+4, sticky=S)
                b.config(text=str(j))
                txt23.append(b)
                pb2.append(c)
        self.update_uni(txt21, txt22, txt23,2)

        for ii in range(self.kolvo_kolonok):
            rez_kol_pb = self.mas_kolonki[ii].info()
            for jj in range(4):
                if self.mas_kolonki[ii].vid_topliva[jj] == 0:
                    pb2[jj + ii * 4].config(value=0)
                else:
                    pb2[jj + ii * 4].config(value=rez_kol_pb[jj])

        btn21 = Button(wind2)
        btn21.config(text="Закрыть", font=("Arial", 12), command=wclose2)
        btn21.grid(row=5, column=0, columnspan=8, pady=10)
        wind2.mainloop()

    def zapravka_azs(self):

        def wclose1():
            wind1.destroy()

        def combovvod_kol_zapravka(event):

            def combovvod_toplivo_zapravka(event):

                def wenter1():
                    kolvo_toplivo = e11.get()
                    e11.config(state="disabled")
                    if not (kolvo_toplivo.isdigit()) or \
                            int(kolvo_toplivo) > self.mas_kolonki[vybor_kol_zap - 1].rezervuar_kolonka[
                        nazvanie_topliva.index(vybor_toplivo_zap)] or \
                            int(kolvo_toplivo) <= 0:
                        txt14.config(text="Некорректное значение.", foreground="red")
                    else:
                        kolvo_toplivo = int(kolvo_toplivo)
                        self.vyruchka += self.mas_kolonki[vybor_kol_zap - 1].zapravka_kolonki(nazvanie_topliva.index(vybor_toplivo_zap), kolvo_toplivo)

                        txt14.config(text="Идёт заправка", foreground="red")

                        pb11 = ttk.Progressbar(wind1)
                        pb11.grid(row=13, column=1, rowspan=4)

                        pbvalue = 100
                        pb11.config(value=0, maximum=100, orient="vertical")
                        time1per = kolvo_toplivo/1000

                        while pbvalue > 0:
                            pbvalue -= 1
                            pb11.config(value=pbvalue)
                            time.sleep(time1per)
                            wind1.update()

                        txt14.config(text="Заправка завершена", foreground="green")

                        f1 = open("d:\\Dannye\_azs_mn_trk_graph\_vyruchka.txt", "w")
                        f1.write(str(self.vyruchka))
                        f1.close()
                        self.update_uni(txt11, txt12, txt13,1)

                    btn12.config(state="disabled")
                self.update_uni(txt11, txt12, txt13, 1)

                vybor_toplivo_zap = cbb12.get()
                cbb12.config(state="disabled")

                txt17 = Label(wind1)
                txt17.grid(row=9, column=1)
                txt17.config(text="Введите количество топлива", font=("Arial", 12))
                e11 = Entry(wind1)
                e11.grid(row=10, column=1)

                txt14 = Label(wind1)
                txt14.grid(row=12, column=1)

                btn12 = Button(wind1)
                btn12.config(text="Ввести", font=("Arial", 12), command=wenter1)
                btn12.grid(row=11, column=1)

            vybor_kol_zap = int(cbb11.get())
            cbb11.config(state="disabled")
            txt16 = Label(wind1)
            txt16.grid(row=7, column=1)
            txt16.config(text="Выберите вид топлива", font=("Arial", 12))

            cbb12 = ttk.Combobox(wind1)
            cbb12.config(values=self.act_top(vybor_kol_zap), state="readonly", font=("Arial", 14))
            cbb12.grid(row=8, column=1)
            cbb12.bind("<<ComboboxSelected>>", combovvod_toplivo_zapravka)

        wind1 = Tk()
        wind1.title("Заправка")
        wind1.geometry("800x650+400+1")

        for i in range(24):
            wind1.rowconfigure(index=i, weight=1)
        for j in range(2):
            wind1.columnconfigure(index=j, weight=1)

        txt11 = Label(wind1)
        txt11.config(text="Количество колонок: " + str(self.kolvo_kolonok) + " Выручка = " + str(self.vyruchka),
                     font=("Arial", 10))
        txt11.grid(row=0, column=0, columnspan=2)

        txt12 = []
        txt13 = []
        for i in range(self.kolvo_kolonok):
            a = Label(wind1)
            a.grid(row=i*5+1, column=0)
            a.config(text=str(i))
            txt12.append(a)
            for j in range(4):
                b = Label(wind1)
                b.grid(row=i*5+j+2)
                b.config(text=str(j))
                txt13.append(b)
        self.update_uni(txt11, txt12, txt13, 1)

        vybor_kol_zap = []
        for i in range(self.kolvo_kolonok):
            vybor_kol_zap.append(str(i + 1))

        txt15 = Label(wind1)
        txt15.grid(row=5, column=1)
        txt15.config(text="Выберите колонку", font=("Arial", 12))

        cbb11 = ttk.Combobox(wind1)
        cbb11.config(values=vybor_kol_zap, state="readonly", font=("Arial", 14))
        cbb11.grid(row=6, column=1)
        cbb11.bind("<<ComboboxSelected>>", combovvod_kol_zapravka)

        btn11 = Button(wind1)
        btn11.config(text="Закрыть", font=("Arial", 12), command=wclose1)
        btn11.grid(row=21, column=0, columnspan=2)
        wind1.mainloop()

    def popolnenie_rezervuara(self):

        def wclose3():
            wind3.destroy()

        def combovvod_kol_popolnenie(event):

            def combovvod_toplivo_popolnenie(event):

                def combovvod_popolnenie(event):

                    def wenter3():
                        dop_value_pop = e31.get()
                        e31.config(state="disabled")
                        if not (dop_value_pop.isdigit()) or \
                                int(dop_value_pop) > 5000-self.mas_kolonki[vybor_kol_pop-1].rezervuar_kolonka[nazvanie_topliva.index(vybor_toplivo_pop)] or \
                                int(dop_value_pop) < 0:
                            txt34.config(text="Некорректное значение.", foreground="red")
                        else:
                            dop_value_pop = int(dop_value_pop)
                            self.mas_kolonki[vybor_kol_pop - 1].popolnenie_rezervuara_kolonki(2, nazvanie_topliva.index(vybor_toplivo_pop),dop_value_pop)
                            self.update_uni(txt31, txt32, txt33, 3)
                            txt34.config(text="")
                        btn32.config(state="disabled")

                    vybor_var_pop = cbb33.get()
                    cbb33.config(state="disabled")
                    if vybor_var_pop == "Залить резервуар полностью":
                        if self.mas_kolonki[vybor_kol_pop - 1].rezervuar_kolonka[nazvanie_topliva.index(vybor_toplivo_pop)]==5000:
                            txt35 = Label(wind3)
                            txt35.grid(row=12, column=1)
                            txt35.config(text="Резервуар уже полон", foreground="red")
                        else:
                            self.mas_kolonki[vybor_kol_pop-1].popolnenie_rezervuara_kolonki(1,nazvanie_topliva.index(vybor_toplivo_pop),0)
                    elif vybor_var_pop == "Залить определённое количество топлива":
                        txt39 = Label(wind3)
                        txt39.grid(row=13, column=1)
                        txt39.config(text="Выберите количество топлива")
                        e31 = Entry(wind3)
                        e31.grid(row=14, column=1)

                        txt34 = Label(wind3)
                        txt34.grid(row=15, column=1)

                        btn32 = Button(wind3)
                        btn32.config(text="Ввести", font=("Arial", 12), command=wenter3)
                        btn32.grid(row=16, column=1)

                    self.update_uni(txt31, txt32, txt33, 3)

                vybor_toplivo_pop = cbb32.get()
                cbb32.config(state="disabled")

                vybor_deistviya = ["Залить резервуар полностью", "Залить определённое количество топлива"]
                txt38 = Label(wind3)
                txt38.grid(row=10, column=1)
                txt38.config(text="Выберите действие", font=("Arial", 12))
                cbb33 = ttk.Combobox(wind3)
                cbb33.config(values=vybor_deistviya, state="readonly", font=("Arial", 14))
                cbb33.grid(row=11, column=1)
                cbb33.bind("<<ComboboxSelected>>", combovvod_popolnenie)

            vybor_kol_pop = int(cbb31.get())
            cbb31.config(state="disabled")
            txt37 = Label(wind3)
            txt37.grid(row=8, column=1)
            txt37.config(text="Выберите вид топлива", font=("Arial", 12))

            cbb32 = ttk.Combobox(wind3)
            cbb32.config(values=self.act_top(vybor_kol_pop), state="readonly", font=("Arial", 14))
            cbb32.grid(row=9, column=1)
            cbb32.bind("<<ComboboxSelected>>", combovvod_toplivo_popolnenie)

        wind3 = Tk()
        wind3.title("Пополнение резервуара")
        wind3.geometry("800x650+400+1")

        for i in range(23):
            wind3.rowconfigure(index=i, weight=1)
        for j in range(2):
            wind3.columnconfigure(index=j, weight=1)

        vybor_kol_korr = []
        for i in range(self.kolvo_kolonok):
            vybor_kol_korr.append(str(i + 1))

        txt31 = Label(wind3)
        txt31.config(text="Количество колонок: " + str(self.kolvo_kolonok) + " Выручка = " + str(self.vyruchka),
                     font=("Arial", 10))
        txt31.grid(row=0, column=0, columnspan=2)

        txt32 = []
        txt33 = []
        for i in range(self.kolvo_kolonok):
            a = Label(wind3)
            a.grid(row=i * 5 + 1, column=0)
            a.config(text=str(i))
            txt32.append(a)
            for j in range(4):
                b = Label(wind3)
                b.grid(row=i * 5 + j + 2)
                b.config(text=str(j))
                txt33.append(b)
        self.update_uni(txt31, txt32, txt33,3)

        txt36 = Label(wind3)
        txt36.grid(row=6, column=1)
        txt36.config(text="Выберите колонку", font=("Arial", 12))
        cbb31 = ttk.Combobox(wind3)
        cbb31.config(values=vybor_kol_korr, state="readonly", font=("Arial", 14))
        cbb31.grid(row=7, column=1)
        cbb31.bind("<<ComboboxSelected>>", combovvod_kol_popolnenie)

        btn31 = Button(wind3)
        btn31.config(text="Закрыть", font=("Arial", 12), command=wclose3)
        btn31.grid(row=21, column=0, columnspan=2)
        wind3.mainloop()

    def sbros(self):

        def wclose4():
            wind4.destroy()

        def combovvod(event):

            def combovvod_kol(event):

                def combovvod_toplivo(event):
                    vybor_toplivo = cbb43.get()
                    cbb43.config(state="disabled")

                    def wenter4():
                        korr_value = e41.get()
                        e41.config(state="disabled")
                        if not (korr_value.isdigit()) or int(korr_value) > 5000 or int(korr_value) < 0:
                            txt44.config(text="Некорректное значение.", foreground="red")
                        else:
                            korr_value = int(korr_value)
                            self.mas_kolonki[vybor_kol - 1].correct(nazvanie_topliva.index(vybor_toplivo), korr_value)
                            self.update_uni(txt41, txt42, txt43, 4)
                            txt44.config(text="")

                    txt48 = Label(wind4)
                    txt48.grid(row=12, column=1)
                    txt48.config(text="Введите количество топлива")
                    e41 = Entry(wind4)
                    e41.grid(row=13, column=1)

                    txt44 = Label(wind4)
                    txt44.grid(row=15, column=1)

                    btn42 = Button(wind4)
                    btn42.config(text="Ввести", font=("Arial", 12), command=wenter4)
                    btn42.grid(row=14, column=1)

                vybor_kol = int(cbb42.get())
                cbb42.config(state="disabled")

                txt47 = Label(wind4)
                txt47.grid(row=10, column=1)
                txt47.config(text="Выберите вид топлива")

                cbb43 = ttk.Combobox(wind4)
                cbb43.config(values=self.act_top(vybor_kol), state="readonly", font=("Arial", 14))
                cbb43.grid(row=11, column=1)
                cbb43.bind("<<ComboboxSelected>>", combovvod_toplivo)

            vybor_var = cbb41.get()
            cbb41.config(state="disabled")
            if vybor_var == "Очистить резервуары":
                for i in range(self.kolvo_kolonok):
                    self.mas_kolonki[i].sbros_kolonka()
            elif vybor_var == "Скорректировать резервуары":
                vybor_kol_korr=[]
                for i in range(self.kolvo_kolonok):
                    vybor_kol_korr.append(str(i+1))
                txt46 = Label(wind4)
                txt46.grid(row=8, column=1)
                txt46.config(text="Выберите колонку")
                cbb42 = ttk.Combobox(wind4)
                cbb42.config(values=vybor_kol_korr, state="readonly", font=("Arial", 14))
                cbb42.grid(row=9, column=1)
                cbb42.bind("<<ComboboxSelected>>", combovvod_kol)
            elif vybor_var == "Очистить выручку":
                self.vyruchka = 0
            self.update_uni(txt41, txt42, txt43, 4)
            f1 = open("d:\\Dannye\_azs_mn_trk_graph\_vyruchka.txt", "w")
            f1.write(str(self.vyruchka))
            f1.close()

        wind4 = Tk()
        wind4.title("Корректировка статистики")
        wind4.geometry("800x650+400+1")

        for i in range(24):
            wind4.rowconfigure(index=i, weight=1)
        for j in range(2):
            wind4.columnconfigure(index=j, weight=1)

        txt41 = Label(wind4)
        txt41.config(text="Количество колонок: " + str(self.kolvo_kolonok) + " Выручка = " + str(self.vyruchka),
                     font=("Arial", 10))
        txt41.grid(row=0, columnspan=2)

        txt42 = []
        txt43 = []
        for i in range(self.kolvo_kolonok):
            a = Label(wind4)
            a.grid(row=i * 5 + 1, column=0)
            a.config(text=str(i))
            txt42.append(a)
            for j in range(4):
                b = Label(wind4)
                b.grid(row=i * 5 + j + 2)
                b.config(text=str(j))
                txt43.append(b)
        self.update_uni(txt41, txt42, txt43, 4)

        vybor = ["Очистить резервуары", "Скорректировать резервуары", "Очистить выручку"]
        txt45 = Label(wind4)
        txt45.grid(row=6, column=1)
        txt45.config(text="Выберите действие")
        cbb41 = ttk.Combobox(wind4)
        cbb41.config(values=vybor, state="readonly", font=("Arial", 14))
        cbb41.grid(row=7, column=1)
        cbb41.bind("<<ComboboxSelected>>", combovvod)

        btn41 = Button(wind4)
        btn41.config(text="Закрыть", font=("Arial", 12), command=wclose4)
        btn41.grid(row=21, columnspan=2)
        wind4.mainloop()


obj1_azs = AZS()

from tkinter import *
from tkinter import ttk
import time

wind = Tk()
wind.title("Оплата услуг АЗС")
wind.geometry("800x350")

btn = []
nadpisi_kn = ["Заправка", "Информация", "Пополнение резервуара",
              "Корректировка статистики"]
for i in range(4):
    a = Button()
    btn.append(a)
for i in range(4):
    btn[i].config(text=nadpisi_kn[i], font=("Arial", 20), width=30, pady=5, padx=5, background="black",
                  foreground="white")
    btn[i].place(x=140, y=20 + i * 80)

btn[0].config(command=obj1_azs.zapravka_azs)
btn[1].config(command=obj1_azs.info)
btn[2].config(command=obj1_azs.popolnenie_rezervuara)
btn[3].config(command=obj1_azs.sbros)


wind.mainloop()
