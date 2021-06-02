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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lato" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		Log_mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.text_field = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 2, 0, 0, 0 )

		uname_field = wx.BoxSizer( wx.HORIZONTAL )

		self.uname_label = wx.StaticText( self.text_field, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.uname_label.Wrap( -1 )

		self.uname_label.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lato" ) )

		uname_field.Add( self.uname_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.uname_input = wx.TextCtrl( self.text_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
		self.uname_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat" ) )

		uname_field.Add( self.uname_input, 0, wx.ALL, 5 )


		gSizer1.Add( uname_field, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		pw_field = wx.BoxSizer( wx.HORIZONTAL )

		self.pw_label = wx.StaticText( self.text_field, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pw_label.Wrap( -1 )

		self.pw_label.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lato" ) )

		pw_field.Add( self.pw_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pw_input = wx.TextCtrl( self.text_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		self.pw_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat" ) )

		pw_field.Add( self.pw_input, 0, wx.ALL, 5 )


		gSizer1.Add( pw_field, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.text_field.SetSizer( gSizer1 )
		self.text_field.Layout()
		gSizer1.Fit( self.text_field )
		Log_mainSizer.Add( self.text_field, 1, wx.EXPAND |wx.ALL, 5 )

		self.btn_field = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		Register = wx.BoxSizer( wx.VERTICAL )

		self.reg = wx.Button( self.btn_field, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		Register.Add( self.reg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( Register, 1, wx.EXPAND, 5 )

		Login = wx.BoxSizer( wx.VERTICAL )

		self.log_in = wx.Button( self.btn_field, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		Login.Add( self.log_in, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( Login, 1, wx.EXPAND, 5 )


		self.btn_field.SetSizer( gSizer2 )
		self.btn_field.Layout()
		gSizer2.Fit( self.btn_field )
		Log_mainSizer.Add( self.btn_field, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( Log_mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.reg.Bind( wx.EVT_BUTTON, self.regs )
		self.log_in.Bind( wx.EVT_BUTTON, self.log )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def regs( self, event ):
		event.Skip()

	def log( self, event ):
		event.Skip()


