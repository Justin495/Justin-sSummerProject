# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Precipitation Vs. Discharge", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Made By: Justin Caniglia", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer3.Add( self.m_datePicker1, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Ending Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_datePicker2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer3.Add( self.m_datePicker2, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Discharge", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_datePicker4 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer4.Add( self.m_datePicker4, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Ending Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_datePicker3 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer4.Add( self.m_datePicker3, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Precip", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel_discharge = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_discharge.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer5.Add( self.m_panel_discharge, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel_precip = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_precip.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer5.Add( self.m_panel_precip, 1, wx.EXPAND |wx.ALL, 5 )

        m_radioBox1Choices = [ u"Daily", u"Monthly", u"Annually" ]
        self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer5.Add( self.m_radioBox1, 0, wx.ALL, 5 )

        m_radioBox3Choices = [ u"Daily", u"Monthly", u"Annually" ]
        self.m_radioBox3 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox3.SetSelection( 0 )
        bSizer5.Add( self.m_radioBox3, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel_both = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_both.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer6.Add( self.m_panel_both, 1, wx.EXPAND |wx.ALL, 5 )

        m_radioBox2Choices = [ u"Daily", u"Monthly", u"Annually" ]
        self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox2.SetSelection( 0 )
        bSizer6.Add( self.m_radioBox2, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )
        

        #from matplot import second figure
        #FIGURE TWO Y-AXIS
        self.m_panel_both.figure = matplotlib.figure.Figure()
        self.axes_both = self.m_panel_both.figure.add_subplot(111)       
        self.canvas_both = FigureCanvas(self.m_panel_both, -1, self.m_panel_both.figure)
  
               
        #from matplot import second figure
        #FIGURE DISCHARGE
        self.m_panel_discharge.figure = matplotlib.figure.Figure()
        self.axes_discharge = self.m_panel_discharge.figure.add_subplot(111)
        self.canvas_discharge = FigureCanvas(self.m_panel_discharge, -1, self.m_panel_discharge.figure)
  
        
        #from matplot import second figure
        #FIGURE PRECIPITATION
        self.m_panel_precip.figure = matplotlib.figure.Figure()
        self.axes_precip = self.m_panel_precip.figure.add_subplot(111)
        self.canvas_precip = FigureCanvas(self.m_panel_precip, -1, self.m_panel_precip.figure) 

        # Connect Events
        self.m_datePicker1.Bind( wx.adv.EVT_DATE_CHANGED, self.startingdate1 )
        self.m_datePicker2.Bind( wx.adv.EVT_DATE_CHANGED, self.endingdate1 )
        self.m_button1.Bind( wx.EVT_BUTTON, self.downloadUSGS )
        self.m_datePicker4.Bind( wx.adv.EVT_DATE_CHANGED, self.startingdate2 )
        self.m_datePicker3.Bind( wx.adv.EVT_DATE_CHANGED, self.endingdate2 )
        self.m_button2.Bind( wx.EVT_BUTTON, self.downloadPrecip )
        self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.changeFreq )
        self.m_radioBox3.Bind( wx.EVT_RADIOBOX, self.changeFreq2 )
        self.m_radioBox2.Bind( wx.EVT_RADIOBOX, self.changeFreq1 )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def startingdate1( self, event ):
        event.Skip()

    def endingdate1( self, event ):
        event.Skip()

    def downloadUSGS( self, event ):
        event.Skip()

    def startingdate2( self, event ):
        event.Skip()

    def endingdate2( self, event ):
        event.Skip()

    def downloadPrecip( self, event ):
        event.Skip()

    def changeFreq( self, event ):
        event.Skip()

    def changeFreq2( self, event ):
        event.Skip()

    def changeFreq1( self, event ):
        event.Skip()

#Need to Develop Code to Control Starting and Ending Dates!!! v
    def startingdate1( self, event ):
        event.Skip()

    def endingdate1( self, event ):
        event.Skip()

    def startingdate2( self, event ):
        event.Skip()

    def endingdate2( self, event ):
        event.Skip()

# USGS CODE # Use GAUGE 01124151
## Check to make sure USGS Sation ID is in Discharge URL
# Virtual event handlers, overide them in your derived class
    def downloadUSGS( self, event ):
        #gauge_list = [self.m_textCtrl.GetValue()]
        gages = ('&site_no={}'.format(self.m_textCtrl2.GetValue()))
        #period = '&period=&begin_date={}&end_date={}'.format(self.startingdate1, self.endingdate1)
        period = '&period=&begin_date={}&end_date={}'.format('2000-01-01', '2019-12-31')
        url = 'https://waterdata.usgs.gov/nwis/dv?&cb_00060=on&format=rdb{}&referred_module=sw{}'.format(gages, period)  
        #self.axes.plot([1, 2], [3, 4])
        self.dataflow = pd.read_csv(url, comment='#', header=0, sep='\t')[1:].apply(lambda x: pd.to_numeric(x, errors='ignore') if x.name.endswith('_va') else x, axis=0)
        print(self.dataflow.set_index('datetime').columns)
        
        pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2]).plot(ax=self.axes_discharge)
        self.canvas = FigureCanvas(self.m_panel_discharge, -1, self.m_panel_discharge.figure)
        
        ser1 = pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2])
        ser1.plot(ax=self.axes_both)
        self.axes_both.set_ylabel('Discharge')
        self.m_panel_both.figure.tight_layout()
        self.canvas_both.draw()
        

    def changeFreq( self, event ):
        self.axes_discharge.clear()
        rID = event.GetInt()
        df =  pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2])
        df.index = pd.DatetimeIndex(df.index)
        if rID == 0:
          df.plot(ax= self.axes_discharge)
        elif rID == 1:
          df.resample('M').mean().plot(ax=self.axes_discharge)
        else:
          df.resample('A').mean().plot(ax=self.axes_discharge)
        self.canvas = FigureCanvas(self.m_panel_discharge, -1, self.m_panel_discharge.figure)
        


# USGS CODE # Use GAUGE 0208732885 or 01104430 
#USGS Precipitation Code
## Check to make sure USGS Station ID is in Precip URL
    def downloadPrecip( self, event ):
        #gauge_list = [self.m_textCtrl.GetValue()]
        gages = ('&site_no={}'.format(self.m_textCtrl3.GetValue()))
        period = '&period=&begin_date={}&end_date={}'.format('2000-01-01', '2019-12-31')
        #period = '&period=&begin_date={}&end_date={}'.format(self.startingdate2, self.endingdate2)
        url1 = 'https://waterdata.usgs.gov/nwis/dv?&cb_00045=on&format=rdb{}&referred_module=sw{}'.format(gages, period)  
        #self.axes.plot([1, 2], [3, 4])
        
        self.rainflow = pd.read_csv(url1, comment='#', header=0, sep='\t')[1:].apply(lambda x: pd.to_numeric(x, errors='ignore') if x.name.endswith('_va') else x, axis=0)
        print(self.rainflow.set_index('datetime').columns)
        
        pd.to_numeric(self.rainflow.set_index('datetime').iloc[:, 2]).plot(ax=self.axes_precip)
        self.canvas = FigureCanvas(self.m_panel_precip, -1, self.m_panel_precip.figure)
        
        ser2 = pd.to_numeric(self.rainflow.set_index('datetime').iloc[:, 2])
        ax1 = self.axes_both.twinx()
        ser2.plot.bar(ax=ax1, color='C1', alpha=0.5)
        ax1.invert_yaxis()
        ax1.set_ylabel('Precip')
        self.m_panel_both.figure.tight_layout()
        self.canvas_both.draw()
        
        
    def changeFreq2( self, event ):
        self.axes_precip.clear()
        rID = event.GetInt()
        df =  pd.to_numeric(self.rainflow.set_index('datetime').iloc[:, 2])
        df.index = pd.DatetimeIndex(df.index)
        if rID == 0:
          df.plot(ax= self.axes_precip)
        elif rID == 1:
          df.resample('M').mean().plot(ax=self.axes_precip)
        else:
          df.resample('A').mean().plot(ax=self.axes_precip)
        self.canvas = FigureCanvas(self.m_panel_precip, -1, self.m_panel_precip.figure)
        

        
    def changeFreq1( self, event ):
        self.axes_both.clear()
        rID = event.GetInt()
        df =  pd.to_numeric(self.rainflow.set_index('datetime').iloc[:, 2])
        df =  pd.to_numeric(self.dataflow.set_index('datetime').iloc[:, 2])
        df.index = pd.DatetimeIndex(df.index)
        if rID == 0:
          df.plot(ax= self.axes_both)
        elif rID == 1:
          df.resample('M').mean().plot(ax=self.axes_both)
        else:
          df.resample('A').mean().plot(ax=self.axes_both)
        self.canvas = FigureCanvas(self.m_panel_both, -1, self.m_panel_both.figure)

        
#https://wcc.sc.egov.usda.gov/nwcc/site?sitenum=2001 maybe use this for climate data


app = wx.App(redirect=True)
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
