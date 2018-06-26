# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"なんやかんや通信する奴", pos = wx.DefaultPosition, size = wx.Size( 820,581 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 400,400 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"接続先：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer28.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"IPアドレス", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer28.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ポート", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer28.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"他の情報", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer28.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"モデムライン状態" ), wx.HORIZONTAL )
		
		self.m_staticText35 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"DSR(6):      , CTS(8):       , DCD(1)       , RI(9):     , GND(5)                ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		sbSizer3.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox5 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"DTR(4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.SetValue(True) 
		sbSizer3.Add( self.m_checkBox5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox6 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"RTS(7)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetValue(True) 
		sbSizer3.Add( self.m_checkBox6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText34 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"送信データをtxtファイルから読み出す：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer42.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Text file(*.txt)|*.txt|CSV file(*.csv)|*.csv|All file(*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer42.Add( self.m_filePicker1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText251 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ログは接続先+日時で保存されます", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		bSizer29.Add( self.m_staticText251, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer29.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"送信文字数（バイト）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer29.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl8.SetMaxLength( 30 ) 
		bSizer29.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText20 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"送信データ", wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER )
		self.m_staticText20.Wrap( -1 )
		bSizer32.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"改行コード変換", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer32.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox6Choices = [ u"No", u"CR", u"LF", u"CRLF" ]
		self.m_comboBox6 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"CR", wx.DefaultPosition, wx.DefaultSize, m_comboBox6Choices, wx.CB_READONLY )
		self.m_comboBox6.SetSelection( 1 )
		bSizer32.Add( self.m_comboBox6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel1, wx.ID_ANY, u"送信クリア", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"自動送信間隔", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer32.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox7Choices = [ u"No", u"100ms", u"500ms", u"1s", u"5s", u"10s" ]
		self.m_comboBox7 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		self.m_comboBox7.SetSelection( 0 )
		bSizer32.Add( self.m_comboBox7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"送信後にテキストエリアをクリア", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_checkBox4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel1, wx.ID_ANY, u"送信", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer27.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl9 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer33.Add( self.m_textCtrl9, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText24 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ASCII表示では、0x00Hは「~」に変換されます", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer36.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		
		bSizer34.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button16 = wx.Button( self.m_panel1, wx.ID_ANY, u"ポート選択", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button16.Hide()
		
		bSizer37.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer37.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"読出し間隔タイムアウト：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer37.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.m_textCtrl10.SetMaxSize( wx.Size( 50,-1 ) )
		
		bSizer37.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText28 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"ms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer37.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer34.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"受信データ", wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER )
		self.m_staticText29.Wrap( -1 )
		bSizer40.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"表示形式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer40.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox8Choices = [ u"utf-8", u"shift-jis", u"ascii" ]
		self.m_comboBox8 = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"utf-8", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, wx.CB_READONLY )
		self.m_comboBox8.SetSelection( 0 )
		bSizer40.Add( self.m_comboBox8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button17 = wx.Button( self.m_panel1, wx.ID_ANY, u"受信クリア", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_button17, 0, wx.ALL, 5 )
		
		
		bSizer39.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"受信ボックス内文字数（バイト）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer41.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer41.Add( self.m_textCtrl12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer39.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer39, 0, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl11 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer38.Add( self.m_textCtrl11, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer27 )
		self.m_panel1.Layout()
		bSizer27.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"シリアル設定", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu1, u"設定" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_timer3 = wx.Timer()
		self.m_timer3.SetOwner( self, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.ExitHandler )
		self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.DTR_ctrl )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.RTS_ctrl )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.Open_file )
		self.m_button14.Bind( wx.EVT_BUTTON, self.send_clear )
		self.m_comboBox7.Bind( wx.EVT_COMBOBOX, self.Auto_Send )
		self.m_button15.Bind( wx.EVT_BUTTON, self.Send_text )
		self.m_textCtrl9.Bind( wx.EVT_TEXT, self.Input_text )
		self.m_comboBox8.Bind( wx.EVT_COMBOBOX, self.change_encode )
		self.m_button17.Bind( wx.EVT_BUTTON, self.recv_clear )
		self.Bind( wx.EVT_TIMER, self.Send_text, id=wx.ID_ANY )
		self.Bind( wx.EVT_MENU, self.Serial_option, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_TIMER, self.Modem_line, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ExitHandler( self, event ):
		event.Skip()
	
	def DTR_ctrl( self, event ):
		event.Skip()
	
	def RTS_ctrl( self, event ):
		event.Skip()
	
	def Open_file( self, event ):
		event.Skip()
	
	def send_clear( self, event ):
		event.Skip()
	
	def Auto_Send( self, event ):
		event.Skip()
	
	def Send_text( self, event ):
		event.Skip()
	
	def Input_text( self, event ):
		event.Skip()
	
	def change_encode( self, event ):
		event.Skip()
	
	def recv_clear( self, event ):
		event.Skip()
	
	
	def Serial_option( self, event ):
		event.Skip()
	
	def Modem_line( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"テキストファイルから送信", pos = wx.DefaultPosition, size = wx.Size( 500,367 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self.m_panel5, wx.ID_ANY, u"順番に送信", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"自動送信間隔：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		bSizer32.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox14Choices = [ u"0", u"100", u"500", u"1000", u"5000", u"10000" ]
		self.m_comboBox14 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, m_comboBox14Choices, wx.CB_READONLY )
		self.m_comboBox14.SetSelection( 0 )
		bSizer32.Add( self.m_comboBox14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"ms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer32.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button8 = wx.Button( self.m_panel5, wx.ID_ANY, u"選択した物を送信", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"※項目ダブルクリックで送信テキストフィールドに挿入", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer36.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		bSizer33.Add( self.m_listBox1, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer31 )
		self.m_panel5.Layout()
		bSizer31.Fit( self.m_panel5 )
		bSizer30.Add( self.m_panel5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.Send_Order )
		self.m_button8.Bind( wx.EVT_BUTTON, self.Send_Selection )
		self.m_listBox1.Bind( wx.EVT_LISTBOX, self.Txt_select )
		self.m_listBox1.Bind( wx.EVT_LISTBOX_DCLICK, self.Txt_execute )
		self.Bind( wx.EVT_TIMER, self.Auto_Send, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Send_Order( self, event ):
		event.Skip()
	
	def Send_Selection( self, event ):
		event.Skip()
	
	def Txt_select( self, event ):
		event.Skip()
	
	def Txt_execute( self, event ):
		event.Skip()
	
	def Auto_Send( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"なんやかんや通信する奴", pos = wx.DefaultPosition, size = wx.Size( 490,309 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox1 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"TCP/IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True) 
		bSizer8.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"ホスト：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer10.Add( self.m_staticText7, 0, wx.ALL, 3 )
		
		self.m_staticText8 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"サービス：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer10.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, wx.CB_DROPDOWN )
		bSizer12.Add( self.m_comboBox1, 0, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox3 = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"履歴を残す", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True) 
		bSizer15.Add( self.m_checkBox3, 0, wx.ALL, 5 )
		
		self.m_radioBtn5 = wx.RadioButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Telnet", wx.DefaultPosition, wx.DefaultSize, wx.RB_SINGLE )
		self.m_radioBtn5.SetValue( True ) 
		bSizer15.Add( self.m_radioBtn5, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"TCPポート：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer17.Add( self.m_staticText4, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetMaxLength( 5 ) 
		bSizer17.Add( self.m_textCtrl1, 1, wx.ALL|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer16.Add( bSizer17, 1, wx.ALIGN_RIGHT, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"SSHバージョン：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.Hide()
		
		bSizer18.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"まだむり", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl2.Hide()
		
		bSizer18.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer16.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"プロトコル：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.Hide()
		
		bSizer19.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox2Choices = [ u"UNSPEC", u"IPv6", u"IPv4" ]
		self.m_comboBox2 = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"UNSPEC", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		self.m_comboBox2.Hide()
		
		bSizer19.Add( self.m_comboBox2, 1, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_checkBox2 = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"シリアル", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"ポート", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		sbSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, wx.CB_READONLY )
		sbSizer3.Add( self.m_comboBox3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self.m_panel1, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self.m_panel1, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		self.m_sdbSizer1Help = wx.Button( self.m_panel1, wx.ID_HELP )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Help )
		m_sdbSizer1.Realize();
		
		bSizer2.Add( m_sdbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.Checked_IP )
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.IP_Set )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.Checked_Serial )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.Dialog_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Checked_IP( self, event ):
		event.Skip()
	
	def IP_Set( self, event ):
		event.Skip()
	
	def Checked_Serial( self, event ):
		event.Skip()
	
	def Dialog_ok( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 258,374 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 5, 10 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText26 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"COMポート", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer1.Add( self.m_staticText26, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox7Choices = [ u"COM1" ]
		self.m_comboBox7 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"COM1", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		fgSizer1.Add( self.m_comboBox7, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ボーレート", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer1.Add( self.m_staticText30, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox8Choices = [ u"50", u"75", u"110", u"134", u"150", u"200", u"300", u"600", u"1200", u"1800", u"2400", u"4800", u"9600", u"19200", u"38400", u"57600", u"115200" ]
		self.m_comboBox8 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"9600", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, 0 )
		self.m_comboBox8.SetSelection( 12 )
		fgSizer1.Add( self.m_comboBox8, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"データビット", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer1.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox9Choices = [ u"5", u"6", u"7", u"8" ]
		self.m_comboBox9 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, m_comboBox9Choices, 0 )
		self.m_comboBox9.SetSelection( 3 )
		fgSizer1.Add( self.m_comboBox9, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"パリティ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer1.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox10Choices = [ u"No", u"Odd", u"Even" ]
		self.m_comboBox10 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, m_comboBox10Choices, 0 )
		self.m_comboBox10.SetSelection( 0 )
		fgSizer1.Add( self.m_comboBox10, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ストップビット", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		fgSizer1.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox11Choices = [ u"1", u"1.5", u"2" ]
		self.m_comboBox11 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, m_comboBox11Choices, 0 )
		self.m_comboBox11.SetSelection( 0 )
		fgSizer1.Add( self.m_comboBox11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"フロー制御", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer1.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox12Choices = [ u"No", u"Hardware", u"Xon/Xoff" ]
		self.m_comboBox12 = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.DefaultSize, m_comboBox12Choices, 0 )
		self.m_comboBox12.SetSelection( 0 )
		fgSizer1.Add( self.m_comboBox12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"受信タイムアウト時間", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer1.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_spinCtrl1 = wx.SpinCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), wx.SP_ARROW_KEYS, 0, 50, 20 )
		fgSizer1.Add( self.m_spinCtrl1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		self.m_button61 = wx.Button( self.m_panel3, wx.ID_ANY, u"デフォルト", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button61, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel3, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer31.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer31 )
		self.m_panel3.Layout()
		bSizer31.Fit( self.m_panel3 )
		bSizer28.Add( self.m_panel3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer28 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button61.Bind( wx.EVT_BUTTON, self.option_reset )
		self.m_button6.Bind( wx.EVT_BUTTON, self.Serial_save )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def option_reset( self, event ):
		event.Skip()
	
	def Serial_save( self, event ):
		event.Skip()
	

