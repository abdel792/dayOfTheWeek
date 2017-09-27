# -*- coding: UTF-8 -*-

# globalPlugins/dayOfTheWeek.py.

# Allows you to find the day of the week corresponding to a chosen date

#Copyright (C) 2015-2017 Abdel <abdelkrim.bensaid@gmail.com>, Noelia <nrm1977@gmail.com>
# Released under GPL 2
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import speech
import time
import keyboardHandler
import api
import controlTypes
import wx
import gui
from NVDAObjects.IAccessible import IAccessible

# Importing the SCRCAT_TOOLS category from the globalCommands module.
from globalCommands import SCRCAT_TOOLS

fieldLabels = (
	# Translators: The label of the days field.
	_("You can select a day with the vertical arrows"),
	# Translators: The label of the months field.
	_("You can select a month with the vertical arrows"),
	# Translators: The label of the years field.
	_("You can select a year with the vertical arrows")
)

curDateField = 0
oldSpeechMode = speech.speechMode

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
		import ctypes
		date = self.datePicker.GetValue()
		weekDay = date.Format("%A")
		msgBox=gui.messageBox(
		message=weekDay,
		# Translators: The title of a dialog.
		caption=_("Your day"),
		style=wx.OK|wx.ICON_INFORMATION)

class MyDayOfWeek (IAccessible):

	def event_gainFocus (self):
		global curDateField
		speech.speakObject (self, reason=controlTypes.REASON_FOCUS)
		if curDateField== 0: curDateField += 1
		self.sayField (curDateField)

	def sayField (self, columnID):
		fieldID = columnID - 1
		speech.speakMessage (fieldLabels[fieldID])

	def whatChanged (self, val1, val2):
		global curDateField
		val1 = val1.split("/")
		val2 = val2.split("/")
		if val1[0] != val2[0]:
			curDateField = 1
		if val1[1] != val2[1]:
			curDateField = 2
		if val1[2] != val2[2]:
			curDateField = 3
		self.sayField (curDateField)

	def script_nextField (self, gesture):
		val1 = self.value
		increment = 0
		gesture.send()
		# I know it is not correct to do this, but we can't do otherwise.
		speech.speechMode = speech.speechMode_off
		keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send()
		increment = 1
		api.processPendingEvents()
		val2 = self.value
		# We verify that we are not on the last value
		if val1 == val2:
			# In this case, we move to the previous value.
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send()
			increment = -1
			api.processPendingEvents()
		# We restore the value of the current date.
		if increment == -1:
			keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send()
			api.processPendingEvents()
		if increment == 1:
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send()
			api.processPendingEvents()
		speech.speechMode = oldSpeechMode
		self.whatChanged (val1, val2)

	def script_previousField (self, gesture):
		val1 = self.value
		increment = 0
		gesture.send()
		# I know it is not correct to do this, but we can't do otherwise.
		speech.speechMode = speech.speechMode_off
		keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send()
		increment = 1
		api.processPendingEvents()
		val2 = self.value
		# We verify that we are not on the last value
		if val1 == val2:
			# In this case, we move to the previous value.
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send()
			increment = -1
			api.processPendingEvents()
		# We restore the value of the current date.
		if increment == -1:
			keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send()
			api.processPendingEvents()
		if increment == 1:
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send()
			api.processPendingEvents()
		speech.speechMode = oldSpeechMode
		self.whatChanged (val1, val2)

	__gestures={
		"kb:leftArrow":"previousField",
		"kb:rightArrow":"nextField"
	}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.createSubMenu()

	def chooseNVDAObjectOverlayClasses (self, obj, clsList):
		if obj.value and obj.role == controlTypes.ROLE_DROPLIST and len(obj.value) == 10 and "/" in obj.value:
			clsList.insert (0, MyDayOfWeek)

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
