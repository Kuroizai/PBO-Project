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


class Barang(Database):
    def __init__(self):
        super().__init__()

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS BARANG
                (
                    UNIQUE_IDS VARCHAR PRIMARY KEY ,
                    USERNAME VARCHAR(12) NOT NULL,
                    PASSWORD VARCHAR(12) NOT NULL
                )"""
        self.conn.execute(query)




def rendem_token():
    y = str(dt.date.today().year)
    y = y[2::]
    y+='AKN'
    rdn = (rd.random()*100)
    rdn = f"{rdn:.0f}"
    y+=rdn
    return y

def main():
    y  = rendem_token()
    uname = input()
    passwd = gp.getpass()
    akn = Akun()
    # akn.read()
    # akn.delete('21AKN61')
    # akn.update('21AKN61',uname,passwd)
    # akn.create_table()
    msg = akn.insert(y,uname,passwd)
    print(msg)

if __name__ == '__main__':
    main()
