# -*- coding: UTF-8 -*-

# globalPlugins/dayOfTheWeek.py.
# Allows you to find the day of the week corresponding to a chosen date

#Copyright (C) 2015-2017 Abdel <abdelkrim.bensaid@gmail.com>, Noelia <nrm1977@gmail.com>
# Released under GPL 2
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

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

weekDays = {
	# Translators: a day of the week.
	"0": _("Sunday"),
	# Translators: a day of the week.
	"1": _("Monday"),
	# Translators: a day of the week.
	"2": _("Tuesday"),
	# Translators: a day of the week.
	"3": _("Wednesday"),
	# Translators: a day of the week.
	"4": _("Thursday"),
	# Translators: a day of the week.
	"5": _("Friday"),
	# Translators: a day of the week.
	"6": _("Saturday"),
	}

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
		mainSizer=wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: A label for a list in a dialog.
		dateLabel = _("Type or select a date")
		sHelper.addItem(wx.StaticText(self, label=dateLabel))
		self.datePicker = sHelper.addItem(wx.DatePickerCtrl(self))
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.datePicker.Bind(wx.EVT_CHAR, self.onListChar)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
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
		weekDay = weekDays[date.Format("%w")]
		msgBox=gui.messageBox(
		message=weekDay,
		# Translators: The title of a dialog.
		caption=_("Your day"),
		style=wx.OK|wx.ICON_INFORMATION)

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
		gui.mainFrame.prePopup()
		d=DateDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_activateDayOfTheWeekDialog(self, gesture):
		wx.CallAfter(self.onDateDialog, gui.mainFrame)
	# Translators: Message presented in input help mode.
	script_activateDayOfTheWeekDialog.__doc__ = _("Allows you to find the day of the week corresponding to a chosen date.")
	script_activateDayOfTheWeekDialog.category = SCRCAT_TOOLS
