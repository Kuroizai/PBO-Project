# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

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


###########################################################################
## Class Home_Frame
###########################################################################

class Home_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SI-TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		self.menubar = wx.MenuBar( 0 )
		self.menu1 = wx.Menu()
		self.open_menu = wx.Menu()
		self.menu1.AppendSubMenu( self.open_menu, u"Open" )

		self.save_menu = wx.Menu()
		self.menu1.AppendSubMenu( self.save_menu, u"Save" )

		self.menubar.Append( self.menu1, u"File" )

		self.menu2 = wx.Menu()
		self.menubar.Append( self.menu2, u"Help" )

		self.menu4 = wx.Menu()
		self.menubar.Append( self.menu4, u"Tools" )

		self.menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.menu3, wx.ID_ANY, u"Log Out", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_TOOLBAR ) )
		self.menu3.Append( self.m_menuItem2 )

		self.menubar.Append( self.menu3, u"Option" )

		self.SetMenuBar( self.menubar )

		content_sizer = wx.BoxSizer( wx.VERTICAL )

		self.logged_as_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self.logged_as_panel, wx.ID_ANY, u"You Logged In As :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.as_container = wx.Panel( self.logged_as_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.as_text = wx.StaticText( self.as_container, wx.ID_ANY, u"Guest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.as_text.Wrap( -1 )

		bSizer4.Add( self.as_text, 0, 0, 5 )


		self.as_container.SetSizer( bSizer4 )
		self.as_container.Layout()
		bSizer4.Fit( self.as_container )
		bSizer5.Add( self.as_container, 1, wx.ALL, 5 )


		self.logged_as_panel.SetSizer( bSizer5 )
		self.logged_as_panel.Layout()
		bSizer5.Fit( self.logged_as_panel )
		content_sizer.Add( self.logged_as_panel, 0, wx.ALL, 5 )

		self.content_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self.content_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"SI-TONG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat" ) )

		bSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Sistem Informasi Toko dan Gudang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Montserrat" ) )

		bSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel8.SetSizer( bSizer7 )
		self.m_panel8.Layout()
		bSizer7.Fit( self.m_panel8 )
		bSizer6.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel9 = wx.Panel( self.content_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button2 = wx.Button( self.m_panel9, wx.ID_ANY, u"Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.m_panel9, wx.ID_ANY, u"Gudang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.ALL, 5 )


		self.m_panel9.SetSizer( bSizer8 )
		self.m_panel9.Layout()
		bSizer8.Fit( self.m_panel9 )
		bSizer6.Add( self.m_panel9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel10 = wx.Panel( self.content_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self.m_panel10, wx.ID_ANY, u"Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button4, 0, wx.ALL, 5 )


		self.m_panel10.SetSizer( bSizer10 )
		self.m_panel10.Layout()
		bSizer10.Fit( self.m_panel10 )
		bSizer6.Add( self.m_panel10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.content_panel.SetSizer( bSizer6 )
		self.content_panel.Layout()
		bSizer6.Fit( self.content_panel )
		content_sizer.Add( self.content_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( content_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.log_out, id = self.m_menuItem2.GetId() )
		self.m_button2.Bind( wx.EVT_BUTTON, self.go_toko )
		self.m_button3.Bind( wx.EVT_BUTTON, self.go_gudang )
		self.m_button4.Bind( wx.EVT_BUTTON, self.go_akun )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def log_out( self, event ):
		event.Skip()

	def go_toko( self, event ):
		event.Skip()

	def go_gudang( self, event ):
		event.Skip()

	def go_akun( self, event ):
		event.Skip()


###########################################################################
## Class Gudang_Frame
###########################################################################

class Gudang_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gudang SI-TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.crud_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		self.text_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.text_field, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.text_field, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.text_field, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )


		self.text_field.SetSizer( bSizer13 )
		self.text_field.Layout()
		bSizer13.Fit( self.text_field )
		gSizer2.Add( self.text_field, 1, wx.ALL|wx.EXPAND, 5 )

		self.input_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl3 = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.SetMinSize( wx.Size( -1,25 ) )

		bSizer14.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMinSize( wx.Size( -1,25 ) )

		bSizer14.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl5.SetMinSize( wx.Size( -1,25 ) )

		bSizer14.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )


		self.input_field.SetSizer( bSizer14 )
		self.input_field.Layout()
		bSizer14.Fit( self.input_field )
		gSizer2.Add( self.input_field, 1, wx.EXPAND |wx.ALL, 5 )

		self.button_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self.button_field, wx.ID_ANY, u"ADD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button6 = wx.Button( self.button_field, wx.ID_ANY, u"UPDATE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button7 = wx.Button( self.button_field, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.button_field.SetSizer( bSizer15 )
		self.button_field.Layout()
		bSizer15.Fit( self.button_field )
		gSizer2.Add( self.button_field, 1, wx.EXPAND |wx.ALL, 5 )


		self.crud_panel.SetSizer( gSizer2 )
		self.crud_panel.Layout()
		gSizer2.Fit( self.crud_panel )
		main_sizer.Add( self.crud_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.Grid_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self.Grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )


		self.Grid_panel.SetSizer( bSizer16 )
		self.Grid_panel.Layout()
		bSizer16.Fit( self.Grid_panel )
		main_sizer.Add( self.Grid_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.view_detail = wx.Button( self.m_panel20, wx.ID_ANY, u"View", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.view_detail, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer17 )
		self.m_panel20.Layout()
		bSizer17.Fit( self.m_panel20 )
		main_sizer.Add( self.m_panel20, 0, wx.ALL, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.get_home )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def get_home( self, event ):
		event.Skip()


###########################################################################
## Class Toko_Frame
###########################################################################

class Toko_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Toko SI_TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.get_home )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def get_home( self, event ):
		event.Skip()


###########################################################################
## Class Akun_Frame
###########################################################################

class Akun_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Akun SI-TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,400 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.get_home )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def get_home( self, event ):
		event.Skip()


