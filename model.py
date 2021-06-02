import sqlite3
import datetime as dt
import random as rd
import getpass as gp
import os


class Database():
    def __init__(self):
        d = os.path.abspath(os.getcwd())
        self._conn = sqlite3.connect(f"{d}\MyDatabase.db")


class Akun(Database):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
        self._data = {}
    
    def get_val(self):
        self._cursor.execute("""SELECT * FROM AKUN""")
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            self._data[item[1]] = item[2]

        return self._data
    
    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS AKUN
                (
                    UNIQUE_IDS VARCHAR PRIMARY KEY ,
                    USERNAME VARCHAR(12) NOT NULL,
                    PASSWORD VARCHAR(12) NOT NULL
                )"""
        self.conn.execute(query)

    def insert(self,tokens,nama,passwd):
        try:
            self.__token = tokens
            self.__uname = nama
            self.__passwd = passwd
            param = (self.__token,self.__uname,self.__passwd)
            query = f"""INSERT INTO AKUN 
                        (UNIQUE_IDS,USERNAME,PASSWORD)
                        VALUES
                        (?,?,?)"""
            self._conn.execute(query,param,)
            self._conn.commit()
            msg = f"ADD ID : {tokens} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def update(self,token,usr,pwd):
        try:
            param = (usr,pwd,token)
            query = """UPDATE AKUN 
                    SET USERNAME = ?,
                        PASSWORD = ?
                    WHERE UNIQUE_IDS = ?"""
            self._conn.execute(query,(param))
            self._conn.commit()
            msg = f"Update ID : {token} Succesfully"
        except Exception:
            msg = "No Such ID"
        return msg

    def delete(self,token):
        try:
            param = (token,)
            query = """DELETE FROM AKUN
                    WHERE UNIQUE_IDS = ?"""
            self._conn.execute(query,param)
            self._conn.commit()
            msg = f"Delete ID : {token} Succesfully"
        except Exception:
            msg = "No Such ID"
        return msg

    def read(self):
        curs = self._conn.cursor()
        query = """SELECT * FROM AKUN"""
        curs.execute(query)
        data = curs.fetchall()
        for item in data:
            print(f"{item[0]:<15s}{item[1]:<15s}{'password':<15s}")


class Gudang(Database):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
        self._data = []

    def search(self,likes):
        items = []
        self._cursor.execute("""SELECT * 
                                FROM GUDANG
                                WHERE KODE_BARANG LIKE ?""",('%'+likes+'%',))
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            items.append(
                {
                    'Kode Barang' : item[0],
                    'Nama Barang' : item[1],
                    'Status Barang' : item[2],
                    'Stock Barang' : item[3],
                    'Harga':item[4]
                }
            )
        return items

    def get_val(self):
        self._cursor.execute("""SELECT * FROM GUDANG""")
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            self._data.append(
                {
                    'Kode Barang' : item[0],
                    'Nama Barang' : item[1],
                    'Status Barang' : item[2],
                    'Stock Barang' : item[3],
                    'Harga':item[4]

                }
            )

        return self._data
    
    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS GUDANG
                (
                    KODE_BARANG VARCHAR PRIMARY KEY ,
                    NAMA_BARANG VARCHAR(12) NOT NULL,
                    JENIS VARCHAR(12) NOT NULL,
                    STOCK_BARANG INTEGER NOT NULL,
                    HARGA INTEGER NOT NULL
                )"""
        self._conn.execute(query)

    def insert(self,kbr,nbr,jbr,sbr,hrbr):
        try:
            param = (kbr,nbr,jbr,sbr,hrbr)
            query = f"""INSERT INTO GUDANG 
                        (KODE_BARANG,NAMA_BARANG,JENIS,STOCK_BARANG,HARGA)
                        VALUES
                        (?,?,?,?,?)"""
            self._conn.execute(query,param,)
            self._conn.commit()
            msg = f"ADD ID : {kbr} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def update(self,kbr,nbr,jbr,sbr,hrbr,nwkbr):
        try:
            param = (nbr,jbr,sbr,hrbr,kbr)
            query = """UPDATE GUDANG 
                    SET NAMA_BARANG = ?,
                        JENIS = ?,
                        STOCK_BARANG = ?,
                        HARGA = ?
                    WHERE KODE_BARANG = ?"""
            self._conn.execute(query,(param))
            self._conn.commit()
            msg = f"Update ID : {kbr} Succesfully"
            self.update_primval(nwkbr,nbr)
        except Exception as e:
            print(e)
            msg = "No Such ID"
        return msg

    def update_primval(self,kbr,nbr):
        param = (kbr,nbr)
        query = """UPDATE GUDANG
                SET KODE_BARANG = ?
                WHERE NAMA_BARANG = ?"""
        self._conn.execute(query,(param))
        self._conn.commit()

    def get_specified(self,kbr):
        param = (kbr)
        query = """SELECT * FROM GUDANG WHERE KODE_BARANG =?"""
        self._cursor.execute(query,(param,))
        self.__res = self._cursor.fetchall()[0]
        return self.__res

    def delete(self,kbr):
        try:
            param = (kbr,)
            query = """DELETE FROM GUDANG
                    WHERE KODE_BARANG = ?"""
            self._conn.execute(query,param)
            self._conn.commit()
            msg = f"Delete ID : {kbr} Succesfully"
        except Exception:
            msg = "No Such ID"
        return msg

    def read(self):
        curs = self._conn.cursor()
        query = """SELECT * FROM GUDANG"""
        curs.execute(query)
        data = curs.fetchall()
        for item in data:
            print(item)


class Toko(Database):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
        self._data = []

    def search(self,likes):
        data = []
        self._cursor.execute("""SELECT * 
                                FROM PENJUALAN
                                WHERE ID_TRANKSAKSI LIKE ?""",
                                ('%'+likes+'%',))
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            data.append(
                {
                    'ID Tranksaksi' : item[0],
                    'Tanggal' : item[1],
                    'Total' : item[2]
                }
            )
        return data

    def get_val(self):
        self._cursor.execute("""SELECT * FROM PENJUALAN""")
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            self._data.append(
                {
                    'ID Tranksaksi' : item[0],
                    'Tanggal' : item[1],
                    'Total' : item[2]
                }
            )
        return self._data

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS PENJUALAN
                (
                    ID_TRANKSAKSI VARCHAR PRIMARY KEY,
                    TANGGAL DATETIME NOT NULL,
                    TOTAL INT NOT NULL
                )"""
        self._conn.execute(query)

    def insert(self,idt,tg,ttl):
        try:
            param = (idt,tg,ttl)
            query = f"""INSERT INTO PENJUALAN
                        (ID_TRANKSAKSI,TANGGAL,TOTAL)
                        VALUES
                        (?,?,?)"""
            self._conn.execute(query,param,)
            self._conn.commit()
            msg = f"ADD ID : {idt} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def update(self,idt,tg,ttl):
        try:
            param = (idt,tg,ttl)
            query = """UPDATE PENJUALAN 
                    SET TANGGAL = ?,
                        TOTAL = ?,
                    WHERE ID_TRANKSAKSI = ?"""
            self._conn.execute(query,(param))
            self._conn.commit()
            msg = f"Update ID : {idt} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def delete(self,idt):
        try:
            param = (idt,)
            query = """DELETE FROM PENJUALAN
                    WHERE ID_TRANKSAKSI = ?"""
            self._conn.execute(query,param)
            self._conn.commit()
            msg = f"Delete ID : {idt} Succesfully"
        except Exception:
            msg = "No Such ID"
        return msg


class Kasir(Database):
    def __init__(self):
        super().__init__()
        self._cursor = self._conn.cursor()
        self._data = []

    def search(self,likes):
        data = []
        self._cursor.execute("""SELECT * 
                                FROM DETAIL
                                WHERE ID LIKE ?""",('%'+likes+'%',))
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            data.append(
                {
                    'Id Tranksaksi' : item[0],
                    'Kode Item' : item[1],
                    'Nama Item' : item[2],
                    'Pieces' : item[3],
                    'Harga' : item[4],
                    'Diskon' : item[5],
                    'Sub Total' : item[6]
                }
            )
        return data
    
    def get_val(self):
        self._cursor.execute("""SELECT * FROM DETAIL""")
        self.__res = self._cursor.fetchall()
        for item in self.__res:
            self._data.append(
                {
                    'Id Tranksaksi' : item[0],
                    'Kode Item' : item[1],
                    'Nama Item' : item[2],
                    'Pieces' : item[3],
                    'Harga' : item[4],
                    'Diskon' : item[5],
                    'Sub Total' : item[6]
                }
            )
        return self._data


    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS DETAIL
                (
                    ID VARCHAR ,
                    KODE_ITEM VARCHAR,
                    NAMA_ITEM DATETIME NOT NULL,
                    PCS INT NOT NULL,
                    HARGA INT NOT NULL,
                    DISKON INT NOT NULL,
                    SUB_TOTAL INT NOT NULL,
                    FOREIGN KEY(ID) REFERENCES PENJUALAN(ID_TRANKSAKSI)
                )"""
        self._conn.execute(query)

    def insert(self,idt,ki,ni,pcs,hrg,dsc,sttl):
        try:
            param = (idt,ki,ni,pcs,hrg,dsc,sttl)
            query = f"""INSERT INTO DETAIL
                        (
                            ID,KODE_ITEM,NAMA_ITEM,
                            PCS,HARGA,DISKON,SUB_TOTAL
                        )
                        VALUES
                        (?,?,?,?,?,?,?)"""
            self._conn.execute(query,param,)
            self._conn.commit()
            msg = f"ADD ID : {idt} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def update(self,idt,ki,ni,pcs,hrg,dsc,sttl):
        try:
            param = (idt,ki,ni,pcs,hrg,dsc,sttl)
            query = """UPDATE DETAIL
                    SET ID = ?,
                    KODE_ITEM = ?,NAMA_ITEM = ?,
                    PCS = ?,HARGA = ?,DISKON = ?,SUB_TOTAL = ?,
                    WHERE ID = ?"""
            self._conn.execute(query,(param))
            self._conn.commit()
            msg = f"Update ID : {idt} Succesfully"
        except Exception as e:
            print(e)
            msg = "ID ALREADY EXIST"
        return msg

    def delete(self,idt):
        try:
            param = (idt,)
            query = """DELETE FROM DETAIL
                    WHERE ID = ?"""
            self._conn.execute(query,param)
            self._conn.commit()
            msg = f"Delete ID : {idt} Succesfully"
        except Exception:
            msg = "No Such ID"
        return msg



def rendem_token():
    y = str(dt.date.today().year)
    y = y[2::]
    y+='AKN'
    rdn = (rd.random()*100)
    rdn = f"{rdn:.0f}"
    y+=rdn
    return y

def generate_kode():
    year = str(dt.date.today().year)
    month = str(dt.date.today().month)
    day = str(dt.date.today().day)
    hour = str((dt.datetime.now()).strftime("%H%M%S"))
    name = (dt.datetime.now()).strftime("%A")[::2].upper()
    kode = (day+month+name+year+hour)
    return kode

def main():
    # y  = rendem_token()
    # uname = input()
    # passwd = gp.getpass()
    # akn = Akun()
    # akn.read()
    # akn.delete('21AKN61')
    # akn.update('21AKN61',uname,passwd)
    # akn.create_table()
    # msg = akn.insert(y,uname,passwd)
    # print(msg)
    nambar = 'DAIA PEMBERSIH BUBUK'
    nbr = nambar[::2].replace(' ','')
    gd = Gudang()
    # gd.get_specified('DIEBRIUU')
    gd.search("BRIUU")
    # gd.create_table()
    # gd.insert(nbr,nambar,'Bahan Kimia',30,5000)
    # gd.delete('DI EBRI UU')
    # val = gd.get_val()
    # for item in val:
        # print(item)
    # pass
    # y = generate_kode()
    # tk = Toko()
    # date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # tk.create_table()
    # tk.insert(y,date,50000)
    # ks = Kasir()
    # ks.create_table()
    # psc = 10
    # hrg = 5000
    # ks.insert(y,nbr,nambar,psc,hrg,0,psc+hrg)
    # val = tk.get_val()
    # for item in val:
    #     print(item)
    # val = ks.get_val()
    # for item in val:
    #     print(item)

if __name__ == '__main__':
    main()
    # generate_kode()
    # dictku = {'a':0,'b':2}
    # for i, item in dictku.items():
    #     print(i,item)