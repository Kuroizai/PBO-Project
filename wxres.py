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

		self.SetSizeHints( wx.Size( 500,300 ), wx.Size( 800,600 ) )
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
		self.dp_trigger = wx.MenuItem( self.menu1, wx.ID_ANY, u"Detail Penjualan", wx.EmptyString, wx.ITEM_NORMAL )
		self.dp_trigger.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_PAGE, wx.ART_TOOLBAR ) )
		self.menu1.Append( self.dp_trigger )

		self.p_trigger = wx.MenuItem( self.menu1, wx.ID_ANY, u"Penjualan", wx.EmptyString, wx.ITEM_NORMAL )
		self.p_trigger.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK, wx.ART_TOOLBAR ) )
		self.menu1.Append( self.p_trigger )

		self.menubar.Append( self.menu1, u"Read" )

		self.menu2 = wx.Menu()
		self.about_mitem = wx.MenuItem( self.menu2, wx.ID_ANY, u"About APP", wx.EmptyString, wx.ITEM_NORMAL )
		self.about_mitem.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP, wx.ART_MENU ) )
		self.menu2.Append( self.about_mitem )

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
		self.Bind( wx.EVT_MENU, self.dp_read, id = self.dp_trigger.GetId() )
		self.Bind( wx.EVT_MENU, self.p_read, id = self.p_trigger.GetId() )
		self.Bind( wx.EVT_MENU, self.show_about, id = self.about_mitem.GetId() )
		self.Bind( wx.EVT_MENU, self.log_out, id = self.m_menuItem2.GetId() )
		self.m_button2.Bind( wx.EVT_BUTTON, self.go_toko )
		self.m_button3.Bind( wx.EVT_BUTTON, self.go_gudang )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dp_read( self, event ):
		event.Skip()

	def p_read( self, event ):
		event.Skip()

	def show_about( self, event ):
		event.Skip()

	def log_out( self, event ):
		event.Skip()

	def go_toko( self, event ):
		event.Skip()

	def go_gudang( self, event ):
		event.Skip()


###########################################################################
## Class Gudang_Frame
###########################################################################

class Gudang_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gudang SI-TONG", pos = wx.DefaultPosition, size = wx.Size( 800,603 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.crud_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		self.text_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self.text_field, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.text_field, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.text_field, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetMinSize( wx.Size( -1,25 ) )

		bSizer13.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.text_field, wx.ID_ANY, u"Harga Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer13.Add( self.m_staticText23, 0, wx.ALL, 5 )


		self.text_field.SetSizer( bSizer13 )
		self.text_field.Layout()
		bSizer13.Fit( self.text_field )
		gSizer2.Add( self.text_field, 1, wx.ALL|wx.EXPAND, 5 )

		self.input_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.nbr_in = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.nbr_in, 0, wx.ALL|wx.EXPAND, 5 )

		self.jbr_in = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.jbr_in, 0, wx.ALL|wx.EXPAND, 5 )

		self.stbr_in = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.stbr_in, 0, wx.ALL|wx.EXPAND, 5 )

		self.hrbr_in = wx.TextCtrl( self.input_field, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.hrbr_in, 0, wx.ALL|wx.EXPAND, 5 )


		self.input_field.SetSizer( bSizer14 )
		self.input_field.Layout()
		bSizer14.Fit( self.input_field )
		gSizer2.Add( self.input_field, 1, wx.EXPAND |wx.ALL, 5 )

		self.button_field = wx.Panel( self.crud_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.addbr = wx.Button( self.button_field, wx.ID_ANY, u"ADD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addbr.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.addbr, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.upbr = wx.Button( self.button_field, wx.ID_ANY, u"UPDATE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.upbr.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.upbr, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.delbr = wx.Button( self.button_field, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.delbr.SetMinSize( wx.Size( -1,25 ) )

		bSizer15.Add( self.delbr, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


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
		self.m_grid1.CreateGrid( 0, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 100 )
		self.m_grid1.SetColSize( 1, 100 )
		self.m_grid1.SetColSize( 2, 100 )
		self.m_grid1.SetColSize( 3, 100 )
		self.m_grid1.SetColSize( 4, 100 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Kode Barang" )
		self.m_grid1.SetColLabelValue( 1, u"Nama Barang" )
		self.m_grid1.SetColLabelValue( 2, u"Jenis Barang" )
		self.m_grid1.SetColLabelValue( 3, u"Stock" )
		self.m_grid1.SetColLabelValue( 4, u"Harga" )
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
		self.m_panel20.SetBackgroundColour( wx.Colour( 85, 85, 85 ) )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button16 = wx.Button( self.m_panel20, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_label = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Cari Kode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_label.Wrap( -1 )

		self.search_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer17.Add( self.search_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_field = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.search_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_button = wx.Button( self.m_panel20, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.search_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.reset_button = wx.Button( self.m_panel20, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.reset_button, 0, wx.ALL, 5 )


		bSizer38.Add( bSizer17, 1, wx.EXPAND, 5 )

		self.nama_kasir = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nama Kasir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kasir.Wrap( -1 )

		self.nama_kasir.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer38.Add( self.nama_kasir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel20.SetSizer( bSizer38 )
		self.m_panel20.Layout()
		bSizer38.Fit( self.m_panel20 )
		main_sizer.Add( self.m_panel20, 0, wx.EXPAND, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.addbr.Bind( wx.EVT_BUTTON, self.tambah )
		self.upbr.Bind( wx.EVT_BUTTON, self.rubah )
		self.delbr.Bind( wx.EVT_BUTTON, self.hapus )
		self.m_grid1.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.get_data )
		self.m_button16.Bind( wx.EVT_BUTTON, self.kembali )
		self.search_button.Bind( wx.EVT_BUTTON, self.search )
		self.reset_button.Bind( wx.EVT_BUTTON, self.reset )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambah( self, event ):
		event.Skip()

	def rubah( self, event ):
		event.Skip()

	def hapus( self, event ):
		event.Skip()

	def get_data( self, event ):
		event.Skip()

	def kembali( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()

	def reset( self, event ):
		event.Skip()


###########################################################################
## Class Toko_Frame
###########################################################################

class Toko_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Toko SI_TONG", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button12 = wx.Button( self.m_panel16, wx.ID_ANY, u"Tambah Item", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button12.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_FRAME_ICON ) )
		bSizer20.Add( self.m_button12, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer20, 0, 0, 5 )

		bSizer271 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText24 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Kode Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer271.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kbr_in = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.kbr_in, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"pcs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer271.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pcs_in = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.pcs_in, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer271, 1, wx.EXPAND, 5 )

		self.hr_field = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Rp. 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hr_field.Wrap( -1 )

		bSizer17.Add( self.hr_field, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer3.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer21.Add( self.m_staticText12, 0, wx.ALL, 5 )


		bSizer19.Add( bSizer21, 0, 0, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.total_field = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Rp.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.total_field.Wrap( -1 )

		self.total_field.SetFont( wx.Font( 28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer22.Add( self.total_field, 0, wx.ALL, 5 )


		bSizer19.Add( bSizer22, 0, 0, 5 )


		gSizer3.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.m_panel16.SetSizer( gSizer3 )
		self.m_panel16.Layout()
		gSizer3.Fit( self.m_panel16 )
		bSizer16.Add( self.m_panel16, 0, wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid3 = wx.grid.Grid( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 0, 7 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 90 )
		self.m_grid3.SetColSize( 1, 100 )
		self.m_grid3.SetColSize( 2, 100 )
		self.m_grid3.SetColSize( 3, 50 )
		self.m_grid3.SetColSize( 4, 80 )
		self.m_grid3.SetColSize( 5, 100 )
		self.m_grid3.SetColSize( 6, 100 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"Id" )
		self.m_grid3.SetColLabelValue( 1, u"Kode Item" )
		self.m_grid3.SetColLabelValue( 2, u"Nama Item" )
		self.m_grid3.SetColLabelValue( 3, u"pcs" )
		self.m_grid3.SetColLabelValue( 4, u"Harga * pcs" )
		self.m_grid3.SetColLabelValue( 5, u"Diskon" )
		self.m_grid3.SetColLabelValue( 6, u"Sub Total" )
		self.m_grid3.SetColLabelValue( 7, wx.EmptyString )
		self.m_grid3.SetColLabelValue( 8, wx.EmptyString )
		self.m_grid3.SetColLabelValue( 9, wx.EmptyString )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 30 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer28.Add( self.m_grid3, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.del_button = wx.Button( self.m_panel17, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.del_button, 0, wx.ALL|wx.EXPAND, 5 )

		self.lunasdah = wx.Button( self.m_panel17, wx.ID_ANY, u"Lunas", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.lunasdah, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText26 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Diskon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer27.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.disc_in = wx.TextCtrl( self.m_panel17, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.disc_in, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer27, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.m_panel17.SetSizer( bSizer25 )
		self.m_panel17.Layout()
		bSizer25.Fit( self.m_panel17 )
		bSizer16.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.Colour( 85, 85, 85 ) )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button14 = wx.Button( self.m_panel19, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button14, 0, wx.ALL, 5 )


		gSizer5.Add( bSizer29, 1, wx.EXPAND, 5 )

		self.nama_kasir = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Nama Kasir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kasir.Wrap( -1 )

		self.nama_kasir.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gSizer5.Add( self.nama_kasir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		self.m_panel19.SetSizer( gSizer5 )
		self.m_panel19.Layout()
		gSizer5.Fit( self.m_panel19 )
		bSizer16.Add( self.m_panel19, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button12.Bind( wx.EVT_BUTTON, self.tambah )
		self.m_grid3.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.get_data )
		self.del_button.Bind( wx.EVT_BUTTON, self.hapus )
		self.lunasdah.Bind( wx.EVT_BUTTON, self.lunas )
		self.m_button14.Bind( wx.EVT_BUTTON, self.kembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambah( self, event ):
		event.Skip()

	def get_data( self, event ):
		event.Skip()

	def hapus( self, event ):
		event.Skip()

	def lunas( self, event ):
		event.Skip()

	def kembali( self, event ):
		event.Skip()


###########################################################################
## Class DP_Frame
###########################################################################

class DP_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detail Penjualan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 900,400 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_griddp = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_griddp.CreateGrid( 0, 7 )
		self.m_griddp.EnableEditing( True )
		self.m_griddp.EnableGridLines( True )
		self.m_griddp.EnableDragGridSize( False )
		self.m_griddp.SetMargins( 0, 0 )

		# Columns
		self.m_griddp.SetColSize( 0, 130 )
		self.m_griddp.SetColSize( 1, 100 )
		self.m_griddp.SetColSize( 2, 100 )
		self.m_griddp.SetColSize( 3, 100 )
		self.m_griddp.SetColSize( 4, 100 )
		self.m_griddp.SetColSize( 5, 100 )
		self.m_griddp.SetColSize( 6, 100 )
		self.m_griddp.EnableDragColMove( False )
		self.m_griddp.EnableDragColSize( True )
		self.m_griddp.SetColLabelSize( 30 )
		self.m_griddp.SetColLabelValue( 0, u"ID" )
		self.m_griddp.SetColLabelValue( 1, u"Kode Barang" )
		self.m_griddp.SetColLabelValue( 2, u"Nama Item" )
		self.m_griddp.SetColLabelValue( 3, u"Pieces" )
		self.m_griddp.SetColLabelValue( 4, u"Harga*pcs" )
		self.m_griddp.SetColLabelValue( 5, u"Diskon" )
		self.m_griddp.SetColLabelValue( 6, u"Sub Total" )
		self.m_griddp.SetColLabelValue( 7, wx.EmptyString )
		self.m_griddp.SetColLabelValue( 8, u"Kode Item" )
		self.m_griddp.SetColLabelValue( 9, u"Nama Barang" )
		self.m_griddp.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_griddp.EnableDragRowSize( True )
		self.m_griddp.SetRowLabelSize( 80 )
		self.m_griddp.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_griddp.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer28.Add( self.m_griddp, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Search ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer37.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.search_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_button = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.search_button, 0, wx.ALL, 5 )

		self.reset_button = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.reset_button, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer37, 0, 0, 5 )


		self.SetSizer( bSizer28 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.search_button.Bind( wx.EVT_BUTTON, self.search )
		self.reset_button.Bind( wx.EVT_BUTTON, self.reset )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def search( self, event ):
		event.Skip()

	def reset( self, event ):
		event.Skip()


###########################################################################
## Class P_Frame
###########################################################################

class P_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penjualan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,400 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_gridp = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_gridp.CreateGrid( 0, 3 )
		self.m_gridp.EnableEditing( True )
		self.m_gridp.EnableGridLines( True )
		self.m_gridp.EnableDragGridSize( False )
		self.m_gridp.SetMargins( 0, 0 )

		# Columns
		self.m_gridp.SetColSize( 0, 130 )
		self.m_gridp.SetColSize( 1, 150 )
		self.m_gridp.SetColSize( 2, 100 )
		self.m_gridp.EnableDragColMove( False )
		self.m_gridp.EnableDragColSize( True )
		self.m_gridp.SetColLabelSize( 30 )
		self.m_gridp.SetColLabelValue( 0, u"ID" )
		self.m_gridp.SetColLabelValue( 1, u"Tanggal" )
		self.m_gridp.SetColLabelValue( 2, u"Total" )
		self.m_gridp.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridp.EnableDragRowSize( True )
		self.m_gridp.SetRowLabelSize( 80 )
		self.m_gridp.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridp.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer28.Add( self.m_gridp, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.search_field = wx.StaticText( self, wx.ID_ANY, u"Search ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_field.Wrap( -1 )

		bSizer38.Add( self.search_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_field = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.search_field, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.search_button = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.search_button, 0, wx.ALL, 5 )

		self.reset_button = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.reset_button, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer38, 0, 0, 5 )


		self.SetSizer( bSizer28 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.search_button.Bind( wx.EVT_BUTTON, self.search )
		self.reset_button.Bind( wx.EVT_BUTTON, self.reset )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def search( self, event ):
		event.Skip()

	def reset( self, event ):
		event.Skip()


###########################################################################
## Class About_frame
###########################################################################

class About_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Barang", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel19, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\intel\\Downloads\\inventory.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap1.SetMinSize( wx.Size( 800,300 ) )

		bSizer32.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel19.SetSizer( bSizer32 )
		self.m_panel19.Layout()
		bSizer32.Fit( self.m_panel19 )
		bSizer30.Add( self.m_panel19, 1, wx.EXPAND, 5 )

		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"SI-TONG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer34.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Sistem Informasi Toko dan Gudang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer34.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"V.A.01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer34.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Adwitya Sadhu Prayastita", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer35.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Dinda Putri Ani", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer35.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Yusrian Darus Syifa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer35.Add( self.m_staticText25, 0, wx.ALL, 5 )


		bSizer34.Add( bSizer35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer31.Add( bSizer34, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"@2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer33.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer31.Add( bSizer33, 0, wx.EXPAND, 5 )


		self.m_panel20.SetSizer( bSizer31 )
		self.m_panel20.Layout()
		bSizer31.Fit( self.m_panel20 )
		bSizer30.Add( self.m_panel20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


