# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Log_Frame
###########################################################################

class Log_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SI_TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		Main_Sizer = wx.BoxSizer( wx.VERTICAL )

		self.title_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Main_Sizer.Add( self.title_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.top_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		field_sizer = wx.GridSizer( 2, 2, 0, 0 )

		self.user_label = wx.StaticText( self.top_panel, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user_label.Wrap( -1 )

		field_sizer.Add( self.user_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.user_field = wx.TextCtrl( self.top_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		field_sizer.Add( self.user_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pass_label = wx.StaticText( self.top_panel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pass_label.Wrap( -1 )

		field_sizer.Add( self.pass_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pw_field = wx.TextCtrl( self.top_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		field_sizer.Add( self.pw_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.top_panel.SetSizer( field_sizer )
		self.top_panel.Layout()
		field_sizer.Fit( self.top_panel )
		Main_Sizer.Add( self.top_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.bot_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.login = wx.Button( self.bot_panel, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.bot_panel.SetSizer( bSizer4 )
		self.bot_panel.Layout()
		bSizer4.Fit( self.bot_panel )
		Main_Sizer.Add( self.bot_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Main_Sizer )
		self.Layout()
		self.status_bar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.status_bar.SetBackgroundColour( wx.Colour( 225, 225, 225 ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.log )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def log( self, event ):
		event.Skip()


