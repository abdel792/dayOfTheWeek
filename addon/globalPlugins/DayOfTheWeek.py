# -*- coding: utf-8 -*-
from __future__ import unicode_literals # To ensure coding compatibility with python 2 and 3.

# globalPlugins/dayOfTheWeek.py.

# Allows you to find the day of the week corresponding to a chosen date

#Copyright (C) 2015-2017 Abdel <abdelkrim.bensaid@gmail.com>, Noelia <nrm1977@gmail.com>
# Released under GPL 2
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
addonHandler.initTranslation ()
import globalPluginHandler
import re
import speech
from logHandler import log
import keyboardHandler
import api
import os
import controlTypes
import wx
import gui
from NVDAObjects.IAccessible import IAccessible
import config

# This block ensures compatibility with NVDA versions prior to 2018.2 which includes the settings panel.
try:
	from gui import SettingsPanel as SettingsDialog
except ImportError:
	from gui.settingsDialogs import SettingsDialog


### Constants
ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]
ADDON_NAME = addonHandler.getCodeAddon ().manifest["name"]

fieldLabels = (
	# Translators: The long label of the days field.
	(_("You can select a day with the vertical arrows"),
	# Translators: The short label of the days field.
	_("Select a day")),
	# Translators: The long label of the months field.
	(_("You can select a month with the vertical arrows"),
	# Translators: The short label of the months field.
	_("Select a month")),
	# Translators: The long label of the years field.
	(_("You can select a year with the vertical arrows"),
	# Translators: The short label of the years field.
	_("Select a year"))
)

# The following dictionary was created to list the Georgian days that are not recognized by the %A format, this technique will be improved if other languages ??encounter the same problem.
# Other localization messages for the Georgian language can be translated by the NVDA translation team.

georgianDays = {
	"0" : "კვირა",
	"1" : "ორშაბათი",
	"2" : "სამშაბათი",
	"3" : "ოთხშაბათი",
	"4" : "ხუთშაბათი",
	"5" : "პარასკევი",
	"6" : "შაბათი"
}

curDateField = 0

confSpec = {
	"enableAnnounces" : "boolean(default = True)",
	"labelAnnounceLevel" : "string(default = long)",
	"reportFieldsValuesWhenMovingVertically" : "boolean(default = False)"
	}
config.conf.spec["dayOfWeek"] = confSpec

def isDatepickerDate (value):
	"""
	This function makes it possible to check whether the date format matches to be able to affect our overlay class.
	"""
	ptrn = "^[\d]{1,4}[/\.-][\da-zA-Z]{1,3}[/\.-][\d]{1,4}[/\.-]?$"
	rg = re.compile (ptrn)
	return bool (rg.match (value))

class DateDialog (wx.Dialog):

	_instance = None

	def __new__ (cls, *args, **kwargs):
		if DateDialog._instance is None:
			return super (DateDialog, cls).__new__(cls, *args, **kwargs)
		return DateDialog._instance

	def __init__ (self, parent):
		if DateDialog._instance is not None:
			return
		DateDialog._instance = self
		# Translators: The title of the Date Dialog.
		dlgTitle = _("Get the day of the week")
		super (DateDialog,self).__init__(parent,title = dlgTitle)
		self.mainSizer = wx.BoxSizer (wx.VERTICAL)
		# Translators: A label for a list in a dialog.
		self.dateLabel = _("Type or select a date")
		# This try/except/else block has been added to ensure the compatibility of the add-on with the NVDA versions that preceded version 2016.4, which included the gui.guiHelper module.
		try:
			import gui.guiHelper
		except ImportError:
			self.showDateDialog ()
		else:
			self.showDateDialogForGuiHelper ()

	def showDateDialogForGuiHelper (self):
		sHelper = gui.guiHelper.BoxSizerHelper (self, orientation = wx.VERTICAL)
		sHelper.addItem (wx.StaticText (self, label = self.dateLabel))
		try:
			# for wx version 4.0.
			self.datePicker = sHelper.addItem (wx.adv.DatePickerCtrl (self))
		except AttributeError:
			# for wx version 3.0.
			self.datePicker = sHelper.addItem (wx.DatePickerCtrl (self))
		sHelper.addDialogDismissButtons (self.CreateButtonSizer (wx.OK|wx.CANCEL))
		self.datePicker.Bind (wx.EVT_CHAR, self.onListChar)
		self.Bind (wx.EVT_BUTTON, self.onOk, id = wx.ID_OK)
		self.mainSizer.Add (sHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag = wx.ALL)
		self.Sizer = self.mainSizer
		self.mainSizer.Fit (self)
		self.datePicker.SetFocus ()
		self.Center (wx.BOTH | wx.CENTER)

	def showDateDialog (self):
		datesLabel = wx.StaticText(self,-1,label=self.dateLabel)
		self.mainSizer.Add (datesLabel)
		self.datePicker = wx.DatePickerCtrl (self)
		self.mainSizer.Add (item = self.datePicker, proportion = 0,flag=wx.ALL, border = 5)
		self.mainSizer.Add (self.CreateButtonSizer (wx.OK | wx.CANCEL))
		self.datePicker.Bind (wx.EVT_CHAR, self.onListChar)
		self.Bind (wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.mainSizer.Fit (self)
		self.SetSizer (self.mainSizer)
		self.datePicker.SetFocus ()
		self.Center (wx.BOTH | wx.CENTER_ON_SCREEN)

	def __del__ (self):
		DateDialog._instance = None

	def onListChar (self, evt):
		if evt.KeyCode == wx.WXK_SPACE:
			# Activate the OK button.
			self.ProcessEvent (wx.CommandEvent (wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK))
		else:
			evt.Skip ()

	def onOk (self, evt):
		import languageHandler
		curNVDALang = languageHandler.getLanguage ()
		date = self.datePicker.GetValue ()
		weekDay = date.Format ("%A") if not curNVDALang == "ka" else georgianDays[date.Format ("%w")]
		msgBox = gui.messageBox (
		message = weekDay,
		# Translators: The title of a dialog.
		caption = _("Your day"),
		style = wx.OK|wx.ICON_INFORMATION)

class DayOfWeekSettingsDialog (SettingsDialog):

	# Translators: The title of the add-on configuration dialog box.
	title = _("Configuration of the addon {0}").format (ADDON_NAME) if not hasattr (gui, "NVDASettingsDialog") else _("Day of the week")
	LABEL_ANNOUNCE_LEVELS = (
		("short",
		# Translators: Level for short announces of labels.
		_("Short")),
		("long",
		# Translators: Level for long announces of labels.
		_("Long")),
		("off",
		# Translators: Level to disable announces of labels.
		_("Off"))
	)

	def makeSettings (self, settingsSizer):
		# Translators: The label of the checkbox to enable or disable the date selector accessibility.
		self.enableAnnounces = _("En&able the accessibility of the date selector:")
		# Translators: The label for an item to select the level of the announces of labels (short, long or disabled).
		self.labelAnnounceLevelText = _("Level of the announces of &labels:")
		# Translators: The label of the checkbox to enable or disable the current date field value only announcement when moving vertically.
		self.valueAnnounce = _("Enable announcements of the current date field value only, when moving &vertically:")
		# This try/except/else block has been added to ensure the compatibility of the add-on with the NVDA versions that preceded version 2016.4, which included the gui.guiHelper module.
		try:
			import gui.guiHelper
		except ImportError:
			self.showSettingsDialog (settingsSizer = settingsSizer)
		else:
			self.showSettingsDialogForGuiHelper (settingsSizer = settingsSizer)

	def showSettingsDialogForGuiHelper (self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper (self, sizer = settingsSizer)
		self.enableAnnouncesCheckBox = wx.CheckBox (self, label = self.enableAnnounces)
		self.enableAnnouncesCheckBox.SetValue (config.conf["dayOfWeek"]["enableAnnounces"])
		settingsSizerHelper.addItem (self.enableAnnouncesCheckBox)

		labelAnnounceLevelChoices = [name for level, name in self.LABEL_ANNOUNCE_LEVELS]
		self.labelAnnounceLevelsList = settingsSizerHelper.addLabeledControl(self.labelAnnounceLevelText, wx.Choice, choices = labelAnnounceLevelChoices)
		curLevel = config.conf["dayOfWeek"]["labelAnnounceLevel"]
		for index, (level, name) in enumerate(self.LABEL_ANNOUNCE_LEVELS):
			if level == curLevel:
				self.labelAnnounceLevelsList.SetSelection(index)
				break
		self.labelAnnounceLevelsList.Enabled = self.enableAnnouncesCheckBox.IsChecked ()

		self.reportDateFieldValuesCheckBox = wx.CheckBox (self, label = self.valueAnnounce)
		self.reportDateFieldValuesCheckBox.SetValue (config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"])
		settingsSizerHelper.addItem (self.reportDateFieldValuesCheckBox)
		self.reportDateFieldValuesCheckBox.Enabled = self.enableAnnouncesCheckBox.IsChecked ()
		self.enableAnnouncesCheckBox.Bind (wx.EVT_CHECKBOX, self.onCheckAnnounces)

	def showSettingsDialog (self, settingsSizer):
		dialogSizer = wx.BoxSizer (wx.VERTICAL)
		self.enableAnnouncesCheckBox = wx.CheckBox (self, label = self.enableAnnounces)
		self.enableAnnouncesCheckBox.SetValue (config.conf["dayOfWeek"]["enableAnnounces"])
		dialogSizer.Add (self.enableAnnouncesCheckBox)

		labelAnnounceLevelChoices = [name for level, name in self.LABEL_ANNOUNCE_LEVELS]
		labelAnnounce = wx.StaticText (self,label=self.labelAnnounceLevelText)
		dialogSizer.Add (labelAnnounce)
		self.labelAnnounceLevelsList = wx.Choice (self, choices = labelAnnounceLevelChoices)
		curLevel = config.conf["dayOfWeek"]["labelAnnounceLevel"]
		for index, (level, name) in enumerate(self.LABEL_ANNOUNCE_LEVELS):
			if level == curLevel:
				self.labelAnnounceLevelsList.SetSelection(index)
				break
		dialogSizer.Add (self.labelAnnounceLevelsList)
		self.labelAnnounceLevelsList.Enabled = self.enableAnnouncesCheckBox.IsChecked ()

		self.reportDateFieldValuesCheckBox = wx.CheckBox (self, label = self.valueAnnounce)
		self.reportDateFieldValuesCheckBox.SetValue (config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"])
		dialogSizer.Add (self.reportDateFieldValuesCheckBox)
		settingsSizer.Add (dialogSizer, border=10, flag=wx.BOTTOM)
		self.reportDateFieldValuesCheckBox.Enabled = self.enableAnnouncesCheckBox.IsChecked ()
		self.enableAnnouncesCheckBox.Bind (wx.EVT_CHECKBOX, self.onCheckAnnounces)

	def postInit (self):
		self.enableAnnouncesCheckBox.SetFocus ()

	def onCheckAnnounces (self, event):
		if self.enableAnnouncesCheckBox.IsChecked ():
			self.labelAnnounceLevelsList.Enable ()
			self.reportDateFieldValuesCheckBox.Enable ()
		else:
			self.labelAnnounceLevelsList.Disable ()
			self.reportDateFieldValuesCheckBox.Disable ()

	def onOk (self, evt):
		config.conf["dayOfWeek"]["enableAnnounces"] = self.enableAnnouncesCheckBox.GetValue ()
		labelAnnounceLevel = self.LABEL_ANNOUNCE_LEVELS[self.labelAnnounceLevelsList.GetSelection()][0]
		config.conf["dayOfWeek"]["labelAnnounceLevel"] = labelAnnounceLevel
		config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"] = self.reportDateFieldValuesCheckBox.GetValue ()
		super (DayOfWeekSettingsDialog, self).onOk (evt)

	def onSave (self):
		config.conf["dayOfWeek"]["enableAnnounces"] = self.enableAnnouncesCheckBox.GetValue ()
		labelAnnounceLevel = self.LABEL_ANNOUNCE_LEVELS[self.labelAnnounceLevelsList.GetSelection()][0]
		config.conf["dayOfWeek"]["labelAnnounceLevel"] = labelAnnounceLevel
		config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"] = self.reportDateFieldValuesCheckBox.GetValue ()

class AnnounceFieldsLabels (IAccessible):

	increment = 0
	vertical = 0
	vMovementKeys = (
		"kb:upArrow",
		"kb:downArrow",
		"kb:home",
		"kb:end"
	)
	hMovementKeys = (
		"kb:leftArrow",
		"kb:rightArrow"
	)

	def initOverlayClass (self):
		for vKey in self.vMovementKeys:
			self.bindGesture (vKey, "verticalMovements")
		for hKey in self.hMovementKeys:
			self.bindGesture (hKey, "horizontalMovements")

	def event_gainFocus (self):
		global curDateField
		super (AnnounceFieldsLabels, self).event_gainFocus ()
		if curDateField == 0: curDateField += 1
		self.calculateCurField ()

	def event_valueChange (self):
		if self.increment:
			return
		super (AnnounceFieldsLabels, self).event_valueChange ()

	def isUS (self):
		import locale
		if "US" in locale.getdefaultlocale ()[0]:
			return True
		return False

	def sayField (self, curValue, columnID = None):
		import ui
		labelAnnounce = ""
		if columnID:
			if config.conf["dayOfWeek"]["labelAnnounceLevel"] != "off":
				if config.conf["dayOfWeek"]["labelAnnounceLevel"] == "long":
					labelAnnounce = fieldLabels[columnID - 1][0]
				else:
					labelAnnounce = fieldLabels[columnID - 1][1]
		field = "{0}, {1}".format (curValue, labelAnnounce) if columnID else curValue
		ui.message (field)

	def getDelimiter (self, value):
		ptrn = "^[\d]{1,4}([\./-]).+$"
		rg = re.compile (ptrn)
		return rg.match (value).group (1)

	def whatChanged (self, val1, val2):
		global curDateField
		isYear = False
		isMonth = False
		isMonthUS = False
		val1 = val1.split (self.getDelimiter (val1))
		val2 = val2.split (self.getDelimiter (val2))
		# To fix a bug with the year 1601, we are forced to initialize the value of curValue to 1601
		curValue = "1601"
		if val1[0] != val2[0]:
			# We're in the day, month or year field.
			curValue = val1[0]
			if self.isUS () and len (val1[2]) == 4 and len (val1[1]) < 3:
				# We're in the month field for US layout.
				isMonthUS = True
				curDateField = 2
				# Here is a technique to fix the problem when switching to shorter months.
				# Since the calculation function executes a down arrow and an up arrow to find the value of the current month, it often switches to shorter months, which changes the value of the day.
				# The following if block is for the common years, where the February month is 28 days.
				if val2[1] == "28":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
					elif val1[1] == "30":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
					elif val1[1] == "29":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
				# The following elif block is for the leap years, where the February month is 29 days.
				elif val2[1] == "29":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
					elif val1[1] == "30":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
				# The following elif block is for the 30-day months.
				elif val2[1] == "30":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
						keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
						api.processPendingEvents ()
			else:
				curDateField = 3 if len (curValue) == 4 else 1
				if len (curValue) == 4:
					isYear = True
					# For the year field only.
					# Here is a technique to fix the problem when switching to shorter years, for instance, when switching from a leap year to a common year.
					# Since the calculation function executes a down arrow and an up arrow to find the value of the current year, it sometimes switches to shorter years, which changes the value of the day field in February month.
					if val2[2] == "28":
						if val1[2] == "29" and val1[1] in ["2", "02"]:
							keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
							api.processPendingEvents ()
		if val1[1] != val2[1]:
			# We're in the month or day field.
			if not isMonthUS and not isYear:
				curValue = val1[1]
				curDateField = 1 if self.isUS () and len (curValue) < 3 and len (val1[2]) == 4 else 2
				if curDateField == 2:
					isMonth = True
					# Here is a technique to fix the problem when switching to shorter months.
					# Since the calculation function executes a down arrow and an up arrow to find the value of the current month, it often switches to shorter months, which changes the value of the day.
					# The following if block is for the common years, where the February month is 28 days.
					if any (x == "28" for x in [val2[0], val2[2]]):
						if any (x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
						elif any (x == "30" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
						elif any (x == "29" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
					# The following elif block is for the leap years, where the February month is 29 days.
					elif any (x == "29" for x in [val2[0], val2[2]]):
						if any (x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
						elif any (x == "30" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
					# The following elif block is for the 30-day months.
					elif any (x == "30" for x in [val2[0], val2[2]]):
						if any (x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight (value = val1[0], flag = True)
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							self.leftOrRight (value = val1[0])
							api.processPendingEvents ()
		if val1[2] != val2[2]:
			# We're in the year or the day field.
			if not isYear and not isMonth:
				curDateField = 3 if len (val1[2]) == 4 else 1
				curValue = val1[2]
				# For the year field only.
				if len (curValue) == 4:
					# Here is a technique to fix the problem when switching to shorter years, for instance, when switching from a leap year to a common year.
					# Since the calculation function executes a down arrow and an up arrow to find the value of the current year, it sometimes switches to shorter years, which changes the value of the day field in February month.
					if any (x == "28" for x in [val2[0], val2[1]]):
						if (val1[0] == "29" and val1[1] in ["2", "02"]) or (val1[1] == "29" and val1[0] in ["2", "02"]):
							if self.isUS ():
								keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
							else:
								keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
							keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
							if self.isUS ():
								keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
							else:
								keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
							api.processPendingEvents ()
		# The following if statement has been added to correct the current field's non-recognition bug when year is 1601.
		if curValue == "1601":
			curDateField = 3
		if not self.vertical:
			self.sayField (curValue, curDateField)
		else:
			if config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"]:
				self.sayField (curValue)
			else:
				super (AnnounceFieldsLabels, self).event_valueChange ()

	def leftOrRight (self, value, flag = None):
		if flag:
			if len (value) == 4:
				keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
			else:
				keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
		else:
			if len (value) == 4:
				keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
			else:
				keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()

	def calculateCurField (self):
		val1 = self.value
			# The following calculation must be made in all cases, to allow those who use only Braille, to have the announcement of the labels of the date fields.
		keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send ()
		self.increment = 1
		api.processPendingEvents ()
		val2 = self.value
		# We verify that we are not on the last value
		if val1 == val2:
			# In this case, we move to the previous value.
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
			self.increment = -1
			api.processPendingEvents ()
		# We restore the value of the current date.
		if self.increment == 1:
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
			api.processPendingEvents ()
		elif self.increment == -1:
			keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send ()
			api.processPendingEvents ()
		self.whatChanged (val1, val2)
		self.increment = 0

	def script_verticalMovements (self, gesture):
		self.vertical = 1
		gesture.send ()
		self.calculateCurField ()

	def script_horizontalMovements (self, gesture):
		gesture.send ()
		self.vertical = 0
		self.calculateCurField ()

class GlobalPlugin (globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self, *args, **kwargs):
		super (GlobalPlugin, self).__init__(*args, **kwargs)
		# This block ensures compatibility with NVDA versions prior to 2018.2 which includes the settings panel.
		if hasattr (gui, "NVDASettingsDialog"):
			from gui import NVDASettingsDialog
			NVDASettingsDialog.categoryClasses.append(DayOfWeekSettingsDialog)
			self.createMenu ()
		else:
			self.createSubMenu ()

	def chooseNVDAObjectOverlayClasses (self, obj, clsList):
		if obj.value and obj.role == (controlTypes.ROLE_DROPLIST if hasattr(controlTypes, "ROLE_DROPLIST") else controlTypes.Role.DROPLIST) and isDatepickerDate (obj.value) and config.conf["dayOfWeek"]["enableAnnounces"]:
			clsList.insert (0, AnnounceFieldsLabels)

	def createMenu (self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.mainItem = self.toolsMenu.Append (wx.ID_ANY,
		# Translators: Item in the tools menu for the Addon dayOfTheWeek.
		_("Day of the &week..."),
		# Translators: The tooltyp text for the dayOfTheWeek item.
		_("Search a day in the calendar"))

		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onDateDialog, self.mainItem)

	def createSubMenu (self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		dowMenu = wx.Menu ()
		self.mainItem = self.toolsMenu.AppendSubMenu (dowMenu,
		# Translators: Item in the tools menu for the Addon dayOfTheWeek.
		_("Day of the &week..."),
		# Translators: The tooltyp text for the dayOfTheWeek submenu.
		_("{0} add-on and its settings").format (ADDON_NAME))

		dateChoice = dowMenu.Append (wx.ID_ANY,
		# Translators: The name of the first item in the dayOfTheWeek add-on submenu.
		_("Search a &day"),
		# Translators: The tooltyp text for the first item in the dayOfTheWeek add-on submenu.
		_("Search a day in the calendar"))
		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onDateDialog, dateChoice)

		addonSettings = dowMenu.Append (wx.ID_ANY,
		# Translators: The name of the second item in the dayOfTheWeek add-on submenu.
		_("{0} add-on se&ttings").format (ADDON_NAME),
		# Translators: The tooltyp text for the second item in the dayOfTheWeek add-on submenu.
		_("Configure the {0} add-on").format (ADDON_NAME))
		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onAddonSettingsDialog, addonSettings)

	def terminate (self):
		if hasattr (gui, "NVDASettingsDialog"):
			gui.NVDASettingsDialog.categoryClasses.remove(DayOfWeekSettingsDialog)
		try:
			if wx.version().startswith("4"):
				self.toolsMenu.Remove(self.mainItem)
			else:
				self.toolsMenu.RemoveItem(self.mainItem)
		except:
			pass

	def onDateDialog (self, evt):
		gui.mainFrame.prePopup ()
		d = DateDialog (gui.mainFrame)
		d.Show ()
		gui.mainFrame.postPopup ()

	def onAddonSettingsDialog (self, evt):
		gui.mainFrame.prePopup ()
		d = DayOfWeekSettingsDialog (gui.mainFrame)
		d.Show ()
		gui.mainFrame.postPopup ()

	def script_activateDayOfTheWeekDialog (self, gesture):
		wx.CallAfter (self.onDateDialog, gui.mainFrame)

	# Translators: Message presented in input help mode.
	script_activateDayOfTheWeekDialog.__doc__ = _("Allows you to find the day of the week corresponding to a chosen date.")

	def script_activateDayOfTheWeekSettingsDialog (self, gesture):
		wx.CallAfter (self.onAddonSettingsDialog, gui.mainFrame)

	# Translators: Message presented in input help mode.
	script_activateDayOfTheWeekSettingsDialog.__doc__ = _("Allows you to open the {0} add-on settings dialog.").format (ADDON_NAME)

