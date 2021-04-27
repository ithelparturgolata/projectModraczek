# pip install pep8
# pip install pycodestyle
# pep8 --first dkmodraczekApp.py
# pycodestyle --first dk_modraczek.py
# coding: utf-8
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
import mysql.connector
from tkinter import messagebox
from smsapi.client import SmsApiPlClient
from smsapi.exception import SmsApiException
import os


db = mysql.connector.connect(host='localhost', user='root',
                             passwd='Savakiran03', database='bazadk')
cursor = db.cursor()


def update_rows(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)


def search_user():
    try:
        q2 = inentuser.get()
        if int(q2):
            messagebox.showerror("Uwaga", "Musisz podać nazwisko")
    except ValueError:
        query = "SELECT idUczen, ImieUczen, NazwiskoUczen, " \
                "DataUrodzenia, AdresUczen, ImieMatka, " \
                "PeselMatka, TelefonMatka, EmailMatka, " \
                "ImieOjciec, PeselOjciec, TelefonOjciec, " \
                "EmailOjciec, PoczatekZajec, KoniecZajec, " \
                "GrupaUczen FROM uczen WHERE NazwiskoUczen " \
                "LIKE '%" + q2 + "%' "
        cursor.execute(query)
        rows = cursor.fetchall()
        update_rows(rows)


def clear():
    query = "SELECT idUczen, ImieUczen, NazwiskoUczen, " \
            "DataUrodzenia, AdresUczen, ImieMatka, " \
            "PeselMatka, TelefonMatka, EmailMatka, " \
            "ImieOjciec, PeselOjciec, TelefonOjciec, " \
            "EmailOjciec, PoczatekZajec, KoniecZajec, " \
            "GrupaUczen FROM uczen"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_rows(rows)
    ent_user.delete(0, END)


def clear2():
    query = "SELECT idUczen, ImieUczen, NazwiskoUczen, " \
            "DataUrodzenia, AdresUczen, ImieMatka, " \
            "PeselMatka, TelefonMatka, EmailMatka, " \
            "ImieOjciec, PeselOjciec, TelefonOjciec, " \
            "EmailOjciec, PoczatekZajec, KoniecZajec, " \
            "GrupaUczen FROM uczen"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_rows(rows)
    ent_iduczen.delete(0, END)
    ent_imieuczen.delete(0, END)
    ent_nazwiskouczen.delete(0, END)
    ent_dataurodzenia.delete(0, END)
    ent_adres.delete(0, END)
    ent_imiematka.delete(0, END)
    ent_peselmatka.delete(0, END)
    ent_telefonmatka.delete(0, END)
    ent_emailmatka.delete(0, END)
    ent_imieojciec.delete(0, END)
    ent_peselojciec.delete(0, END)
    ent_telefonojciec.delete(0, END)
    ent_emailojciec.delete(0, END)
    ent_poczatekzajec.delete(0, END)
    ent_konieczajec.delete(0, END)
    # ent_grupa.delete(0, END)
    ent_imieuczen.focus()


def sendSMS():
    ent_telefonojciec.info = ent_telefonojciec.get()
    ent_telefonmatka.info = ent_telefonmatka.get()
    ent_wiadomoscsms.info = ent_wiadomoscsms.get()
    token = "oYeJUXpAF7Iu3l0tVHoxaxL4cEGSKUAbQKedJK6q"
    client = SmsApiPlClient(access_token=token)
    send_results = client.sms.send(to=(ent_telefonojciec.info,
                                       ent_telefonmatka.info),
                                   message=ent_wiadomoscsms.info,
                                   from_="DKMODRACZEK")
    for result in send_results:
        print(result.id, result.points, result.error)
    ent_wiadomoscsms.delete(0, END)


def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    tviduczen.set(item['values'][0])
    tvimieuczen.set(item['values'][1])
    tvnazwiskouczen.set(item['values'][2])
    tvdataurodzenia.set(item['values'][3])
    tvadres.set(item['values'][4])
    tvimiematka.set(item['values'][5])
    tvpeselmatka.set(item['values'][6])
    tvtelefonmatka.set(item['values'][7])
    tvemailmatka.set(item['values'][8])
    tvimieojciec.set(item['values'][9])
    tvpeselojciec.set(item['values'][10])
    tvtelefonojciec.set(item['values'][11])
    tvemailojciec.set(item['values'][12])
    tvpoczatekzajec.set(item['values'][13])
    tvkonieczajec.set(item['values'][14])
    tvgrupa.set(item['values'][15])


def update_customer():
    ImieUczen = tvimieuczen.get()
    NazwiskoUczen = tvnazwiskouczen.get()
    DataUrodzenia = tvdataurodzenia.get()
    AdresUczen = tvadres.get()
    ImieMatka = tvimiematka.get()
    PeselMatka = tvpeselmatka.get()
    TelefonMatka = tvtelefonmatka.get()
    EmailMatka = tvemailmatka.get()
    ImieOjciec = tvimieojciec.get()
    PeselOjciec = tvpeselojciec.get()
    TelefonOjciec = tvtelefonojciec.get()
    EmailOjciec = tvemailojciec.get()
    PoczatekZajec = tvpoczatekzajec.get()
    KoniecZajec = tvkonieczajec.get()
    GrupaUczen = tvgrupa.get()

    if messagebox.askyesno("Uwaga", "Czy chcesz zaktualizować Ucznia?"):
        query = "UPDATE uczen SET ImieUczen = %s, NazwiskoUczen = %s, " \
                "DataUrodzenia = %s, AdresUczen = %s, " \
                "ImieMatka = %s, PeselMatka = %s, " \
                "TelefonMatka = %s, EmailMatka = %s, " \
                "ImieOjciec = %s, PeselOjciec = %s, " \
                "TelefonOjciec = %s, EmailOjciec = %s, " \
                "PoczatekZajec = %s, KoniecZajec = %s, " \
                "GrupaUczen = %s WHERE idUczen = %s"
        val = (tvimieuczen.get(), tvnazwiskouczen.get(),
               tvdataurodzenia.get(), tvadres.get(),
               tvimiematka.get(), tvpeselmatka.get(),
               tvtelefonmatka.get(), tvemailmatka.get(),
               tvimieojciec.get(), tvpeselojciec.get(),
               tvtelefonojciec.get(), tvemailojciec.get(),
               tvpoczatekzajec.get(), tvkonieczajec.get(),
               tvgrupa.get(), tviduczen.get())
        cursor.execute(query, val)
        db.commit()
        clear()
        ent_user.delete(0, END)
        ent_iduczen.delete(0, END)
        ent_imieuczen.delete(0, END)
        ent_nazwiskouczen.delete(0, END)
        ent_dataurodzenia.delete(0, END)
        ent_adres.delete(0, END)
        ent_imiematka.delete(0, END)
        ent_peselmatka.delete(0, END)
        ent_telefonmatka.delete(0, END)
        ent_emailmatka.delete(0, END)
        ent_imieojciec.delete(0, END)
        ent_peselojciec.delete(0, END)
        ent_telefonojciec.delete(0, END)
        ent_emailojciec.delete(0, END)
        ent_poczatekzajec.delete(0, END)
        ent_konieczajec.delete(0, END)
        # ent_grupa.delete(0, END)
        ent_imieuczen.focus()
    else:
        return True


def delete_customer():
    customer_id = tviduczen.get()
    if messagebox.askyesno("Uwaga", "Czy na pewno chcesz usunąć Ucznia?"):
        query = "DELETE FROM uczen WHERE idUczen = " + customer_id
        cursor.execute(query)
        db.commit()
        clear()
        ent_user.delete(0, END)
        ent_iduczen.delete(0, END)
        ent_imieuczen.delete(0, END)
        ent_nazwiskouczen.delete(0, END)
        ent_dataurodzenia.delete(0, END)
        ent_adres.delete(0, END)
        ent_imiematka.delete(0, END)
        ent_peselmatka.delete(0, END)
        ent_telefonmatka.delete(0, END)
        ent_emailmatka.delete(0, END)
        ent_imieojciec.delete(0, END)
        ent_peselojciec.delete(0, END)
        ent_telefonojciec.delete(0, END)
        ent_emailojciec.delete(0, END)
        ent_poczatekzajec.delete(0, END)
        ent_konieczajec.delete(0, END)
        # ent_grupa.delete(0, END)
        ent_imieuczen.focus()
    else:
        return True


def show_grupa():
    lbl_grupa = Label(wrapper3, text=tvgrupa.get()).pack()
    lbl_grupa.grid(row=7, column=2, padx=5, pady=3, sticky=W)


def add_new():

    ImieUczen = tvimieuczen.get()
    NazwiskoUczen = tvnazwiskouczen.get()
    DataUrodzenia = tvdataurodzenia.get()
    AdresUczen = tvadres.get()
    ImieMatka = tvimiematka.get()
    PeselMatka = tvpeselmatka.get()
    TelefonMatka = tvtelefonmatka.get()
    EmailMatka = tvemailmatka.get()
    ImieOjciec = tvimieojciec.get()
    PeselOjciec = tvpeselojciec.get()
    TelefonOjciec = tvtelefonojciec.get()
    EmailOjciec = tvemailojciec.get()
    PoczatekZajec = tvpoczatekzajec.get()
    KoniecZajec = tvkonieczajec.get()
    GrupaUczen = tvgrupa.get()

    ent_imieuczen.delete(0, END)
    ent_nazwiskouczen.delete(0, END)
    ent_dataurodzenia.delete(0, END)
    ent_adres.delete(0, END)
    ent_imiematka.delete(0, END)
    ent_peselmatka.delete(0, END)
    ent_telefonmatka.delete(0, END)
    ent_emailmatka.delete(0, END)
    ent_imieojciec.delete(0, END)
    ent_peselojciec.delete(0, END)
    ent_telefonojciec.delete(0, END)
    ent_emailojciec.delete(0, END)
    ent_poczatekzajec.delete(0, END)
    ent_konieczajec.delete(0, END)
    # ent_grupa.delete(0, END)
    ent_imieuczen.focus()

    if messagebox.askyesno("Uwaga", "Dodać Ucznia?"):
        query = "INSERT INTO uczen (idUczen, ImieUczen, " \
                "NazwiskoUczen, DataUrodzenia, AdresUczen, " \
                "ImieMatka, PeselMatka, TelefonMatka, " \
                "EmailMatka, ImieOjciec, PeselOjciec, " \
                "TelefonOjciec, EmailOjciec, PoczatekZajec, " \
                "KoniecZajec, GrupaUczen) VALUES " \
                "(NULL, %s, %s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (ImieUczen, NazwiskoUczen,
                               DataUrodzenia, AdresUczen,
                               ImieMatka, PeselMatka,
                               TelefonMatka, EmailMatka,
                               ImieOjciec, PeselOjciec,
                               TelefonOjciec, EmailOjciec,
                               PoczatekZajec, KoniecZajec, GrupaUczen))
        db.commit()
        clear()
    else:
        return True


root = Tk()
pesel = StringVar()
inentuser = StringVar()
q2 = StringVar()
tviduczen = StringVar()
tvimieuczen = StringVar()
tvnazwiskouczen = StringVar()
tvdataurodzenia = StringVar()
tvadres = StringVar()
tvimiematka = StringVar()
tvpeselmatka = StringVar()
tvtelefonmatka = StringVar()
tvemailmatka = StringVar()
tvimieojciec = StringVar()
tvpeselojciec = StringVar()
tvtelefonojciec = StringVar()
tvemailojciec = StringVar()
tvpoczatekzajec = StringVar()
tvkonieczajec = StringVar()
tvgrupa = StringVar()
tvgrupa.set("Mądra Sówka")
tvwiadomoscsms = StringVar()

wrapper1 = LabelFrame(root, text="Lista uczniów", font=("bold", 12))
wrapper2 = LabelFrame(root, text="Szukaj", font=("bold", 12))
wrapper3 = LabelFrame(root, text="Uczeń - szczegóły", font=("bold", 12))

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6),
               show="headings", height="10")
trv.pack()
trv.heading(1, text="ID uczeń")
trv.heading(2, text="Imię uczeń")
trv.heading(3, text="Nazwisko uczneń")
trv.heading(4, text="Data urodzenia")
trv.heading(5, text="Adres")
trv.heading(6, text="Matka")
trv.bind('<Double 1>', getrow)

query = "SELECT idUczen, ImieUczen, NazwiskoUczen, " \
        "DataUrodzenia, AdresUczen, ImieMatka, " \
        "PeselMatka, TelefonMatka, EmailMatka, " \
        "ImieOjciec, PeselOjciec, TelefonOjciec, " \
        "EmailOjciec, PoczatekZajec, KoniecZajec, " \
        "GrupaUczen FROM uczen"
cursor.execute(query)
rows = cursor.fetchall()


lbl_search = Label(wrapper2, text="Szukaj", font=("bold", 13))
lbl_search.pack(side=tk.LEFT, padx=10)
ent_user = Entry(wrapper2, textvariable=inentuser, font=("bold", 13))
ent_user.pack(side=tk.LEFT, padx=6)
btn_user = Button(wrapper2, text="Szukaj",
                  command=search_user, font=("bold", 13))
btn_user.pack(side=tk.LEFT, padx=6)
cbtn_user = Button(wrapper2, text="Wyczyść",
                   command=clear, font=("bold", 13))
cbtn_user.pack(side=tk.LEFT, padx=6)

lbl_iduczen = Label(wrapper3, text="Id Uczeń:", font=("bold", 13))
lbl_iduczen.grid(row=0, column=0, padx=5, pady=3, sticky=W)
ent_iduczen = Entry(wrapper3, textvariable=tviduczen,
                    font=("bold", 13))
ent_iduczen.grid(row=0, column=1, padx=5, pady=3, sticky=W)

lbl_imieuczen = Label(wrapper3, text="Imię Uczeń:", font=("bold", 13))
lbl_imieuczen.grid(row=1, column=0, padx=5, pady=3, sticky=W)
ent_imieuczen = Entry(wrapper3, textvariable=tvimieuczen,
                      font=("bold", 13), width="30")
ent_imieuczen.grid(row=1, column=1, padx=5, pady=3, sticky=W)

lbl_nazwiskouczen = Label(wrapper3, text="Nazwisko Uczeń:", font=("bold", 13))
lbl_nazwiskouczen.grid(row=2, column=0, padx=5, pady=3, sticky=W)
ent_nazwiskouczen = Entry(wrapper3, textvariable=tvnazwiskouczen,
                          font=("bold", 13), width="30")
ent_nazwiskouczen.grid(row=2, column=1, padx=5, pady=3, sticky=W)

lbl_dataurodzenia = Label(wrapper3, text="Data urodzenia:", font=("bold", 13))
lbl_dataurodzenia.grid(row=3, column=0, padx=5, pady=3, sticky=W)
ent_dataurodzenia = Entry(wrapper3, textvariable=tvdataurodzenia,
                          font=("bold", 13), width="30")
ent_dataurodzenia.grid(row=3, column=1, padx=5, pady=3, sticky=W)

lbl_adres = Label(wrapper3, text="Adres:", font=("bold", 13))
lbl_adres.grid(row=4, column=0, padx=5, pady=3, sticky=W)
ent_adres = Entry(wrapper3, textvariable=tvadres,
                  font=("bold", 13), width="30")
ent_adres.grid(row=4, column=1, padx=5, pady=3, sticky=W)

lbl_imiematka = Label(wrapper3, text="Imię matka:", font=("bold", 13))
lbl_imiematka.grid(row=5, column=0, padx=5, pady=3, sticky=W)
ent_imiematka = Entry(wrapper3, textvariable=tvimiematka,
                      font=("bold", 13), width="30")
ent_imiematka.grid(row=5, column=1, padx=5, pady=3, sticky=W)

lbl_peselmatka = Label(wrapper3, text="Pesel matka:", font=("bold", 13))
lbl_peselmatka.grid(row=6, column=0, padx=5, pady=3, sticky=W)
ent_peselmatka = Entry(wrapper3, textvariable=tvpeselmatka,
                       font=("bold", 13), width="30")
ent_peselmatka.grid(row=6, column=1, padx=5, pady=3, sticky=W)

lbl_telefonmatka = Label(wrapper3, text="Telefon matka:", font=("bold", 13))
lbl_telefonmatka.grid(row=7, column=0, padx=5, pady=3, sticky=W)
ent_telefonmatka = Entry(wrapper3, textvariable=tvtelefonmatka,
                         font=("bold", 13), width="30")
ent_telefonmatka.grid(row=7, column=1, padx=5, pady=3, sticky=W)

lbl_emailmatka = Label(wrapper3, text="Email matka:", font=("bold", 13))
lbl_emailmatka.grid(row=8, column=0, padx=5, pady=3, sticky=W)
ent_emailmatka = Entry(wrapper3, textvariable=tvemailmatka,
                       font=("bold", 13), width="30")
ent_emailmatka.grid(row=8, column=1, padx=5, pady=3, sticky=W)

lbl_imieojciec = Label(wrapper3, text="Imię ojciec:", font=("bold", 13))
lbl_imieojciec.grid(row=1, column=2, padx=5, pady=3, sticky=W)
ent_imieojciec = Entry(wrapper3, textvariable=tvimieojciec,
                       font=("bold", 13), width="30")
ent_imieojciec.grid(row=1, column=3, padx=5, pady=3, sticky=W)

lbl_peselojciec = Label(wrapper3, text="Pesel ojciec:", font=("bold", 13))
lbl_peselojciec.grid(row=2, column=2, padx=5, pady=3, sticky=W)
ent_peselojciec = Entry(wrapper3, textvariable=tvpeselojciec,
                        font=("bold", 13), width="30")
ent_peselojciec.grid(row=2, column=3, padx=5, pady=3, sticky=W)

lbl_telefonojciec = Label(wrapper3, text="Telefon ojciec:", font=("bold", 13))
lbl_telefonojciec.grid(row=3, column=2, padx=5, pady=3, sticky=W)
ent_telefonojciec = Entry(wrapper3, textvariable=tvtelefonojciec,
                          font=("bold", 13), width="30")
ent_telefonojciec.grid(row=3, column=3, padx=5, pady=3, sticky=W)

lbl_emailojciec = Label(wrapper3, text="Email ojciec:", font=("bold", 13))
lbl_emailojciec.grid(row=4, column=2, padx=5, pady=3, sticky=W)
ent_emailojciec = Entry(wrapper3, textvariable=tvemailojciec,
                        font=("bold", 13), width="30")
ent_emailojciec.grid(row=4, column=3, padx=5, pady=3, sticky=W)

lbl_poczatekzajec = Label(wrapper3, text="Początek zajęć:", font=("bold", 13))
lbl_poczatekzajec.grid(row=5, column=2, padx=5, pady=3, sticky=W)
ent_poczatekzajec = Entry(wrapper3, textvariable=tvpoczatekzajec,
                          font=("bold", 13), width="30")
ent_poczatekzajec.grid(row=5, column=3, padx=5, pady=3, sticky=W)

lbl_konieczajec = Label(wrapper3, text="Koniec zajęć:", font=("bold", 13))
lbl_konieczajec.grid(row=6, column=2, padx=5, pady=3, sticky=W)
ent_konieczajec = Entry(wrapper3, textvariable=tvkonieczajec,
                        font=("bold", 13), width="30")
ent_konieczajec.grid(row=6, column=3, padx=5, pady=3, sticky=W)

drop = OptionMenu(wrapper3, tvgrupa, "Mądra Sówka", "Pianino",
                  "Język niemiecki", "Język angielski D",
                  "Plastyka", "Występy Cyrkowe", "Kurs8kl",
                  "Język angielski", "Klub Malucha")
drop.grid(row=7, column=3, padx=5, pady=3, sticky=W)

lbl_wiadomoscsms = Label(wrapper3, text="Wiadomość SMS:", font=("bold", 13))
lbl_wiadomoscsms.grid(row=2, column=4, padx=5, pady=3, sticky=W)
ent_wiadomoscsms = Entry(wrapper3, textvariable=tvwiadomoscsms,
                         font=("bold", 13))
ent_wiadomoscsms.grid(row=2, column=5, padx=5, pady=3, sticky=W)

add_btn = Button(wrapper3, text="Dodaj",
                 command=add_new, font=("bold", 13))
update_btn = Button(wrapper3, text="Aktualizuj",
                    command=update_customer, font=("bold", 13))
delete_btn = Button(wrapper3, text="Usuń",
                    command=delete_customer, font=("bold", 13))
sms_btn = Button(wrapper3, text="Wyślij",
                 command=sendSMS, font=("bold", 13))
clear_btn = Button(wrapper3, text="Wyczyść",
                   command=clear2, font=("bold", 13))

add_btn.grid(row=9, column=0, padx=20, pady=20)
update_btn.grid(row=9, column=1, padx=20, pady=20)
delete_btn.grid(row=9, column=2, padx=20, pady=20)
sms_btn.grid(row=3, column=4, padx=5, pady=3)
clear_btn.grid(row=3, column=5, padx=5, pady=3)

update_rows(rows)
root.title("DK Modraczek")
root.geometry("1500x800")
root.resizable(0, 0)
root.mainloop()
