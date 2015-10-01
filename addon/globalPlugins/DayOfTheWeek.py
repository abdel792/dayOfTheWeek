# -*- coding: utf-8 -*-
# Allows you to find the day of the week corresponding to a choosen date
# Authors:
# Abdel <abdelkrim.bensaid@gmail.com>

import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import wx
import gui
import datetime
# Importing the SCRCAT_TOOLS category from the globalCommands module.
from globalCommands import SCRCAT_TOOLS

# The weekDays tuple
weekDays = (
	# Translators: A day of the week.
	_(u"Monday"),
	_(u"Tuesday"),
	_(u"Wednesday"),
	_(u"Thursday"),
	_(u"Friday"),
	_(u"Saturday"),
	_(u"Sunday")
	)

def getDayName(numberedDay=1):
	day = weekDays[numberedDay - 1]
	return day

def getDayOfWeek(iYear, iMonth, iDay):
	""" Returns the day of the week corresponding to the chosen date.
	@param1 : The year of the date.
	@param2 : The month of the date.
	@param3: The day of the date.
	"""
	d=datetime.datetime(int(iYear), int(iMonth), int(iDay))
	theDay = getDayName(d.isoweekday())
	return theDay

# Creating a dialog derived from wx.Dialog
class DateDialog(wx.Dialog):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if DateDialog._instance is None:
			return super(DateDialog, cls).__new__(cls, *args, **kwargs)
		return DateDialog._instance

	def __init__(self, parent, title):
		if DateDialog._instance is not None:
			return
		DateDialog._instance = self
		wx.Dialog.__init__(self, parent=parent, title=title)
		# Creating a BoxSizer
		dialogSizer=wx.BoxSizer(wx.VERTICAL)
		# Creating a DatePickerCtrl
		self.datePicker = wx.DatePickerCtrl(parent=self)
		searchButton = wx.Button(parent=self, label=_(u"&Get the day"), size=(175, 28))
		closeButton = wx.Button(parent=self, label=_(u"&Close"), id=wx.ID_CLOSE, size=(175, 28))
		# Adding the widgets in the sizer
		dialogSizer.Add(item=self.datePicker, proportion = 0,flag=wx.ALL, border=5)
		dialogSizer.Add(item=searchButton, proportion = 0, flag=wx.ALL, border=5)
		dialogSizer.Add(item=closeButton, proportion = 0, flag=wx.ALL, border=5)
		self.SetSizerAndFit(dialogSizer)
		self.Center

		# Events of actions
		searchButton.Bind(wx.EVT_BUTTON, self.onSearch)
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.onClose())
		closeButton.Bind(wx.EVT_BUTTON, self.onClose)
		self.EscapeId = wx.ID_CLOSE
		searchButton.SetDefault()

	def onSearch(self, evt):
		evt.Skip()
		msgBox=gui.messageBox(message=getDayOfWeek(str(self.datePicker.GetValue()).split("/")[2].split()[0], str(self.datePicker.GetValue()).split("/")[1], str(self.datePicker.GetValue()).split("/")[0]), caption=_(u"Your day"), style=wx.OK|wx.ICON_INFORMATION)
		# Translators: To not close the dialog after closing the msgBox.
		return

	def onClose(self, evt):
		evt.Skip()
		self.Destroy()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.createSubMenu()

	def createSubMenu(self):
		""" Adds a subMenu in the tools menu for the day of the week
		"""
		self.sub_menu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Items in the tools menu for the Addon dayOfTheWeek.
		self.dayOfTheWeek = self.sub_menu.Append(wx.ID_ANY, _(u"&Day of the week..."), _(u"Displays the dialog box to search a day corresponding to a chosen date"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.showDialog, self.dayOfTheWeek)

	def showDialog(self, evt):
		""" Create the dialog box to search the day of the week
		"""
		dlg = DateDialog(parent = gui.mainFrame, title=_(u"Choose a date"))
		dlg.Show(True)

	def script_activateDayOfTheWeekDialog(self, gesture):
		wx.CallAfter(self.showDialog, None)
	# documentation:
	script_activateDayOfTheWeekDialog.__doc__ = _(u"Allows you to find the day of the week corresponding to a choosen date")
	script_activateDayOfTheWeekDialog.category = SCRCAT_TOOLS
