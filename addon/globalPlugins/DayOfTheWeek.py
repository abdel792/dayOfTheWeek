# -*- coding: UTF-8 -*-

# globalPlugins/dayOfTheWeek.py.

# Allows you to find the day of the week corresponding to a chosen date

#Copyright (C) 2015-2017 Abdel <abdelkrim.bensaid@gmail.com>, Noelia <nrm1977@gmail.com>
# Released under GPL 2
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
addonHandler.initTranslation ()
import globalPluginHandler
import speech
from logHandler import log
import keyboardHandler
import api
import os
import controlTypes
import wx
import gui
from gui.settingsDialogs import SettingsDialog
from NVDAObjects.IAccessible import IAccessible
import config

### Constants
ADDON_SUMMARY = addonHandler.Addon (os.path.join (os.path.dirname (__file__), "..").decode ("mbcs")).manifest["summary"]

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
	"0" : u"კვირა",
	"1" : u"ორშაბათი",
	"2" : u"სამშაბათი",
	"3" : u"ოთხშაბათი",
	"4" : u"ხუთშაბათი",
	"5" : u"პარასკევი",
	"6" : u"შაბათი"
}

curDateField = 0

confSpec = {
	"enableAnnounces" : "boolean(default = True)",
	"labelAnnounceLevel" : "string(default = long)",
	"reportFieldsValuesWhenMovingVertically" : "boolean(default = False)"
	}
config.conf.spec["dayOfWeek"] = confSpec

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
		mainSizer = wx.BoxSizer (wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper (self, orientation = wx.VERTICAL)
		# Translators: A label for a list in a dialog.
		dateLabel = _("Type or select a date")
		sHelper.addItem (wx.StaticText (self, label = dateLabel))
		self.datePicker = sHelper.addItem (wx.DatePickerCtrl (self))
		sHelper.addDialogDismissButtons (self.CreateButtonSizer (wx.OK|wx.CANCEL))
		self.datePicker.Bind (wx.EVT_CHAR, self.onListChar)
		self.Bind (wx.EVT_BUTTON, self.onOk, id = wx.ID_OK)
		mainSizer.Add (sHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag = wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit (self)
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
		weekDay = date.Format ("%A") if not curNVDALang == u"ka" else georgianDays[date.Format ("%w")]
		msgBox = gui.messageBox (
		message = weekDay,
		# Translators: The title of a dialog.
		caption = _("Your day"),
		style = wx.OK|wx.ICON_INFORMATION)

class DayOfWeekSettingsDialog (SettingsDialog):

	# Translators: The title of the add-on configuration dialog box.
	title = _("Configuration of the addon {0}").format ("dayOfTheWeek")
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
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper (self, sizer = settingsSizer)
		# Translators: The label of the checkbox to enable or disable the date selector accessibility.
		enableAnnounces = _("En&able the accessibility of the date selector:")
		self.enableAnnouncesCheckBox = wx.CheckBox (parent = self, label = enableAnnounces)
		self.enableAnnouncesCheckBox.SetValue (config.conf["dayOfWeek"]["enableAnnounces"])
		settingsSizerHelper.addItem (self.enableAnnouncesCheckBox)

		# Translators: The label for an item to select the level of the announces of labels (short, long or disabled).
		labelAnnounceLevelText = _("Level of the announces of labels:")
		labelAnnounceLevelChoices = [name for level, name in self.LABEL_ANNOUNCE_LEVELS]
		self.labelAnnounceLevelsList = settingsSizerHelper.addLabeledControl(labelAnnounceLevelText, wx.Choice, choices = labelAnnounceLevelChoices)
		curLevel = config.conf["dayOfWeek"]["labelAnnounceLevel"]
		for index, (level, name) in enumerate(self.LABEL_ANNOUNCE_LEVELS):
			if level == curLevel:
				self.labelAnnounceLevelsList.SetSelection(index)
				break
			else:
				log.debugWarning("Could not set level list to current level of the announces of labels")
		self.labelAnnounceLevelsList.Enabled = self.enableAnnouncesCheckBox.IsChecked ()

		# Translators: The label of the checkbox to enable or disable the current date field value only announcement when moving vertically.
		valueAnnounce = _("Enable announcements of the current date field value only, when moving &vertically")
		self.reportDateFieldValuesCheckBox = wx.CheckBox (parent = self, label = valueAnnounce)
		self.reportDateFieldValuesCheckBox.SetValue (config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"])
		settingsSizerHelper.addItem (self.reportDateFieldValuesCheckBox)
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

	def sayFieldLabel (self, curValue, columnID = None):
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

	def whatChanged (self, val1, val2):
		global curDateField
		val1 = val1.split ("/")
		val2 = val2.split ("/")
		# To fix a bug with the year 1601, we are forced to initialize the value of curValue to 1601
		curValue = "1601"
		if val1[0] != val2[0]:
			# We're in the day field.
			curDateField = 1
			curValue = val1[0]
		if val1[1] != val2[1]:
			# We're in the month field.
			curDateField = 2
			curValue = val1[1]
			# Here is a technique to fix the problem when switching to shorter months.
			# Since the calculation function executes a down arrow and an up arrow to find the value of the current month, it often switches to shorter months, which changes the value of the day.
			# The following if block is for the common years, where the February month is 28 days.
			if val2[0] == "28":
				if val1[0] == "31":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
				elif val1[0] == "30":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
				elif val1[0] == "29":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
			# The following elif block is for the leap years, where the February month is 29 days.
			elif val2[0] == "29":
				if val1[0] == "31":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
				elif val1[0] == "30":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
			# The following elif block is for the 30-day months.
			elif val2[0] == "30":
				if val1[0] == "31":
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					api.processPendingEvents ()
		if val1[2] != val2[2]:
			# We're in the year field.
			curDateField = 3
			curValue = val1[2]
			# Here is a technique to fix the problem when switching to shorter years, for instance, when switching from a leap year to a common year.
			# Since the calculation function executes a down arrow and an up arrow to find the value of the current year, it sometimes switches to shorter years, which changes the value of the day field in February month.
			if val2[0] == "28":
				if val1[0] == "29" and val1[1] == "02":
					keyboardHandler.KeyboardInputGesture.fromName ("rightArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
					keyboardHandler.KeyboardInputGesture.fromName ("leftArrow").send ()
					api.processPendingEvents ()
		# The following if statement has been added to correct the current field's non-recognition bug when year is 1601.
		if curValue == "1601":
			curDateField = 3
		if not self.vertical:
			self.sayFieldLabel (curValue, curDateField)
		else:
			if config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"]:
				self.sayFieldLabel (curValue)
			else:
				super (AnnounceFieldsLabels, self).event_valueChange ()

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
		self.createSubMenu ()

	def chooseNVDAObjectOverlayClasses (self, obj, clsList):
		if obj.value and obj.role == controlTypes.ROLE_DROPLIST and len (obj.value) == 10 and "/" in obj.value and config.conf["dayOfWeek"]["enableAnnounces"]:
			clsList.insert (0, AnnounceFieldsLabels)

	def createSubMenu (self):
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		dowMenu = wx.Menu ()
		self.mainItem = self.menu.AppendSubMenu (dowMenu,
		# Translators: Item in the preferences menu for the Addon dayOfTheWeek.
		_("Day of the &week..."),
		# Translators: The tooltyp text for the dayOfTheWeek submenu.
		_("Day of the week add-on and its settings"))

		dateChoice = dowMenu.Append (wx.ID_ANY,
		# Translators: The name of the first item in the dayOfTheWeek add-on submenu.
		_("Search a &day"),
		# Translators: The tooltyp text for the first item in the dayOfTheWeek add-on submenu.
		_("Search a day in the calendar"))
		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onDateDialog, dateChoice)

		addonSettings = dowMenu.Append (wx.ID_ANY,
		# Translators: The name of the second item in the dayOfTheWeek add-on submenu.
		_("{0} add-on se&ttings").format ("dayOfTheWeek"),
		# Translators: The tooltyp text for the second item in the dayOfTheWeek add-on submenu.
		_("Configure the dayOfTheWeek add-on"))
		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onAddonSettingsDialog, addonSettings)

	def terminate (self):
		try:
			self.menu.RemoveItem (self.mainItem)
		except wx.PyDeadObjectError:
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
	script_activateDayOfTheWeekSettingsDialog.__doc__ = _("Allows you to open the dayOfTheWeek add-on settings dialog.")

