import wx
import wxres 
import model
import datetime as dt



class About(wxres.About_frame):
    def __init__(self, parent = None):
        super().__init__(parent)


class Detail(wxres.DP_Frame):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.items = []
        self.load()
    
    def reset(self, event):
        for i in range(self.m_griddp.GetNumberRows()):
            self.m_griddp.DeleteRows(pos=0)
        for i in range(len(self.items)):
            self.m_griddp.AppendRows()
            for j in range(len(self.items[i])):
                self.m_griddp.SetCellValue(i,j,str(self.items[i][j]))

    def load(self):
        data = model.Kasir().get_val()
        for lists in data:
            items = []
            for i,item in lists.items():
                items.append(str(item))
            self.items.append(items)
        for i in range(len(self.items)):
            self.m_griddp.AppendRows()
            for j in range(len(self.items[i])):
                self.m_griddp.SetCellValue(i,j,str(self.items[i][j]))
        
    def search(self, event):
        data = []
        for i in range(self.m_griddp.GetNumberRows()):
            self.m_griddp.DeleteRows(pos=0)
        likes = self.search_field.GetValue()
        for lists in model.Kasir().search(likes):
            items = []
            for i,item in lists.items():
                items.append(str(item))
            data.append(items)
        for i in range(len(data)):
            self.m_griddp.AppendRows()
            for j in range(len(data[i])):
                self.m_griddp.SetCellValue(i,j,str(data[i][j]))


class Penjualan(wxres.P_Frame):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.items = []
        self.load()
        

    def reset(self, event):
        for i in range(self.m_gridp.GetNumberRows()):
            self.m_gridp.DeleteRows(pos=0)
        for i in range(len(self.items)):
            self.m_gridp.AppendRows()
            for j in range(len(self.items[i])):
                self.m_gridp.SetCellValue(i,j,str(self.items[i][j]))

    def load(self):
        data = model.Toko().get_val()
        for lists in data:
            items = []
            for i,item in lists.items():
                items.append(str(item))
            self.items.append(items)
        for i in range(len(self.items)):
            self.m_gridp.AppendRows()
            for j in range(len(self.items[i])):
                self.m_gridp.SetCellValue(i,j,str(self.items[i][j]))
        
    def search(self, event):
        data = []
        for i in range(self.m_gridp.GetNumberRows()):
            self.m_gridp.DeleteRows(pos=0)
        likes = self.search_field.GetValue()
        for lists in model.Toko().search(likes):
            items = []
            for i,item in lists.items():
                items.append(str(item))
            data.append(items)
        for i in range(len(data)):
            self.m_gridp.AppendRows()
            for j in range(len(data[i])):
                self.m_gridp.SetCellValue(i,j,str(data[i][j]))


class Toko(wxres.Toko_Frame):
    def __init__(self,uname,parent = None):
        wxres.Toko_Frame.__init__(self,parent)
        self.__user = uname
        self._auth = True
        self.nama_kasir.SetLabel(self.__user)
        self.items = []
        # self.load()
        self._id = model.generate_kode()
        self.date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def get_list(self):
        for i in range(self.m_grid3.GetNumberRows()):
            items = []
            for j in range(self.m_grid3.GetNumberCols()):
                value = self.m_grid3.GetCellValue(i,j)
                items.append(value)
            if items not in self.items:
                self.items.append(items)

    def get_data(self, event):
        self.si = self.m_grid3.GetSelectedRows()
        if self.si != []:
            try:
                self.si = self.si[0]
                self.get_list()
                self.kbr_in.SetValue(self.items[self.si][1])
                self.pcs_in.SetValue(self.items[self.si][3])
                self.disc_in.SetValue(self.items[self.si][5])
            except Exception:
                pass
        self.get_values()

    def check(self,kbr,pcs):
        if kbr.replace(' ','') != '' and pcs >0:
            return True

    def get_values(self):
        self.kbr = self.kbr_in.GetValue()
        self.pcs = self.pcs_in.GetValue()
        self.disc = self.disc_in.GetValue()
    
    def tambah(self, event):
        self.get_list()
        # print(self.items)
        self.get_values()
        self.pcs = int(self.pcs)
        self.disc = float(self.disc)
        if self.check(self.kbr,self.pcs):
            data = model.Gudang().get_specified(self.kbr)
            nbr = data[1]
            hbr = data[-1]
            hpcs = hbr*self.pcs
            self.hr_field.SetLabel(str(hbr))
            sbttl = (hpcs - (hpcs*(self.disc/100)))
            item = [self._id,self.kbr,nbr,self.pcs,hpcs,self.disc,sbttl]
            item = [str(x) for x in item]
            self.m_grid3.AppendRows()
            self.items.append(item)
            # print(self.items)
            for i in range(self.m_grid3.GetNumberRows()):
                for j in range(self.m_grid3.GetNumberCols()):
                    self.m_grid3.SetCellValue(i,j,str(self.items[i][j]))
        self.count_total()

    def count_total(self):
        total = 0
        for i in range(self.m_grid3.GetNumberRows()):
            total += float(self.m_grid3.GetCellValue(i,6))
        # print(self.total)
        self.total_field.SetLabel(str(f"Rp.{total}"))

    def lunas(self, event):
        total = self.total_field.GetLabel()
        model.Toko().insert(self._id,self.date,total)
        self.hr_field.SetLabel('Rp.0')
        for i in range(self.m_grid3.GetNumberRows()):
            self.m_grid3.DeleteRows(pos=0)
        self.kbr_in.SetValue('')
        self.pcs_in.SetValue('')
        self.total_field.SetLabel('Rp. 0.0')
        self.get_list()
        for datas in self.items:
            print(datas)
            model.Kasir().insert(
                datas[0],datas[1],datas[2],datas[3],datas[4],
                datas[5],datas[6]
                )
        self._id = model.generate_kode()
        self.items = []

    def hapus(self, event):
        
        
        m_count = self.m_grid3.GetCellValue(self.si,6)
        total = (self.total_field.GetLabel()).replace('Rp.','')
        total = eval(f"{total}-{m_count}")
        self.total_field.SetLabel(str(f"Rp.{total}"))
        self.items.pop(self.si)
        self.m_grid3.DeleteRows(pos=self.si)

    def get_home(self, event):
        self._goingto = True
        self.go(Home(self.__user))
        self.Destroy()
        
    def go(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()
           
        self._goingto = False

    def kembali(self, event):
        # self.get_home(event)
        self.Destroy()


class Gudang(wxres.Gudang_Frame):
    def __init__(self,uname, parent = None):
        super().__init__(parent)
        self.__user = uname
        self._auth = True
        self.nama_kasir.SetLabel(self.__user)
        self.items= []
        self.load()

    def reset(self, event):
        for i in range(self.m_grid1.GetNumberRows()):
            self.m_grid1.DeleteRows(pos=0)
        for i in range(len(self.items)):
            self.m_grid1.AppendRows()
            for j in range(len(self.items[i])):
                self.m_grid1.SetCellValue(i,j,str(self.items[i][j]))

    def search(self, event):
        data = []
        for i in range(self.m_grid1.GetNumberRows()):
            self.m_grid1.DeleteRows(pos=0)
        likes = self.search_field.GetValue()
        for lists in model.Gudang().search(likes):
            items = []
            for i,item in lists.items():
                items.append(str(item))
            data.append(items)
        for i in range(len(data)):
            self.m_grid1.AppendRows()
            for j in range(len(data[i])):
                self.m_grid1.SetCellValue(i,j,str(data[i][j]))

    def get_home(self, event):
        self._goingto = True
        self.go(Home(self.__user))
        self.Destroy()
        
    def go(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()
           
        self._goingto = False

    def kembali(self, event):
        # self.get_home(event)
        self.Destroy()

    def get_list(self):
        for i in range(self.m_grid1.GetNumberRows()):
            items = []
            for j in range(self.m_grid1.GetNumberCols()):
                value = self.m_grid1.GetCellValue(i,j)
                items.append(value)
            if items not in self.items:
                self.items.append(items)

    def load(self):
        items = model.Gudang().get_val()
        for lists in items:
            items = []
            for i,item in lists.items():
                items.append(str(item))
            self.items.append(items)
        for i in range(len(self.items)):
            self.m_grid1.AppendRows()
            for j in range(len(self.items[i])):
                self.m_grid1.SetCellValue(i,j,str(self.items[i][j]))

    def get_values(self):
        self.nbr = self.nbr_in.GetValue()
        self.kbr = self.nbr[::2].replace(' ','').upper()
        self.jbr = self.jbr_in.GetValue()
        self.stbr = self.stbr_in.GetValue()
        self.hrbr = self.hrbr_in.GetValue()

    def check(self):
        self.get_values()
        self.get_list()
        ck = [self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr]
        for item in ck:
            if item == '' or len(item) ==0:
                return False
        if len(self.items) == 0:
            return True
        for datas in self.items:
            if datas[0] == self.kbr:
                wx.MessageBox('Add Failed \nBarang Exist','Message', wx.OK | wx.ICON_ERROR)
                return False
        else:
            return True

    def tambah(self, event):
        temp = model.Gudang()
        if self.check():
            temp.insert(self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr)
            self.m_grid1.AppendRows()
            self.items.append([self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr])
            for i in range(self.m_grid1.GetNumberRows()):
                for j in range(self.m_grid1.GetNumberCols()):
                    self.m_grid1.SetCellValue(i,j,str(self.items[i][j]))

    def get_data(self, event):
        i = self.m_grid1.GetSelectedRows()
        if i != []:
            i = i[0]
            self.get_list()
            try:    
                self.nbr_in.SetValue(self.items[i][1])
                self.jbr_in.SetValue(self.items[i][2])
                self.stbr_in.SetValue(self.items[i][3])
                self.hrbr_in.SetValue(self.items[i][4])
                self.get_values()
            except Exception:
                pass

    def hapus(self, event):
        temp = model.Gudang()
        self.get_list()
        self.get_values()
        datas = [self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr]
        for i,items in enumerate(self.items):
            # print(datas[0],items[0])
            if datas[0] == items[0]:
                selected = i
                break
        try:
            self.items.pop(selected)
            self.m_grid1.DeleteRows(pos=selected)
            temp.delete(datas[0])
        except Exception:
            pass

    def rubah(self, event):
        temp = model.Gudang()
        self.get_list()
        datas = [self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr]
        for i,item in enumerate(self.items):
            # print(datas[0],item[0])
            if datas[0] == item[0]:
                selected_item = i
                break
        try:
            old_kbr = self.kbr
            self.get_values()

            temp.update(old_kbr,self.nbr,self.jbr,self.stbr,self.hrbr,self.kbr)
            datas = [self.kbr,self.nbr,self.jbr,self.stbr,self.hrbr]
            self.items[selected_item] = datas
            for i,item in enumerate(self.items[selected_item]):
                self.m_grid1.SetCellValue(selected_item,i,str(item))
        except Exception:
            print('No Such Code')


class Home(wxres.Home_Frame):
    def __init__(self, account ='Guest', parent = None):
        super().__init__(parent)
        self._logout = False
        self.__user = account.title()
        self._goingto = False
        self.as_text.SetLabel(self.__user)

    def show_about(self, event):
        self._goingto = True
        self.redirecting(About())

    def log_out(self,event):
        self._logout = True
        self.Close()

        if self.log_out:
            temp = MyLogin()
            temp.Show()

    def go_toko(self, event):
        self._goingto = True
        # self.Close()  
        self.redirecting(Toko(self.__user))

    def go_gudang(self, event):
        self._goingto = True
        # self.Close()
        self.redirecting(Gudang(self.__user))

    def redirecting(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()

    def p_read(self, event):
        Penjualan().Show()


    def dp_read(self, event):
        Detail().Show()


class MyLogin(wxres.Log_Frame):
    def __init__(self, parent = None):
        wxres.Log_Frame.__init__(self,parent)
        self._auth = False
        self.log_try = 1
        self.db = model.Akun()

    def log(self,event):
        if self.log_try == 3:
            wx.MessageBox('Log In Failed \n3 Times Wrong','Message', wx.OK | wx.ICON_AUTH_NEEDED)
            self.Close()
        self.__uname = self.user_field.GetValue()
        self.__pass = self.pw_field.GetValue()
        self.db.get_val()
        if len(self.__uname) == 0 or len(self.__pass) == 0:
            self._auth = False
            wx.MessageBox('Field Empty','Required to fill',wx.OK | wx.ICON_ERROR)
        elif self.__uname.count(' '):
            self._auth = False
            wx.MessageBox("Can't Assign 'Space'",'Space Detected',wx.OK | wx.ICON_ERROR)
        else:
            if self.__uname in self.db._data:
                if self.__pass == self.db._data[self.__uname]:
                    self._auth = True
                    wx.MessageBox('Log In Succeed','Message', wx.OK | wx.ICON_INFORMATION)
                    self.Close()
                else:
                    self._auth = False
                    self.log_try +=1
                    wx.MessageBox('Log In Failed | Wrong Password','Message', wx.OK | wx.ICON_INFORMATION)
            else:
                self._auth = False
                wx.MessageBox('Log In Failed','Message',wx.OK | wx.ICON_ERROR)
        
        if self._auth:
            Home(self.__uname).Show()
            


if __name__=='__main__':
    app = wx.App()
    MyLogin().Show()
    app.MainLoop()