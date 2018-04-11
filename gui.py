# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"NovaManger"), pos = wx.DefaultPosition, size = wx.Size( 563,724 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"下机单导入") ), wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"导入文件") ), wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"上传下机单"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		sbSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer2.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"批量导入") ), wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"下机单目录"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		sbSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer3.Add( self.m_dirPicker1, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"过滤条件") ), wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"信息分析师"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		sbSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_toggleBtn2 = wx.ToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"开始上传"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_toggleBtn2, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"生成配置文件") ), wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"信息收集表") ), wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, _(u"选择信息收集表"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		sbSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_filePicker2 = wx.FilePickerCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer6.Add( self.m_filePicker2, 0, wx.ALL, 5 )
		
		self.m_toggleBtn3 = wx.ToggleButton( sbSizer6.GetStaticBox(), wx.ID_ANY, _(u"Check"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_toggleBtn3, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer6, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"选项") ), wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"测序策略"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		sbSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"期号"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		sbSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		sbSizer7.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer7, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"选项") ), wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, _(u"疾病名"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		sbSizer15.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, _(u"DOID"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		sbSizer15.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, _(u"试剂盒"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		sbSizer15.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer15, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"选项") ), wx.HORIZONTAL )
		
		self.m_checkBox1 = wx.CheckBox( sbSizer9.GetStaticBox(), wx.ID_ANY, _(u"南京集群"), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, _(u"分析序列"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		sbSizer9.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_textCtrl81 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_textCtrl81, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer3, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_toggleBtn21 = wx.ToggleButton( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"生成文件"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn21.SetValue( True ) 
		sbSizer5.Add( self.m_toggleBtn21, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( sbSizer5, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_toggleBtn2.Bind( wx.EVT_TOGGLEBUTTON, self.upload_to_db )
		self.m_toggleBtn3.Bind( wx.EVT_TOGGLEBUTTON, self.check_info )
		self.m_toggleBtn21.Bind( wx.EVT_TOGGLEBUTTON, self.generate_config )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def upload_to_db( self, event ):
		event.Skip()
	
	def check_info( self, event ):
		event.Skip()
	
	def generate_config( self, event ):
		event.Skip()
	

