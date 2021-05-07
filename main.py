import wx
import sqlite3
import wxres 

class MyLogin(wxres.Log_Frame):
    def __init__(self, parent = None):
        wxres.Log_Frame.__init__(self,parent)



if __name__=='__main__':
    app = wx.App()
    frame = MyLogin()
    frame.Show()
    app.MainLoop()