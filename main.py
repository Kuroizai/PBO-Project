import wx
import wxres 
import model

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



if __name__=='__main__':
    app = wx.App()
    frame = MyLogin()
    frame.Show()
    app.MainLoop()