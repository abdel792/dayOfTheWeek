# -*- coding: utf-8 -*-
# Allows you to find the day of the week corresponding to a chosen date
# Authors:
# Abdel <abdelkrim.bensaid@gmail.com>
# Noelia <nrm1977@gmail.com>

import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import wx
import gui
# Importing the SCRCAT_TOOLS category from the globalCommands module.
from globalCommands import SCRCAT_TOOLS

class DateDialog(wx.Dialog):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if DateDialog._instance is None:
			return super(DateDialog, cls).__new__(cls, *args, **kwargs)
		return DateDialog._instance

	def __init__(self, parent):
		if DateDialog._instance is not None:
			return
		DateDialog._instance = self
		# Translators: The title of the Date Dialog.
		super(DateDialog,self).__init__(parent,title=_("Get the day of the week"))
		dialogSizer=wx.BoxSizer(wx.VERTICAL)
		# Translators: A label for a list in a dialog.
		datesLabel=wx.StaticText(self,-1,label=_("Type or select a date"))
		dialogSizer.Add(datesLabel)
		self.datePicker = wx.DatePickerCtrl(self)
		dialogSizer.Add(item=self.datePicker, proportion = 0,flag=wx.ALL, border=5)
		dialogSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.datePicker.Bind(wx.EVT_CHAR, self.onListChar)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		dialogSizer.Fit(self)
		self.SetSizer(dialogSizer)
		self.datePicker.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def __del__(self):
		DateDialog._instance = None

	def onListChar(self, evt):
		if evt.KeyCode == wx.WXK_SPACE:
			# Activate the OK button.
			self.ProcessEvent(wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK))
		else:
			evt.Skip()

	def onOk(self, evt):
		date = self.datePicker.GetValue()
		weekDay = date.Format("%A")
		msgBox=gui.messageBox(
		message=weekDay,
		# Translators: The title of a dialog.
		caption=_("Your day"),
		style=wx.OK|wx.ICON_INFORMATION)

	def onCancel(self, evt):
		self.Destroy()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.createSubMenu()

	def createSubMenu(self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		# Translators: Item in the tools menu for the Addon dayOfTheWeek.
		self.dayOfTheWeek = self.toolsMenu.Append(wx.ID_ANY, _("&Day of the week..."),
		"")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onDateDialog, self.dayOfTheWeek)

	def terminate(self):
		try:
			self.toolsMenu.RemoveItem(self.dayOfTheWeek)
		except wx.PyDeadObjectError:
			pass

	def onDateDialog(self, evt):
		if gui.isInMessageBox:
			return
		gui.mainFrame.prePopup()
		d=DateDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_activateDayOfTheWeekDialog(self, gesture):
		wx.CallAfter(self.onDateDialog, gui.mainFrame)
	# Translators: Message presented in input help mode.
	script_activateDayOfTheWeekDialog.__doc__ = _("Allows you to find the day of the week corresponding to a chosen date.")
	script_activateDayOfTheWeekDialog.category = SCRCAT_TOOLS
