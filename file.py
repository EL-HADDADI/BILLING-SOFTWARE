
from PyQt5.QtWidgets import *
from collections import ChainMap
import sys
from PyQt5.uic import loadUi
import sqlite3
import db

class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("project.ui",self)
        self.message = QMessageBox()
        db.connect()
        #self.bill_num = random.randint(1,100)
        #self.bill.setText(str(self.bill_num))

        self.row = 0
        self.rc = 2
        self.load()
        #self.dictionary =1
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

        self.quantity("0")
        

    def quantity(self,v):
        value = v

        self.TC.setText(v)
        self.TG.setText(v)
        self.TS.setText(v)
        self.TA.setText(v)
        self.GRAND.setText(v)

    def forTOT(self,v):
        value = v

        self.GRAND.setText(v)



    def load(self):
        self.table.setRowCount(self.rc)
        self.table.setColumnCount(4)
        #self.table.setItem(0,0,QTableWidgetItem("ID"))
        self.table.setItem(0,0,QTableWidgetItem("NAME"))
        self.table.setItem(0,1,QTableWidgetItem("QTY"))
        self.table.setItem(0,2,QTableWidgetItem("RATE"))
        self.table.setItem(0,3,QTableWidgetItem("AMOUNT"))
        






    def parseProduct(self,pname,pqty,prate,pamount):
        qty1 = self.cosinp.text()
        qty2 = self.grocinp.text()
        qty3 = self.alcinp.text()
        qty4 = self.sofinp.text()

        #if self.dictionary == 1:
            #dic = {'Name': pname , 'Qty': pqty , 'Rate': prate , 'Amount': pamount}

            #self.dic3 = dic
            #for k,v  in self.dic3.items():
                #print(k,"---",v)
            #print(self.dic3)
            #self.dictionary +=1


        #else:
            #dic = {'Name': pname, 'Qty': pqty, 'Rate': prate, 'Amount': pamount}
            #self.dic3 = ChainMap(self.dic3 , dic)
            #for k,v in self.dic3.items():
                #print(k,"---",v)
            #print(self.dic3)

        
        if self.row < self.table.rowCount() :
            self.rc
            self.row+=1
            #self.table.setItem(self.row,0,QTableWidgetItem(pid))
            self.table.setItem(self.row,0,QTableWidgetItem(pname))
            self.table.setItem(self.row,1,QTableWidgetItem(pqty))
            self.table.setItem(self.row,2,QTableWidgetItem(prate))
            self.table.setItem(self.row,3,QTableWidgetItem(pamount))

            self.rc = self.table.rowCount()+1
            self.table.setRowCount(self.rc)


        else:
            print("more than row count")
        

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
            #self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            #self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalCosmetics(self):
        name = self.cos_list.currentText()
        #print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM cosmetics WHERE NAME= '"+name+"'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.cosinp.text())
            TCOS = T * inp
            self.C = int(self.TC.text())+TCOS
            self.TC.setText(str(self.C))
            #print(self.TC.text())
                

            con.commit()
            self.message.information(self,"Info","Operation COSM Performed")

        except Exception as e:
            #self.message.information(self,"Error",e)
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
            #self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            #self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalAlcohol(self):
        name = self.alc_list.currentText()
        #print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM alcohol WHERE NAME= '"+name+"'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.alcinp.text())
            TALC = T * inp
            self.A = int(self.TA.text())+TALC
            self.TA.setText(str(self.A))
            #print(self.TA.text())
                

            con.commit()
            self.message.information(self,"Info","Operation ALC Performed")

        except Exception as e:
            #self.message.information(self,"Error",e)
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
            #self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            #self.message.information(self,"Error",e)
            print(e)

            con.close()


    def totalGroceries(self):
        name = self.groc_list.currentText()
        #print(self.cos_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM groceries WHERE NAME= '"+name+"'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.grocinp.text())
            TGROC = T * inp
            self.G = int(self.TG.text())+TGROC
            self.TG.setText(str(self.G))
                

            con.commit()
            self.message.information(self,"Info","Operation GROC Performed")

        except Exception as e:
            #self.message.information(self,"Error",e)
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
            #self.message.information(self,"Info","successfully Loaded")

        except Exception as e:
            #self.message.information(self,"Error",e)
            print(e)

            con.close()

    def totalSoftdrinks(self):
        name = self.sof_list.currentText()
        #print(self.sof_list.currentText())

        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM softdrinks WHERE NAME= '"+name+"'")
            record = cursor.fetchall()

            for r in record:
                T = r[3]

            inp = int(self.sofinp.text())
            TSOF = T * inp
            self.S = int(self.TS.text())+TSOF
            self.TS.setText(str(self.S))
                

            con.commit()
            self.message.information(self,"Info","Operation SOF Performed")

        except Exception as e:
            #self.message.information(self,"Error",e)
            print(e)

            con.close()

    def cosmeticsProduct(self):
        if int(self.cosinp.text()) >= 1:
            
            get = self.cos_list.currentText()
            qty = self.cosinp.text()


        
            try:
                con = sqlite3.connect("./db/mini_database.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM cosmetics WHERE NAME='"+get+"'")
                record = cursor.fetchall()

                cosm = record

                for cm in cosm:
                    total = int(cm[3])*int(qty)
                    #print(total)

                    self.parseProduct(cm[1],qty,str(cm[3]),str(total))
                                  
                con.commit()
                self.totalCosmetics()

            except Exception as e:
                print(e)

                con.close()
        else:
            self.message.information(self,"Info","No Quantity Entered for Cosmetics")

    def groceriesProduct(self):
        
        if int(self.grocinp.text()) >= 1:
             
            get = self.groc_list.currentText()
            qty = self.grocinp.text()


        
            try:
                con = sqlite3.connect("./db/mini_database.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM groceries WHERE NAME='"+get+"'")
                record = cursor.fetchall()

                groc = record

                for gm in groc:
                    total = int(gm[3])*int(qty)
                    #print(total)

                    self.parseProduct(gm[1],qty,str(gm[3]),str(total))
                                  
                con.commit()
                self.totalGroceries()

            except Exception as e:
                print(e)

                con.close()
        else:
            self.message.information(self,"Info","No Quantity Entered for Groceries")


    def alcoholProduct(self):
        if int(self.alcinp.text()) >= 1:
            

            get = self.alc_list.currentText()
            qty = self.alcinp.text()


        
            try:
                con = sqlite3.connect("./db/mini_database.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM alcohol WHERE NAME='"+get+"'")
                record = cursor.fetchall()

                alc = record

                for ac in alc:
                    total = int(ac[3])*int(qty)
                    #print(total)

                    self.parseProduct(ac[1],qty,str(ac[3]),str(total))
                                  
                con.commit()
                self.totalAlcohol()

            except Exception as e:
                print(e)

                con.close()
        else:
            self.message.information(self,"Info","No Quantity Entered for Alcohol")

    def softdrinksProduct(self):
        if int(self.sofinp.text()) >= 1:
            

            get = self.sof_list.currentText()
            qty = self.sofinp.text()


        
            try:
                con = sqlite3.connect("./db/mini_database.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM softdrinks WHERE NAME='"+get+"'")
                record = cursor.fetchall()

                sof = record

                for sf in sof:
                    total = int(sf[3])*int(qty)
                    #print(total)

                    self.parseProduct(sf[1],qty,str(sf[3]),str(total))
                                  
                con.commit()
                self.totalSoftdrinks()

            except Exception as e:
                print(e)

                con.close()
        else:
            self.message.information(self,"Info","No Quantity Entered for SoftDrinks")

    def TOTAL(self):
        self.forTOT("0")
        self.GG = int(self.TC.text())+int(self.TA.text())+int(self.TG.text())+int(self.TS.text())
        self.GRAND.setText(str(int(self.GRAND.text())+self.GG))

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
        self.id()
        self.storage()
        self.message.information(self,"Info","Sales Made and Recorded")
        self.clearfncn()



    def delfcn(self):

        if self.table.rowCount() > 2:
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
                    print(citems[1])
                    u1.append(citems[1])

                print(u1)
                print("u1")
                print(self.nme)
                if self.nme in u1:
                    self.C -= int(self.table.item(var, 3).text())
                    self.TC.setText(str(self.C))


                else:
                    print("NOT HERE!!")


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

                print(u2)
                print("u2")
                print(self.nme)
                if self.nme in u2:
                    self.G -= int(self.table.item(var, 3).text())
                    self.TG.setText(str(self.G))


                else:
                    print("NOT HERE!!")

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

                print(u3)
                print("u3")
                print(self.nme)
                if self.nme in u3:
                    self.A -= int(self.table.item(var, 3).text())
                    self.TA.setText(str(self.A))


                else:
                    print("NOT HERE!!")

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

                print(u4)
                print("u4")
                print(self.nme)
                if self.nme in u4:
                    self.S -= int(self.table.item(var, 3).text())
                    self.TS.setText(str(self.S))


                else:
                    print("NOT HERE!!")
                    pass

                con.commit()
                # self.message.information(self,"Info","successfully Loaded")


            except Exception as e:
                # self.message.information(self,"Error",e)
                print(e)




            self.table.removeRow(var)
            self.row -= 1
            con.close()


        else:
            self.message.information(self, "Info", "You Can't Clear The Whole Table!!!")
        self.forTOT("0")





        #pass
        #s = "LOTION
        #f = self.table.findItems(s)
        #self.mon = 1
        #for i in range (self.row):
            #f = self.table.item(self.mon, 0).text()
            #self.mon+=1


        ####self.table.removeRow(2)
        ####self.row -=1
        #self.matching_items = self.table.findItems(s, Qt.MatchContains)
        #self.table.item(2,1)
        #print(str(self.table. QTableWidgetItem(2,1)))
        #print(self.table.Item(1, 0, QTableWidgetItem()))
        #self.table.QTableWidgetItem(text[, type=Type])

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

            self.bill.setText(str(number))
            number += 1



            con.commit()


        except Exception as e:
            # self.message.information(self,"Error",e)
            print(e)

            con.close()


        try:
            con = sqlite3.connect("./db/mini_database.db")
            cursor = con.cursor()

            cursor.execute("UPDATE ID  SET ID_NUM ='"+str(number)+"' WHERE SN = '"+str(num)+"'")


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

        sid = self.bill.text()
        sname =self.name.text()
        sphone = self.phone.text()
        stotal = self.GRAND.text()



        r = self.table.rowCount()
        c = self.table.columnCount()
        r -=1

        for rr in range(r):
            for cc in range(c):

                l = (self.table.item(rr, cc).text())
                self.li.append(l)
        self.list.append(self.li)

        print(self.list)

        sproducts = str(self.list)

        db.insertRecord(sid, sname, sphone, stotal, sproducts)

        self.li.clear()
        self.list.clear()



        #print(self.table.item(0,1).text())
        #self.A -= int(self.table.item(var, 3).text())

        #g = 0

        #for i in nrows:
            #g+=1
            #print(self.table.item(0, i[2]).text())

        #print(self.table.selectAll().text())








app = QApplication(sys.argv)
M = MAIN()
M.show()

app.exec_()
app.exit()
