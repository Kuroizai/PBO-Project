import wx
import wxres 
import model

class Akun(wxres.Akun_Frame):
    def __init__(self,uname, parent = None):
        wxres.Akun_Frame.__init__(self,parent)
        self.__user = uname

    def get_home(self, event):
        self._goingto = True
        self.go(Home(self.__user))
        self.Destroy()
        
    def go(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()
           
        self._goingto = False


class Toko(wxres.Toko_Frame):
    def __init__(self,uname,parent = None):
        wxres.Toko_Frame.__init__(self,parent)
        self.__user = uname

    def get_home(self, event):
        self._goingto = True
        self.go(Home(self.__user))
        self.Destroy()
        
    def go(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()
           
        self._goingto = False


class Gudang(wxres.Gudang_Frame):
    def __init__(self,uname, parent = None):
        super().__init__(parent)
        self.__user = uname


    def get_home(self, event):
        self._goingto = True
        self.go(Home(self.__user))
        self.Destroy()
        
    def go(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()
           
        self._goingto = False


class Home(wxres.Home_Frame):
    def __init__(self, account ='Guest', parent = None):
        super().__init__(parent)
        self._logout = False
        self.__user = account.title()
        self._goingto = False
        self.as_text.SetLabel(self.__user)

    def log_out(self,event):
        self._logout = True
        self.Close()

        if self.log_out:
            temp = MyLogin()
            temp.Show()

    def go_toko(self, event):
        self._goingto = True
        self.Close()
        self.redirecting(Toko(self.__user))

    def go_akun(self, event):
        self._goingto = True
        self.Close()
        self.redirecting(Akun(self.__user))

    def go_gudang(self, event):
        self._goingto = True
        self.Close()
        self.redirecting(Gudang(self.__user))

    def redirecting(self,classes):
        if self._goingto:
            temp = classes
            temp.Show()


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
            temp = Home(self.__uname)
            temp.Show()


if __name__=='__main__':
    app = wx.App()
    frame = MyLogin()
    frame.Show()
    app.MainLoop()