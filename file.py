from PyQt5.QtWidgets import *
from collections import ChainMap
import sys
from PyQt5.uic import loadUi
from _datetime import datetime
import sqlite3
import db
import os


class LOGIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("log.ui", self)
        self.clear_btn.clicked.connect(self.cleared)
        self.login_btn.clicked.connect(self.logfcn)
        self.EXIT.clicked.connect(self.exit)
        self.adm_btn.clicked.connect(self.admfcn)
        self.sls.clicked.connect(self.lg)
        self.adm.clicked.connect(self.ad)
        self.admusername.hide()
        self.admpassword.hide()
        self.adm_btn.hide()
        self.cleared()
        self.message = QMessageBox()

    def logfcn(self):
        self.uname = self.username.text()
        self.pword = self.password.text()

        if self.uname == "" and self.pword == "":
            self.L = MAIN()
            self.L.show()
            self.hide()
            self.cleared()

            self.username.setText("")
            self.password.setText("")



        else:
            self.message.information(self, "info", "invalid login")
            self.cleared()

    def admfcn(self):
        self.admuname = self.admusername.text()
        self.admpword = self.admpassword.text()

        if self.admuname == "player" and self.admpword == "admin":
            self.L = ADMIN()
            self.L.show()
            self.hide()
            self.cleared()

            self.admusername.setText("")
            self.admpassword.setText("")



        else:
            self.message.information(self, "info", "invalid Admin login Deteails")
            self.cleared()

    def cleared(self):
        self.username.setText("")
        self.password.setText("")
        self.admusername.setText("")
        self.admpassword.setText("")

    def lg(self):
        self.admusername.hide()
        self.admpassword.hide()
        self.adm_btn.hide()
        self.username.show()
        self.password.show()
        self.login_btn.show()

    def ad(self):
        self.username.hide()
        self.password.hide()
        self.login_btn.hide()
        self.admusername.show()
        self.admpassword.show()
        self.adm_btn.show()

    def exit(self):
        self.L = LOGIN()
        self.close()


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("project.ui", self)
        self.message = QMessageBox()
        db.connect()
        # self.bill_num = random.randint(1,100)
        # self.bill.setText(str(self.bill_num))

        self.row = 0
        self.rc = 2
        self.load()
        # self.dictionary =1
        self.list = []
        self.li = []
        self.id2()

        self.loadCosmetics()
        self.loadAlcohol()
        self.loadGrocery()
        self.loadSoftDrinks()

        self.cosadd.clicked.connect(self.cosmeticsProduct)
        self.grocadd.clicked.connect(self.groceriesProduct)
        self.alcadd.clicked.connect(self.alcoholProduct)
        self.sofadd.clicked.connect(self.softdrinksProduct)
        self.delete_btn.clicked.connect(self.delfcn)
        self.reciept.clicked.connect(self.rcpt)
        self.FINAL.clicked.connect(self.TOTAL)
        self.clear.clicked.connect(self.clearfncn)
        self.logout_btn.clicked.connect(self.logout)
        self.re.clicked.connect(self.rep)

        self.quantity("0")

    def quantity(self, v):
        value = v

        self.TC.setText(v)
        self.TG.setText(v)
        self.TS.setText(v)
        self.TA.setText(v)
        self.GRAND.setText(v)

    def forTOT(self, v):
        value = v

        self.GRAND.setText(v)

    def load(self):
        self.table.setRowCount(self.rc)
        self.table.setColumnCount(4)
        # self.table.setItem(0,0,QTableWidgetItem("ID"))
        self.table.setItem(0, 0, QTableWidgetItem("NAME"))
        self.table.setItem(0, 1, QTableWidgetItem("QTY"))
        self.table.setItem(0, 2, QTableWidgetItem("RATE"))
        self.table.setItem(0, 3, QTableWidgetItem("AMOUNT"))

    def parseProduct(self, pname, pqty, prate, pamount):
        qty1 = self.cosinp.text()
        qty2 = self.grocinp.text()
        qty3 = self.alcinp.text()
        qty4 = self.sofinp.text()


        if self.row < self.table.rowCount():

            self.row += 1
            # self.table.setItem(self.row,0,QTableWidgetItem(pid))
            self.table.setItem(self.row, 0, QTableWidgetItem(pname))
            self.table.setItem(self.row, 1, QTableWidgetItem(pqty))
            self.table.setItem(self.row, 2, QTableWidgetItem(prate))
            self.table.setItem(self.row, 3, QTableWidgetItem(pamount))

            self.rc = self.table.rowCount() + 1
            self.table.setRowCount(self.rc)


        else:
            self.message.information(self,"Info","More than Row Count")


    def loadCosmetics(self):

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM cosmetics")
            record = cursor.fetchall()
            cosm = record

            for citems in cosm:
                self.cos_list.addItem(citems[1])

            con.commit()
            # self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalCosmetics(self):
        name = self.cos_list.currentText()
        # print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM cosmetics WHERE NAME= '" + name + "'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.cosinp.text())
            TCOS = T * inp
            self.C = int(self.TC.text()) + TCOS
            self.TC.setText(str(self.C))
            # print(self.TC.text())

            con.commit()
            #self.message.information(self, "Info", "Operation COSM Performed")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def loadAlcohol(self):

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM alcohol")
            record = cursor.fetchall()
            alch = record

            for aitems in alch:
                self.alc_list.addItem(aitems[1])

            con.commit()
            # self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalAlcohol(self):
        name = self.alc_list.currentText()
        # print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM alcohol WHERE NAME= '" + name + "'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.alcinp.text())
            TALC = T * inp
            self.A = int(self.TA.text()) + TALC
            self.TA.setText(str(self.A))
            # print(self.TA.text())

            con.commit()
            #self.message.information(self, "Info", "Operation ALC Performed")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def loadGrocery(self):

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM groceries")
            record = cursor.fetchall()
            groc = record

            for gitems in groc:
                self.groc_list.addItem(gitems[1])

            con.commit()
            # self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalGroceries(self):
        name = self.groc_list.currentText()
        # print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM groceries WHERE NAME= '" + name + "'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.grocinp.text())
            TGROC = T * inp
            self.G = int(self.TG.text()) + TGROC
            self.TG.setText(str(self.G))

            con.commit()
            #self.message.information(self, "Info", "Operation GROC Performed")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def loadSoftDrinks(self):

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM softdrinks")
            record = cursor.fetchall()
            sofd = record

            for sitems in sofd:
                self.sof_list.addItem(sitems[1])

            con.commit()
            # self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalSoftdrinks(self):
        name = self.sof_list.currentText()
        # print(self.sof_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM softdrinks WHERE NAME= '" + name + "'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.sofinp.text())
            TSOF = T * inp
            self.S = int(self.TS.text()) + TSOF
            self.TS.setText(str(self.S))

            con.commit()
            #self.message.information(self, "Info", "Operation SOF Performed")

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()


    def cosmeticsProduct(self):

        if self.rc <=2:
            if int(self.cosinp.text()) >= 1:

                get = self.cos_list.currentText()
                qty = self.cosinp.text()

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM cosmetics WHERE NAME='" + get + "'")
                    record = cursor.fetchall()

                    cosm = record

                    for cm in cosm:
                        total = int(cm[3]) * int(qty)
                        # print(total)
                        q = int(cm[2])
                        aq = (q - int(qty))

                        if aq > 3:
                            self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                            self.totalCosmetics()

                        elif q == 0:
                            self.message.information(self, "Info", "product exhausted already")

                        elif aq <= 3 and aq > 0:
                            self.message.information(self, "Info", "available quantity getting low")
                            self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                            self.totalCosmetics()

                        elif aq == 0:
                            self.message.information(self, "Info", "you are selling the last quantity")
                            self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                            self.totalCosmetics()


                        elif int(qty) > q and q > 1:
                            self.message.information(self, "Info", "you have lesser available product")


                        else:
                            self.message.information(self, "Info", "check available quantity")

                    con.commit()


                except Exception as e:
                    print(e)

                    con.close()
            else:
                self.message.information(self, "Info", "No Quantity Entered for Cosmetics")

        elif self.rc >2:

            get = self.cos_list.currentText()
            #print(self.rc)
            # print(self.cos_list.currentText())

            z = []
            zz = 1
            self.rc = self.table.rowCount()
            self.rcc = self.rc - 2
            #print(self.rcc)
            # monitor = (self.table.item(self.rcc, 0).text())
            for r in range(self.rcc):
                z.append((self.table.item(zz, 0).text()))
                zz += 1

            zz = 1

            #print(get)
            #print(z)


            if get in z:
                #print("get is in z")
                self.message.information(self, "Info", "Product selected already")


            elif get not in z:
                #print("get is not in z")
                if int(self.cosinp.text()) >= 1:

                    get = self.cos_list.currentText()
                    qty = self.cosinp.text()

                    try:
                        con = sqlite3.connect("./db/mini_database.db")
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM cosmetics WHERE NAME='" + get + "'")
                        record = cursor.fetchall()

                        cosm = record

                        for cm in cosm:
                            total = int(cm[3]) * int(qty)
                            # print(total)
                            q = int(cm[2])
                            aq = (q - int(qty))

                            if aq > 3:
                                self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                                self.totalCosmetics()

                            elif q == 0:
                                self.message.information(self, "Info", "product exhausted already")

                            elif aq <= 3 and aq > 0:
                                self.message.information(self, "Info", "available quantity getting low")
                                self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                                self.totalCosmetics()

                            elif aq == 0:
                                self.message.information(self, "Info", "you are selling the last quantity")
                                self.parseProduct(cm[1], qty, str(cm[3]), str(total))
                                self.totalCosmetics()


                            elif int(qty) > q and q > 1:
                                self.message.information(self, "Info", "you have lesser available product")


                            else:
                                self.message.information(self, "Info", "check available quantity")

                        con.commit()


                    except Exception as e:
                        print(e)

                        con.close()
                else:
                    self.message.information(self, "Info", "No Quantity Entered for Cosmetics")

        else:
            self.message.information(self, "Info", "RECHECK")





    def groceriesProduct(self):

        if self.rc <= 2:
            if int(self.grocinp.text()) >= 1:

                get = self.groc_list.currentText()
                qty = self.grocinp.text()

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM groceries WHERE NAME='" + get + "'")
                    record = cursor.fetchall()

                    groc = record

                    for gm in groc:
                        total = int(gm[3]) * int(qty)
                        # print(total)
                        q = int(gm[2])
                        aq = (q - int(qty))

                        if aq > 3:
                            self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                            self.totalGroceries()

                        elif q == 0:
                            self.message.information(self, "Info", "product exhausted already")

                        elif aq <= 3 and aq > 0:
                            self.message.information(self, "Info", "available quantity getting low")
                            self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                            self.totalGroceries()

                        elif aq == 0:
                            self.message.information(self, "Info", "you are selling the last quantity")
                            self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                            self.totalGroceries()


                        elif int(qty) > q and q > 1:
                            self.message.information(self, "Info", "you have lesser available product")


                        else:
                            self.message.information(self, "Info", "check available quantity")

                    con.commit()


                except Exception as e:
                    print(e)

                    con.close()
            else:
                self.message.information(self, "Info", "No Quantity Entered for Groceries")

        elif self.rc > 2:

            get = self.groc_list.currentText()
            # print(self.rc)
            # print(self.cos_list.currentText())

            z = []
            zz = 1
            self.rc = self.table.rowCount()
            self.rcc = self.rc - 2
            # print(self.rcc)
            # monitor = (self.table.item(self.rcc, 0).text())
            for r in range(self.rcc):
                z.append((self.table.item(zz, 0).text()))
                zz += 1

            zz = 1

            # print(get)
            # print(z)

            if get in z:
                # print("get is in z")
                self.message.information(self, "Info", "Product selected already")


            elif get not in z:
                # print("get is not in z")
                if int(self.grocinp.text()) >= 1:

                    get = self.groc_list.currentText()
                    qty = self.grocinp.text()

                    try:
                        con = sqlite3.connect("./db/mini_database.db")
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM groceries WHERE NAME='" + get + "'")
                        record = cursor.fetchall()

                        groc = record

                        for gm in groc:
                            total = int(gm[3]) * int(qty)
                            # print(total)
                            q = int(gm[2])
                            aq = (q - int(qty))

                            if aq > 3:
                                self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                                self.totalGroceries()

                            elif q == 0:
                                self.message.information(self, "Info", "product exhausted already")

                            elif aq <= 3 and aq > 0:
                                self.message.information(self, "Info", "available quantity getting low")
                                self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                                self.totalGroceries()

                            elif aq == 0:
                                self.message.information(self, "Info", "you are selling the last quantity")
                                self.parseProduct(gm[1], qty, str(gm[3]), str(total))
                                self.totalGroceries()


                            elif int(qty) > q and q > 1:
                                self.message.information(self, "Info", "you have lesser available product")


                            else:
                                self.message.information(self, "Info", "check available quantity")

                        con.commit()


                    except Exception as e:
                        print(e)

                        con.close()
                else:
                    self.message.information(self, "Info", "No Quantity Entered for Groceries")

        else:
            self.message.information(self, "Info", "RECHECK")



    def alcoholProduct(self):

        if self.rc <= 2:
            if int(self.alcinp.text()) >= 1:

                get = self.alc_list.currentText()
                qty = self.alcinp.text()

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM alcohol WHERE NAME='" + get + "'")
                    record = cursor.fetchall()

                    alc = record

                    for ac in alc:
                        total = int(ac[3]) * int(qty)
                        # print(total)
                        q = int(ac[2])
                        aq = (q - int(qty))

                        if aq > 3:
                            self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                            self.totalAlcohol()

                        elif q == 0:
                            self.message.information(self, "Info", "product exhausted already")

                        elif aq <= 3 and aq > 0:
                            self.message.information(self, "Info", "available quantity getting low")
                            self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                            self.totalAlcohol()

                        elif aq == 0:
                            self.message.information(self, "Info", "you are selling the last quantity")
                            self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                            self.totalAlcohol()


                        elif int(qty) > q and q > 1:
                            self.message.information(self, "Info", "you have lesser available product")


                        else:
                            self.message.information(self, "Info", "check available quantity")

                    con.commit()


                except Exception as e:
                    print(e)

                    con.close()
            else:
                self.message.information(self, "Info", "No Quantity Entered for Alcohol")

        elif self.rc > 2:

            get = self.alc_list.currentText()
            # print(self.rc)
            # print(self.cos_list.currentText())

            z = []
            zz = 1
            self.rc = self.table.rowCount()
            self.rcc = self.rc - 2
            # print(self.rcc)
            # monitor = (self.table.item(self.rcc, 0).text())
            for r in range(self.rcc):
                z.append((self.table.item(zz, 0).text()))
                zz += 1

            zz = 1

            # print(get)
            # print(z)

            if get in z:
                # print("get is in z")
                self.message.information(self, "Info", "Product selected already")


            elif get not in z:
                # print("get is not in z")
                if int(self.alcinp.text()) >= 1:

                    get = self.alc_list.currentText()
                    qty = self.alcinp.text()

                    try:
                        con = sqlite3.connect("./db/mini_database.db")
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM alcohol WHERE NAME='" + get + "'")
                        record = cursor.fetchall()

                        alc = record

                        for ac in alc:
                            total = int(ac[3]) * int(qty)
                            # print(total)
                            q = int(ac[2])
                            aq = (q - int(qty))

                            if aq > 3:
                                self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                                self.totalAlcohol()

                            elif q == 0:
                                self.message.information(self, "Info", "product exhausted already")

                            elif aq <= 3 and aq > 0:
                                self.message.information(self, "Info", "available quantity getting low")
                                self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                                self.totalAlcohol()

                            elif aq == 0:
                                self.message.information(self, "Info", "you are selling the last quantity")
                                self.parseProduct(ac[1], qty, str(ac[3]), str(total))
                                self.totalAlcohol()


                            elif int(qty) > q and q > 1:
                                self.message.information(self, "Info", "you have lesser available product")


                            else:
                                self.message.information(self, "Info", "check available quantity")

                        con.commit()


                    except Exception as e:
                        print(e)

                        con.close()
                else:
                    self.message.information(self, "Info", "No Quantity Entered for Alcohol")

        else:
            self.message.information(self, "Info", "RECHECK")


    def softdrinksProduct(self):
        if self.rc <= 2:
            if int(self.sofinp.text()) >= 1:

                get = self.sof_list.currentText()
                qty = self.sofinp.text()

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM softdrinks WHERE NAME='" + get + "'")
                    record = cursor.fetchall()

                    sof = record

                    for sf in sof:
                        total = int(sf[3]) * int(qty)
                        # print(total)
                        q = int(sf[2])
                        aq = (q - int(qty))

                        if aq > 3:
                            self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                            self.totalSoftdrinks()

                        elif q == 0:
                            self.message.information(self, "Info", "product exhausted already")

                        elif aq <= 3 and aq > 0:
                            self.message.information(self, "Info", "available quantity getting low")
                            self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                            self.totalSoftdrinks()

                        elif aq == 0:
                            self.message.information(self, "Info", "you are selling the last quantity")
                            self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                            self.totalSoftdrinks()



                        elif int(qty) > q and q > 1:
                            self.message.information(self, "Info", "you have lesser available product")


                        else:
                            self.message.information(self, "Info", "check available quantity")

                    con.commit()


                except Exception as e:
                    print(e)

                    con.close()
            else:
                self.message.information(self, "Info", "No Quantity Entered for SoftDrinks")

        elif self.rc > 2:

            get = self.sof_list.currentText()
            # print(self.rc)
            # print(self.cos_list.currentText())

            z = []
            zz = 1
            self.rc = self.table.rowCount()
            self.rcc = self.rc - 2
            # print(self.rcc)
            # monitor = (self.table.item(self.rcc, 0).text())
            for r in range(self.rcc):
                z.append((self.table.item(zz, 0).text()))
                zz += 1

            zz = 1

            # print(get)
            # print(z)

            if get in z:
                # print("get is in z")
                self.message.information(self, "Info", "Product selected already")


            elif get not in z:
                # print("get is not in z")
                if int(self.sofinp.text()) >= 1:

                    get = self.sof_list.currentText()
                    qty = self.sofinp.text()

                    try:
                        con = sqlite3.connect("./db/mini_database.db")
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM softdrinks WHERE NAME='" + get + "'")
                        record = cursor.fetchall()

                        sof = record

                        for sf in sof:
                            total = int(sf[3]) * int(qty)
                            # print(total)
                            q = int(sf[2])
                            aq = (q - int(qty))

                            if aq > 3:
                                self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                                self.totalSoftdrinks()

                            elif q == 0:
                                self.message.information(self, "Info", "product exhausted already")

                            elif aq <= 3 and aq > 0:
                                self.message.information(self, "Info", "available quantity getting low")
                                self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                                self.totalSoftdrinks()

                            elif aq == 0:
                                self.message.information(self, "Info", "you are selling the last quantity")
                                self.parseProduct(sf[1], qty, str(sf[3]), str(total))
                                self.totalSoftdrinks()


                            elif int(qty) > q and q > 1:
                                self.message.information(self, "Info", "you have lesser available product")


                            else:
                                self.message.information(self, "Info", "check available quantity")

                        con.commit()


                    except Exception as e:
                        print(e)

                        con.close()
                else:
                    self.message.information(self, "Info", "No Quantity Entered for Softdrinks")

        else:
            self.message.information(self, "Info", "RECHECK")




    def TOTAL(self):
        self.forTOT("0")
        self.GG = int(self.TC.text()) + int(self.TA.text()) + int(self.TG.text()) + int(self.TS.text())
        self.GRAND.setText(str(int(self.GRAND.text()) + self.GG))

    def clearfncn(self):

        self.row = 0
        self.cosinp.setValue(0)
        self.alcinp.setValue(0)
        self.sofinp.setValue(0)
        self.grocinp.setValue(0)
        self.TA.setText("0")
        self.TC.setText("0")
        self.name.setText("")
        self.phone.setText("")
        self.TS.setText("0")
        self.TG.setText("0")
        self.forTOT("0")
        self.rc = 2
        self.li = []
        self.list = []
        self.table.clear()
        self.load()

    def rcpt(self):
        self.storage()
        self.print()
        self.id()
        self.message.information(self, "Info", "Sales Made and Recorded also Reciept Ready")
        self.clearfncn()


    def print(self):

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(r"c:\Users\personal\Documents\COMPLETED PROJECTS\BILLING SOFTWARE\print\p.txt", "w") as f:
            f.write("\t__________________ Corler store ______________\n\n")
            f.write("\t Address:    11,kingston Road, Ikeja, Lagos\n\n")
            f.write("\t Phone:    08085872783 \n\n\n")
            f.write("\t___________________ Invoice ___________________\n\n")
            f.write("\t" + "Customer-NAME :     " + self.name.text() + "\n\n")
            f.write("\t" + "Bill-Number :     " + self.bill.text() + "\n\n")
            f.write("\t" + "DATE/TIME :   " + dt_string + "\n\n")
            f.write("\t_____________________________________________\n\n")
            r = self.table.rowCount()
            c = self.table.columnCount()
            r -= 1

            for rr in range(1, r):
                for cc in range(1):
                    f.write("\t" + self.table.item(rr, 0).text() + "\n")
                    f.write("\t" + self.table.item(rr, 1).text() + "   ")
                    f.write("  " + " X " + "  ")
                    f.write(self.table.item(rr, 2).text())
                    f.write("  " + " == " + "  ")
                    f.write(self.table.item(rr, 3).text() + "\n")
                    f.write("\t___________________\n")

                f.write("\n")
            f.write("\t___________________________________________\n\n")
            f.write("\t\t\tTOTAL-----  #" + self.GRAND.text() + "\n\n")
            f.write("\t______ Thank you for your patronage__________\n\n")
            i = self.bill.text()


        f = open(r"c:\Users\personal\Documents\COMPLETED PROJECTS\BILLING SOFTWARE\print\p.txt", "r")
        if f.mode == 'r':
            content = f.read()



        db.RePrint(i, content)

        os.startfile(r"c:\Users\personal\Documents\COMPLETED PROJECTS\BILLING SOFTWARE\print\p.txt")


    def rep(self):
        if self.reprintid.text() == "":
            self.message.information(self, "Info", "input Product ID")

        else:
            idd = int(self.reprintid.text())
            iddd = str(idd)

            try:
                con = sqlite3.connect("./db/mini_database.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM reprint WHERE ID='" + iddd + "'")
                record = cursor.fetchall()
                repr = record

                rl = []
                for r in repr:
                    rl.append(r[0])

                if idd in rl:
                    try:
                        con = sqlite3.connect("./db/mini_database.db")
                        cursor = con.cursor()
                        cursor.execute("SELECT * FROM reprint WHERE ID='" + iddd + "'")
                        record = cursor.fetchall()
                        re = record
                        for r in record:
                            rec = r[1]

                        with open(r"c:\Users\personal\Desktop\zoom teach\print/p.txt", "w") as p:
                            p.write(rec)
                            # rec

                        con.commit()

                        os.startfile(r"c:\Users\personal\Desktop\zoom teach\print/p.txt")
                        self.message.information(self, "Info", "Reprint ready")


                    except Exception as e:
                        self.message.information(self, "Error", e)

                elif self.reprintid.text() == "":
                    self.message.information(self, "Info", "input Product ID")

                else:
                    self.message.information(self, "Info", "Invalid Reciept ID")

                con.commit()


            except Exception as e:

                self.message.information(self, "Error", e)



    def delfcn(self):

        if self.table.rowCount() > 2:
            try:

                var = self.table.currentRow()
                self.table.item(var, 3).text()

                self.nme = self.table.item(var, 0).text()
                #################################################################1

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM cosmetics")
                    record = cursor.fetchall()
                    cosm = record

                    u1 = []

                    for citems in cosm:
                        u1.append(citems[1])

                    if self.nme in u1:
                        self.C -= int(self.table.item(var, 3).text())
                        self.TC.setText(str(self.C))


                    else:
                        pass

                    con.commit()
                    # self.message.information(self,"Info","successfully Loaded")


                except Exception as e:
                    # self.message.information(self,"Error",e)
                    print(e)
                #################################################################2
                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM groceries")
                    record = cursor.fetchall()
                    groc = record

                    u2 = []

                    for gitems in groc:
                        u2.append(gitems[1])

                    if self.nme in u2:
                        self.G -= int(self.table.item(var, 3).text())
                        self.TG.setText(str(self.G))


                    else:
                        print("NOT HERE!!")
                        pass

                    con.commit()
                    # self.message.information(self,"Info","successfully Loaded")


                except Exception as e:
                    # self.message.information(self,"Error",e)
                    print(e)

                #################################################3

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM alcohol")
                    record = cursor.fetchall()
                    alc = record

                    u3 = []

                    for aitems in alc:
                        u3.append(aitems[1])

                    if self.nme in u3:
                        self.A -= int(self.table.item(var, 3).text())
                        self.TA.setText(str(self.A))


                    else:
                        pass

                    con.commit()
                    # self.message.information(self,"Info","successfully Loaded")

                except Exception as e:
                    # self.message.information(self,"Error",e)
                    print(e)

                ###################################################4

                try:
                    con = sqlite3.connect("./db/mini_database.db")
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM softdrinks")
                    record = cursor.fetchall()
                    sod = record

                    u4 = []

                    for sitems in sod:
                        u4.append(sitems[1])

                    if self.nme in u4:
                        self.S -= int(self.table.item(var, 3).text())
                        self.TS.setText(str(self.S))


                    else:
                        pass

                    con.commit()
                    # self.message.information(self,"Info","successfully Loaded")


                except Exception as e:
                    # self.message.information(self,"Error",e)
                    print(e)

                self.table.removeRow(var)
                self.row -= 1
                con.close()


            except:
                self.message.information(self, "Info", "product to be deleted not selected")



        else:
            self.message.information(self, "Info", "You Can't Clear The Whole Table!!!")
        self.forTOT("0")



    def id(self):
        self.bill.setText("")
        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM ID")
            record = cursor.fetchall()

            for i in record:
                num = i[0]
                number = i[1]

            number += 1

            con.commit()


        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()

            cursor.execute("UPDATE ID  SET ID_NUM ='" + str(number) + "' WHERE SN = '" + str(num) + "'")

            con.commit()

        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM ID")
            record = cursor.fetchall()

            for i in record:
                num = i[0]
                number = i[1]

            self.bill.setText(str(number))

            con.commit()


        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def id2(self):
        self.bill.setText("")
        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM ID")
            record = cursor.fetchall()

            for i in record:
                num = i[0]
                number = i[1]

            self.bill.setText(str(number))

            con.commit()


        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()

    def storage(self):

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        sid = self.bill.text()
        sdate = dt_string
        sname = self.name.text()
        sphone = self.phone.text()
        stotal = self.GRAND.text()
        a = []
        b = []
        C = []
        d = []

        r = self.table.rowCount()
        c = self.table.columnCount()
        self.unit = 0
        ut = 1
        utt = 1
        r -= 1

        for rr in range(1, r):
            self.rqn = (self.table.item(rr, 0).text())
            self.rq = (self.table.item(rr, 1).text())


            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM cosmetics")
                row = cur.fetchall()

                for r in row:
                    a.append(r[1])

                # print(a)
                # print(self.rqn)
                if self.rqn in a:
                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "SELECT * FROM cosmetics WHERE NAME='" + self.rqn + "'")
                        row = cur.fetchall()
                        for r in row:
                            Q = int(r[2])

                        NQ = Q - int(self.rq)

                        con.commit()
                        # self.message.information(self, "info", "new quantity gotten")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()

                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "UPDATE cosmetics SET  QTY ='" + str(NQ) + "' WHERE NAME ='" + self.rqn + "'")

                        con.commit()
                        # self.message.information(self, "info", "updated")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()


                else:
                    pass
                    # self.message.information(self, "info", "NOT IN COSMETICS")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            try:

                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM groceries")
                row = cur.fetchall()

                for r in row:
                    b.append(r[1])

                # print(b)
                # print(self.rqn)
                if self.rqn in b:
                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "SELECT * FROM groceries WHERE NAME='" + self.rqn + "'")
                        row = cur.fetchall()
                        for r in row:
                            Q = int(r[2])

                        NQ = Q - int(self.rq)

                        con.commit()
                        # self.message.information(self, "info", "new quantity gotten")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()

                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "UPDATE groceries SET  QTY ='" + str(NQ) + "' WHERE NAME ='" + self.rqn + "'")

                        con.commit()
                        # self.message.information(self, "info", "updated")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()


                else:
                    pass
                    # self.message.information(self, "info", "NOT IN GROCERIES")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM alcohol")
                row = cur.fetchall()

                for r in row:
                    C.append(r[1])

                # print(C)
                # print(self.rqn)
                if self.rqn in C:
                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "SELECT * FROM alcohol WHERE NAME='" + self.rqn + "'")
                        row = cur.fetchall()
                        for r in row:
                            Q = int(r[2])

                        NQ = Q - int(self.rq)

                        con.commit()
                        # self.message.information(self, "info", "new quantity gotten")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()

                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "UPDATE alcohol SET  QTY ='" + str(NQ) + "' WHERE NAME ='" + self.rqn + "'")

                        con.commit()
                        # self.message.information(self, "info", "updated")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()


                else:
                    pass
                    # self.message.information(self, "info", "NOT IN ALCOHOL")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM softdrinks")
                row = cur.fetchall()

                for r in row:
                    d.append(r[1])


                if self.rqn in d:
                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "SELECT * FROM softdrinks WHERE NAME='" + self.rqn + "'")
                        row = cur.fetchall()
                        for r in row:
                            Q = int(r[2])

                        NQ = Q - int(self.rq)

                        con.commit()
                        # self.message.information(self, "info", "new quantity gotten")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()

                    try:
                        con = sqlite3.connect("db/mini_database.db")
                        cur = con.cursor()

                        cur.execute(
                            "UPDATE softdrinks SET  QTY ='" + str(NQ) + "' WHERE NAME ='" + self.rqn + "'")

                        con.commit()
                        # self.message.information(self, "info", "updated")

                    except Exception as e:
                        self.message.information(self, "Error", e)

                    # con.close()


                else:
                    pass
                    # self.message.information(self, "info", "NOT IN SOFTDRINKS")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()
            self.a = []
            self.b = []
            self.cc = []
            self.d = []

            for cc in range(c):
                l = (self.table.item(rr, cc).text())
                self.li.append(l)

        self.list.append(self.li)
        # print(str(self.uniting))

        sproducts = str(self.list)

        db.insertRecord(sid, sdate, sname, sphone, stotal, sproducts)

        self.li.clear()
        self.list.clear()
        self.rq = []
        self.rqn = []
        self.a = []
        self.b = []
        self.cc = []
        self.d = []

    def logout(self):
        self.L = LOGIN()
        self.L.show()
        self.hide()


class ADMIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("admin.ui", self)
        self.message = QMessageBox()
        self.checking.hide()
        self.updt.hide()
        self.delete_btn.hide()
        self.logout.clicked.connect(self.logoutfcn)
        self.message = QMessageBox()
        # self.registration.setStyleSheet("color:white;background:black")
        db.connect()

        self.fields()
        self.rowcheck = 1
        self.newcos.clicked.connect(self.insert1)
        self.newgroc.clicked.connect(self.insert2)
        self.newsod.clicked.connect(self.insert3)
        self.newalc.clicked.connect(self.insert4)
        self.checking.clicked.connect(self.searchRecord)
        self.registration.clicked.connect(self.regis)
        # self.search.clicked.connect(self.sch)
        self.clear_btn.clicked.connect(self.clear)
        self.update.clicked.connect(self.updateRecord)
        self.showall.clicked.connect(self.all)
        self.delete_2.clicked.connect(self.delt)
        self.updt.clicked.connect(self.updatefcn)
        self.sale.clicked.connect(self.sales)
        # self.check2.clicked.connect(self.checkupdt)
        self.delete_btn.clicked.connect(self.deletefcn)
        self.checker.hide()

        self.display.setColumnWidth(0, 300)
        self.display.setColumnWidth(1, 200)
        self.display.setColumnWidth(2, 200)
        self.display.setColumnWidth(3, 100)
        self.display.setColumnWidth(4, 150)
        self.display.setColumnWidth(5, 300)

    def insert1(self):
        id = self.ID.text()
        name = self.NAME.text()
        qty = self.QTY.text()
        rate = self.RATE.text()


        db.adminInsert1(id, name, qty, rate)
        # data = [reg, fname, lname, gender, dob, course]
        # self.fields()

        self.message.information(self, "info", "Record Added")

    def insert2(self):
        id = self.ID.text()
        name = self.NAME.text()
        qty = self.QTY.text()
        rate = self.RATE.text()

        db.adminInsert2(id, name, qty, rate)
        # data = [reg, fname, lname, gender, dob, course]
        # self.fields()

        self.message.information(self, "info", "Record Added")

    def insert3(self):
        id = self.ID.text()
        name = self.NAME.text()
        qty = self.QTY.text()
        rate = self.RATE.text()

        db.adminInsert3(id, name, qty, rate)
        # data = [reg, fname, lname, gender, dob, course]
        # self.fields()

        self.message.information(self, "info", "Record Added")

    def insert4(self):
        id = self.ID.text()
        name = self.NAME.text()
        qty = self.QTY.text()
        rate = self.RATE.text()

        db.adminInsert4(id, name, qty, rate)
        # data = [reg, fname, lname, gender, dob, course]
        # self.fields()

        self.message.information(self, "info", "Record Added")

    def sch(self):
        # self.search.setStyleSheet("color:white;background:black")
        self.add.hide()
        self.check.show()
        self.updt.hide()
        self.regno.setText("")
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.display.clear()
        self.search.setStyleSheet("color:white;background:black")
        self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        self.update.setStyleSheet("background: rgb(68, 45, 34);")
        self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        self.firstname.setText("")
        self.lastname.setText("")
        self.gender.setText("")
        self.dob.setText("")
        self.course.setText("")
        self.regno.setText("")
        self.fields()
        self.check2.hide()
        self.delete_btn.hide()

    def regis(self):
        self.newcos.show()
        self.checker.hide()
        self.newgroc.show()
        self.newsod.show()
        self.newalc.show()
        self.display.clear()
        self.updt.hide()
        self.delete_btn.hide()
        # self.registration.setStyleSheet("color:white;background:black")
        # self.update.setStyleSheet("background: rgb(68, 45, 34);")
        # self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        # self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        # self.search.setStyleSheet("background: rgb(68, 45, 34);")
        # self.check2.hide()
        self.ID.setText("")
        self.NAME.setText("")
        self.QTY.setText("")
        self.RATE.setText("")
        self.display.clear()
        self.fields()

    def all(self):
        self.newcos.hide()
        self.newgroc.hide()
        self.newsod.hide()
        self.newalc.hide()
        self.checker.hide()
        self.display.clear()
        self.updt.hide()
        # self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        # self.showall.setStyleSheet("color:white;background:black")
        # self.update.setStyleSheet("background: rgb(68, 45, 34);")
        # self.delete_2.setStyleSheet("background: rgb(68, 45, 34);")
        # self.search.setStyleSheet("background: rgb(68, 45, 34);")
        self.fields()
        self.ID.setText("")
        self.NAME.setText("")
        self.QTY.setText("")
        self.RATE.setText("")
        self.delete_btn.hide()

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM cosmetics WHERE 1 ORDER BY ID Asc")
            row = cur.fetchall()

            # checking = len(row)
            # print(checking)

            self.display.setRowCount(self.track + 1)
            self.display.setColumnCount(4)

            for r in row:
                self.display.setItem(self.rowcheck, 0, QTableWidgetItem(r[0]))
                self.display.setItem(self.rowcheck, 1, QTableWidgetItem(r[1]))
                self.display.setItem(self.rowcheck, 2, QTableWidgetItem(str(r[2])))
                self.display.setItem(self.rowcheck, 3, QTableWidgetItem(str(r[3])))
                self.rowcheck += 1

            # self.rowcheck = 1

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        con.close()

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM groceries WHERE 1 ORDER BY ID Asc")
            row = cur.fetchall()

            # checking = len(row)
            # print(checking)

            # self.display.setRowCount( self.track + 1)
            # self.display.setColumnCount(4)

            for r in row:
                self.display.setItem(self.rowcheck, 0, QTableWidgetItem(r[0]))
                self.display.setItem(self.rowcheck, 1, QTableWidgetItem(r[1]))
                self.display.setItem(self.rowcheck, 2, QTableWidgetItem(str(r[2])))
                self.display.setItem(self.rowcheck, 3, QTableWidgetItem(str(r[3])))
                self.rowcheck += 1

            # self.rowcheck = 1

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        con.close()

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM softdrinks WHERE 1 ORDER BY ID Asc")
            row = cur.fetchall()

            # checking = len(row)
            # print(checking)

            # self.display.setRowCount( self.track + 1)
            # self.display.setColumnCount(4)

            for r in row:
                self.display.setItem(self.rowcheck, 0, QTableWidgetItem(r[0]))
                self.display.setItem(self.rowcheck, 1, QTableWidgetItem(r[1]))
                self.display.setItem(self.rowcheck, 2, QTableWidgetItem(str(r[2])))
                self.display.setItem(self.rowcheck, 3, QTableWidgetItem(str(r[3])))
                self.rowcheck += 1

            # self.rowcheck = 1

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        con.close()

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM alcohol WHERE 1 ORDER BY ID Asc")
            row = cur.fetchall()

            # checking = len(row)
            # print(checking)

            # self.display.setRowCount( self.track + 1)
            # self.display.setColumnCount(4)

            for r in row:
                self.display.setItem(self.rowcheck, 0, QTableWidgetItem(r[0]))
                self.display.setItem(self.rowcheck, 1, QTableWidgetItem(r[1]))
                self.display.setItem(self.rowcheck, 2, QTableWidgetItem(str(r[2])))
                self.display.setItem(self.rowcheck, 3, QTableWidgetItem(str(r[3])))
                self.rowcheck += 1

            self.rowcheck = 1
            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        con.close()

    def sales(self):
        self.display.clear()
        self.newcos.hide()
        self.newgroc.hide()
        self.newsod.hide()
        self.newalc.hide()
        self.checker.hide()
        self.updt.hide()
        self.ID.setText("")
        self.NAME.setText("")
        self.QTY.setText("")
        self.RATE.setText("")
        self.delete_btn.hide()

        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM store")
            row = cur.fetchall()

            store = len(row)
            store += 1
            stored = 1
            # print(checking)

            self.display.setRowCount(store)
            self.display.setColumnCount(6)

            self.display.setItem(0, 0, QTableWidgetItem("ID"))
            self.display.setItem(0, 1, QTableWidgetItem("DATE/TIME"))
            self.display.setItem(0, 2, QTableWidgetItem("NAME"))
            self.display.setItem(0, 3, QTableWidgetItem("PHONE"))
            self.display.setItem(0, 4, QTableWidgetItem("TOTAL"))
            self.display.setItem(0, 5, QTableWidgetItem("PRODUCT"))

            for r in row:
                self.display.setItem(stored, 0, QTableWidgetItem(str(r[0])))
                self.display.setItem(stored, 1, QTableWidgetItem(r[1]))
                self.display.setItem(stored, 2, QTableWidgetItem(r[2]))
                self.display.setItem(stored, 3, QTableWidgetItem(str(r[3])))
                self.display.setItem(stored, 4, QTableWidgetItem(str(r[4])))
                self.display.setItem(stored, 5, QTableWidgetItem(r[5]))
                stored += 1

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)
        con.close()

    def searchRecord(self):
        self.na = []
        self.nb = []
        self.nc = []
        self.nd = []
        reg = self.reg.text()

        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM cosmetics ")
            row = cur.fetchall()

            for r in row:
                self.na.append(r[1])

            con.commit()

        except Exception as e:
            pass
            #print("cosmetics not selected")

        con.close()

        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM groceries")
            row = cur.fetchall()

            for r in row:
                self.nb.append(r[1])

            con.commit()

        except Exception as e:
            pass
            #print("groceries not selected")

        con.close()

        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM softdrinks")
            row = cur.fetchall()

            for r in row:
                self.nc.append(r[1])

            con.commit()

        except Exception as e:
            pass
            #print("softdrinks not selected")

        con.close()

        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM alcohol")
            row = cur.fetchall()

            for r in row:
                self.nd.append(r[1])

            con.commit()

        except Exception as e:
            pass
            #print("alcohol not selected")

        con.close()
        #print(self.na)
        #print(self.nb)
        #print(self.nc)
        #print(self.nd)

        if reg in self.na:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM cosmetics WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    #print("we in first")
                    self.NAME.setText(r[1])
                    self.QTY.setText(str(r[2]))
                    self.RATE.setText(str(r[3]))

                self.message.information(self, "info", "succesfully searched")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nb:
            #print("we in second")
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute("SELECT * FROM groceries WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.NAME.setText(r[1])
                    self.QTY.setText(str(r[2]))
                    self.RATE.setText(str(r[3]))

                    self.message.information(self, "info", "succesfully searched")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nc:
            #print("we in third")
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute("SELECT * FROM softdrinks WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.NAME.setText(r[1])
                    self.QTY.setText(str(r[2]))
                    self.RATE.setText(str(r[3]))

                    self.message.information(self, "info", "succesfully searched")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nd:
            #print("we in fourth")
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute("SELECT * FROM alcohol WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    #print("we here")
                    self.NAME.setText(r[1])
                    self.QTY.setText(str(r[2]))
                    self.RATE.setText(str(r[3]))

                    self.message.information(self, "info", "succesfully searched")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        else:
            self.message.information(self, "info", "oops!! search unsuccessfull")
            self.clear()
            self.fields()

    def updateRecord(self):
        # self.update.setStyleSheet("color:white;background:black")
        self.updt.show()
        self.newcos.hide()
        self.newgroc.hide()
        self.newsod.hide()
        self.newalc.hide()
        self.checker.show()
        self.checking.show()
        # self.update.setStyleSheet("color:white;background:black")
        # self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        # self.delete_2.setStyleSheet("background-color: rgb(68, 45, 34);")
        # self.search.setStyleSheet("background-color: rgb(68, 45, 34);")
        # self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        # self.check2.show()
        self.display.clear()
        self.clear()
        self.fields()
        self.delete_btn.hide()

    def clear(self):
        self.ID.setText("")
        self.reg.setText("")
        self.NAME.setText("")
        self.RATE.setText("")
        self.QTY.setText("")
        self.display.clear()

    def delt(self):
        # self.delete_2.setStyleSheet("color:white;background:black")
        # self.update.setStyleSheet("background: rgb(68, 45, 34);")
        # self.registration.setStyleSheet("background: rgb(68, 45, 34);")
        # self.showall.setStyleSheet("background: rgb(68, 45, 34);")
        # self.search.setStyleSheet("background: rgb(68, 45, 34);")
        # self.delete_btn.show()
        self.updt.hide()
        self.newcos.hide()
        self.newgroc.hide()
        self.newsod.hide()
        self.newalc.hide()
        self.checker.show()
        self.delete_btn.show()
        self.checking.show()
        self.display.clear()
        self.fields()

    def fields(self):

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM cosmetics")
            row = cur.fetchall()

            checking1 = len(row)

            # print(checking1)

            # self.display.setRowCount(checking + 1)
            # self.display.setColumnCount(6)

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM groceries")
            row = cur.fetchall()

            checking2 = len(row)
            # print(checking2)

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM softdrinks")
            row = cur.fetchall()

            checking3 = len(row)
            # print(checking3)

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

        try:
            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM alcohol")
            row = cur.fetchall()

            checking4 = len(row)
            #print(checking4)
            self.track = checking1 + checking2 + checking3 + checking4
            # print(self.track)
            self.display.setRowCount(self.track + 1)
            self.display.setColumnCount(4)

            self.display.setItem(0, 0, QTableWidgetItem("Reg No"))
            self.display.setItem(0, 1, QTableWidgetItem("NAME"))
            self.display.setItem(0, 2, QTableWidgetItem("QTY"))
            self.display.setItem(0, 3, QTableWidgetItem("RATE"))

            con.commit()

        except Exception as e:
            self.message.information(self, "Error", e)

    def checkupdt(self):
        reg = self.reg.text()
        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM cosmetics WHERE ID = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.ID.setText(r[0])
                self.NAME.setText(r[1])
                self.RATE.setText(r[3])


            con.commit()

        except Exception as e:
            pass


        try:

            con = sqlite3.connect("db/mini_database.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM groceries WHERE ID = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.ID.setText(r[0])
                self.NAME.setText(r[1])
                self.RATE.setText(r[3])


            con.commit()

        except Exception as e:
            pass
            #print("Not here")

        try:

            con = sqlite3.connect("db/mini_database.db.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM softdrinks WHERE ID = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.ID.setText(r[0])
                self.NAME.setText(r[1])
                self.RATE.setText(r[3])


            con.commit()

        except Exception as e:
            pass
            #print("Not here")

        try:

            con = sqlite3.connect("db/mini_database.db.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM alcohol WHERE ID = '" + reg + "'")
            row = cur.fetchall()

            for r in row:
                self.ID.setText(r[0])
                self.NAME.setText(r[1])
                self.RATE.setText(r[3])

            con.commit()

        except Exception as e:
            pass
            #print("Not here")

    def updatefcn(self):
        reg = self.reg.text()
        # sid = self.ID.text()
        sname = self.NAME.text()
        sqty = self.QTY.text()
        srate = self.RATE.text()

        self.display.clear()
        self.fields()

        if reg in self.na:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM cosmetics WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    ua = int(r[2])

                fua = str(ua + int(sqty))

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE cosmetics SET  NAME ='" + sname + "',QTY ='" + fua + "',RATE ='" + srate + "' WHERE NAME ='" + reg + "'")

                self.message.information(self, "info", "Successfully Updated")

                con.commit()


            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM cosmetics WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                    self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                    self.display.setItem(1, 2, QTableWidgetItem(str(r[2])))
                    self.display.setItem(1, 3, QTableWidgetItem(str(r[3])))

                self.message.information(self, "info", "succesfully loaded")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nb:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM groceries WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    ub = int(r[2])

                fub = str(ub + int(sqty))


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE groceries SET  NAME ='" + sname + "',QTY ='" + fub + "',RATE ='" + srate + "' WHERE NAME ='" + reg + "'")

                self.message.information(self, "info", "Successfully Updated")

                con.commit()


            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM groceries WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                    self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                    self.display.setItem(1, 2, QTableWidgetItem(str(r[2])))
                    self.display.setItem(1, 3, QTableWidgetItem(str(r[3])))

                self.message.information(self, "info", "succesfully loaded")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nc:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM softdrinks WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    uc = int(r[2])

                fuc = str(uc + int(sqty))


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE softdrinks SET  NAME ='" + sname + "',QTY ='" + fuc + "',RATE ='" + srate + "' WHERE NAME ='" + reg + "'")

                self.message.information(self, "info", "Successfully Updated")

                con.commit()


            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM softdrinks WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                    self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                    self.display.setItem(1, 2, QTableWidgetItem(str(r[2])))
                    self.display.setItem(1, 3, QTableWidgetItem(str(r[3])))

                self.message.information(self, "info", "succesfully loaded")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nd:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM alcohol WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    ud = int(r[2])

                fud = str(ud + int(sqty))


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE alcohol SET  NAME ='" + sname + "',QTY ='" + fud + "',RATE ='" + srate + "' WHERE NAME ='" + reg + "'")

                self.message.information(self, "info", "Successfully Updated")

                con.commit()


            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()

                cur.execute(
                    "SELECT * FROM alcohol WHERE NAME = '" + reg + "'")
                row = cur.fetchall()

                for r in row:
                    self.display.setItem(1, 0, QTableWidgetItem(r[0]))
                    self.display.setItem(1, 1, QTableWidgetItem(r[1]))
                    self.display.setItem(1, 2, QTableWidgetItem(str(r[2])))
                    self.display.setItem(1, 3, QTableWidgetItem(str(r[3])))

                self.message.information(self, "info", "succesfully loaded")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()




        else:
            self.message.information(self, "info", "Product not found")

    def deletefcn(self):
        reg = self.reg.text()

        if reg in self.na:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute("DELETE FROM cosmetics WHERE NAME = '" + reg + "'")
                self.message.information(self, "info", "Record Deleted")


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nb:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute("DELETE FROM groceries WHERE NAME = '" + reg + "'")
                self.message.information(self, "info", "Record Deleted")


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nc:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute("DELETE FROM softdrinks WHERE NAME = '" + reg + "'")
                self.message.information(self, "info", "Record Deleted")
                print("deleted")

                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        elif reg in self.nd:
            try:
                con = sqlite3.connect("db/mini_database.db")
                cur = con.cursor()
                cur.execute("DELETE FROM alcohol WHERE NAME = '" + reg + "'")
                self.message.information(self, "info", "Record Deleted")


                con.commit()

            except Exception as e:
                self.message.information(self, "Error", e)

            con.close()

        else:
            self.message.information(self, "info", "Record Not Deleted")

        self.clear()
        self.fields()

    def logoutfcn(self):
        self.L = LOGIN()
        self.L.show()
        self.hide()


app = QApplication(sys.argv)
L = LOGIN()
L.show()

app.exec_()
app.exit()
