# -*- coding: utf-8 -*-

# globalPlugins/dayOfTheWeek.py.

# Allows you to find the day of the week corresponding to a chosen date

# Copyright(C) 2015-2017 Abdel <abdelkrim.bensaid@gmail.com>, Noelia <nrm1977@gmail.com>
# Released under GPL 2
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from __future__ import unicode_literals
import addonHandler
import globalPluginHandler
import locale
import buildVersion
from scriptHandler import script
import speech
import re
from collections.abc import Callable
import keyboardHandler
import api
import controlTypes
import wx
import wx.adv
import gui
from gui.settingsDialogs import SettingsPanel as SettingsDialog, NVDASettingsDialog
from NVDAObjects.IAccessible import IAccessible
import config

addonHandler.initTranslation()
_: Callable[[str], str]

# Constants
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
ADDON_NAME = addonHandler.getCodeAddon().manifest["name"]

# Support for speech-on-demand mode introduced in recent NVDA versions.
speakOnDemand = {"speakOnDemand": True} if buildVersion.version_year > 2023 else {}

fieldLabels = (
	(
		_("You can select a day with the vertical arrows"),
		_("Select a day"),
	),
	(
		_("You can select a month with the vertical arrows"),
		_("Select a month"),
	),
	(
		_("You can select a year with the vertical arrows"),
		_("Select a year"),
	),
)

# Specific mapping for Georgian language localization to bypass standard format limitations.
georgianDays = {
	"0": "კვირა",
	"1": "ორშაბათი",
	"2": "სამშაბათი",
	"3": "ოთხშაბათი",
	"4": "ხუთშაბათი",
	"5": "პარასკევი",
	"6": "შაბათი",
}

curDateField = 0

confSpec = {
	"enableAnnounces": "boolean(default=True)",
	"labelAnnounceLevel": "string(default=long)",
	"reportFieldsValuesWhenMovingVertically": "boolean(default=False)",
}
config.conf.spec["dayOfWeek"] = confSpec


def isDatepickerDate(value):
	"""
	Validates the format of the date string to determine 
	if the overlay class should be applied.
	"""
	ptrn = r"^[\d]{1,4}[/\.-][\da-zA-Z]{1,3}[/\.-][\d]{1,4}[/\.-]?$"
	rg = re.compile(ptrn)
	return bool(rg.match(value))


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
		dlgTitle = _("Get the day of the week")
		super(DateDialog, self).__init__(parent, title=dlgTitle)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.dateLabel = _("Type or select a date")
		
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		sHelper.addItem(wx.StaticText(self, label=self.dateLabel))
		self.datePicker = sHelper.addItem(wx.adv.DatePickerCtrl(self))
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		
		self.datePicker.Bind(wx.EVT_CHAR, self.onListChar)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = self.mainSizer
		self.mainSizer.Fit(self)
		self.datePicker.SetFocus()
		self.Center(wx.BOTH | wx.CENTER)

	def __del__(self):
		DateDialog._instance = None

	def onListChar(self, evt):
		if evt.KeyCode == wx.WXK_SPACE:
			self.ProcessEvent(wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wx.ID_OK))
		else:
			evt.Skip()

	def onOk(self, evt):
		import languageHandler

		curNVDALang = languageHandler.getLanguage()
		date = self.datePicker.GetValue()
		locale.setlocale(locale.LC_TIME, "")
		weekDay = date.Format("%A") if not curNVDALang == "ka" else georgianDays[date.Format("%w")]
		
		if not gui.message.isModalMessageBoxActive():
			try:
				gui.messageBox(
					message=weekDay,
					caption=_("Your day"),
					style=wx.OK | wx.ICON_INFORMATION,
				)
				# Restore focus to the date picker after the messageBox is closed.
				self.datePicker.SetFocus()
			except Exception:
				pass


class DayOfWeekSettingsDialog(SettingsDialog):
	title = _("Day of the week")
	LABEL_ANNOUNCE_LEVELS = (
		("short", _("Short")),
		("long", _("Long")),
		("off", _("Off")),
	)

	def makeSettings(self, settingsSizer):
		self.enableAnnounces = _("En&able the accessibility of the date selector:")
		self.labelAnnounceLevelText = _("Level of the announces of &labels:")
		self.valueAnnounce = _("Enable announcements of the current date field value only, when moving &vertically:")

		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self.enableAnnouncesCheckBox = wx.CheckBox(self, label=self.enableAnnounces)
		self.enableAnnouncesCheckBox.SetValue(config.conf["dayOfWeek"]["enableAnnounces"])
		settingsSizerHelper.addItem(self.enableAnnouncesCheckBox)

		labelAnnounceLevelChoices = [name for level, name in self.LABEL_ANNOUNCE_LEVELS]
		self.labelAnnounceLevelsList = settingsSizerHelper.addLabeledControl(
			self.labelAnnounceLevelText,
			wx.Choice,
			choices=labelAnnounceLevelChoices,
		)
		curLevel = config.conf["dayOfWeek"]["labelAnnounceLevel"]
		for index, (level, name) in enumerate(self.LABEL_ANNOUNCE_LEVELS):
			if level == curLevel:
				self.labelAnnounceLevelsList.SetSelection(index)
				break
		self.labelAnnounceLevelsList.Enabled = self.enableAnnouncesCheckBox.IsChecked()

		self.reportDateFieldValuesCheckBox = wx.CheckBox(self, label=self.valueAnnounce)
		self.reportDateFieldValuesCheckBox.SetValue(
			config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"],
		)
		settingsSizerHelper.addItem(self.reportDateFieldValuesCheckBox)
		self.reportDateFieldValuesCheckBox.Enabled = self.enableAnnouncesCheckBox.IsChecked()
		self.enableAnnouncesCheckBox.Bind(wx.EVT_CHECKBOX, self.onCheckAnnounces)

	def postInit(self):
		self.enableAnnouncesCheckBox.SetFocus()

	def onCheckAnnounces(self, event):
		if self.enableAnnouncesCheckBox.IsChecked():
			self.labelAnnounceLevelsList.Enable()
			self.reportDateFieldValuesCheckBox.Enable()
		else:
			self.labelAnnounceLevelsList.Disable()
			self.reportDateFieldValuesCheckBox.Disable()

	def onOk(self, evt):
		config.conf["dayOfWeek"]["enableAnnounces"] = self.enableAnnouncesCheckBox.GetValue()
		labelAnnounceLevel = self.LABEL_ANNOUNCE_LEVELS[self.labelAnnounceLevelsList.GetSelection()][0]
		config.conf["dayOfWeek"]["labelAnnounceLevel"] = labelAnnounceLevel
		config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"] = (
			self.reportDateFieldValuesCheckBox.GetValue()
		)
		super(DayOfWeekSettingsDialog, self).onOk(evt)

	def onSave(self):
		config.conf["dayOfWeek"]["enableAnnounces"] = self.enableAnnouncesCheckBox.GetValue()
		labelAnnounceLevel = self.LABEL_ANNOUNCE_LEVELS[self.labelAnnounceLevelsList.GetSelection()][0]
		config.conf["dayOfWeek"]["labelAnnounceLevel"] = labelAnnounceLevel
		config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"] = (
			self.reportDateFieldValuesCheckBox.GetValue()
		)


class AnnounceFieldsLabels(IAccessible):
	increment = 0
	vertical = 0
	vMovementKeys = ("kb:upArrow", "kb:downArrow", "kb:home", "kb:end")
	hMovementKeys = ("kb:leftArrow", "kb:rightArrow")

	def event_gainFocus(self):
		global curDateField
		super(AnnounceFieldsLabels, self).event_gainFocus()
		if curDateField == 0:
			curDateField += 1
		self.calculateCurField()

	def event_valueChange(self):
		if self.increment:
			return
		super(AnnounceFieldsLabels, self).event_valueChange()

	def isUS(self):
		return "US" in locale.getdefaultlocale()[0]

	def sayField(self, curValue, columnID=None):
		import ui

		labelAnnounce = ""
		if columnID:
			if config.conf["dayOfWeek"]["labelAnnounceLevel"] != "off":
				if config.conf["dayOfWeek"]["labelAnnounceLevel"] == "long":
					labelAnnounce = fieldLabels[columnID - 1][0]
				else:
					labelAnnounce = fieldLabels[columnID - 1][1]
		field = "{0}, {1}".format(curValue, labelAnnounce) if columnID else curValue
		ui.message(field)

	def getDelimiter(self, value):
		ptrn = r"^[\d]{1,4}([\./-]).+$"
		rg = re.compile(ptrn)
		return rg.match(value).group(1)

	def whatChanged(self, val1, val2):  # noqa: C901
		global curDateField
		isYear = False
		isMonth = False
		isMonthUS = False
		val1 = val1.split(self.getDelimiter(val1))
		val2 = val2.split(self.getDelimiter(val2))
		
		# Workaround: Initialize curValue to 1601 to handle and correct 
		# field identification errors when encountering the base year 1601.
		curValue = "1601"
		
		if val1[0] != val2[0]:
			curValue = val1[0]
			if self.isUS() and len(val1[2]) == 4 and len(val1[1]) < 3:
				isMonthUS = True
				curDateField = 2
				
				# Compensation logic for the US layout when switching to shorter months.
				# Since the detection simulation performs a 'down arrow' then 'up arrow',
				# this can lead to an unintended decrease in the day value for shorter months.
				# The following conditions handle common years (February with 28 days) 
				# and dynamically correct the active field context.
				if val2[1] == "28":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
					elif val1[1] == "30":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
					elif val1[1] == "29":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
						
				# Compensation logic for US layout during leap years (February with 29 days).
				elif val2[1] == "29":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
					elif val1[1] == "30":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
						
				# Compensation logic for US layout during 30-day months.
				elif val2[1] == "30":
					if val1[1] == "31":
						keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
						keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						api.processPendingEvents()
			else:
				curDateField = 3 if len(curValue) == 4 else 1
				if len(curValue) == 4:
					isYear = True
					
					# Year field adjustment: Fixes day shifting issues when transitioning 
					# from a leap year to a common year during February.
					if val2[2] == "28":
						if val1[2] == "29" and val1[1] in ["2", "02"]:
							keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
							api.processPendingEvents()
		if val1[1] != val2[1]:
			if not isMonthUS and not isYear:
				curValue = val1[1]
				curDateField = 1 if self.isUS() and len(curValue) < 3 and len(val1[2]) == 4 else 2
				if curDateField == 2:
					isMonth = True
					
					# Standard layout compensation logic for common years (February with 28 days) 
					# when shifting fields across different month lengths.
					if any(x == "28" for x in [val2[0], val2[2]]):
						if any(x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
						elif any(x == "30" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
						elif any(x == "29" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
							
					# Standard layout compensation logic for leap years (February with 29 days).
					elif any(x == "29" for x in [val2[0], val2[2]]):
						if any(x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
						elif any(x == "30" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
							
					# Standard layout compensation logic for 30-day months.
					elif any(x == "30" for x in [val2[0], val2[2]]):
						if any(x == "31" for x in [val1[0], val1[2]]):
							self.leftOrRight(value=val1[0], flag=True)
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							self.leftOrRight(value=val1[0])
							api.processPendingEvents()
		if val1[2] != val2[2]:
			if not isYear and not isMonth:
				curDateField = 3 if len(val1[2]) == 4 else 1
				curValue = val1[2]
				if len(curValue) == 4:
					
					# Dynamic alignment handling for the year field when navigating 
					# and encountering February limit changes.
					if any(x == "28" for x in [val2[0], val2[1]]):
						if self.isUS():
							keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
						else:
							keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
							keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
							if self.isUS():
								keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
							else:
								keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
							api.processPendingEvents()
		if curValue == "1601":
			curDateField = 3
		if not self.vertical:
			self.sayField(curValue, curDateField)
		else:
			if config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"]:
				self.sayField(curValue)
			else:
				super(AnnounceFieldsLabels, self).event_valueChange()

	def leftOrRight(self, value, flag=None):
		if flag:
			if len(value) == 4:
				keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()
			else:
				keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
		else:
			if len(value) == 4:
				keyboardHandler.KeyboardInputGesture.fromName("leftArrow").send()
			else:
				keyboardHandler.KeyboardInputGesture.fromName("rightArrow").send()

	def calculateCurField(self):
		"""
		Simulates focus movement via arrow keys to safely determine the structure 
		and boundaries of the focused date field (useful for braille-only configurations).
		"""
		val1 = self.value
		keyboardHandler.KeyboardInputGesture.fromName("downArrow").send()
		self.increment = 1
		api.processPendingEvents()
		val2 = self.value
		
		# If values are identical, boundary limits are reached; step backwards instead.
		if val1 == val2:
			keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
			self.increment = -1
			api.processPendingEvents()
			
		# Restore the user's focus position to the original state.
		if self.increment == 1:
			keyboardHandler.KeyboardInputGesture.fromName("upArrow").send()
			api.processPendingEvents()
		elif self.increment == -1:
			keyboardHandler.KeyboardInputGesture.fromName("downArrow").send()
			api.processPendingEvents()
		self.whatChanged(val1, val2)
		self.increment = 0

	@script(gestures=vMovementKeys, **speakOnDemand)
	def script_verticalMovements(self, gesture):
		self.vertical = 1
		gesture.send()
		if config.conf["dayOfWeek"]["reportFieldsValuesWhenMovingVertically"]:
			speech.setSpeechMode(speech.SpeechMode.off)
			api.processPendingEvents()
			speech.setSpeechMode(speech.SpeechMode.talk)
		else:
			api.processPendingEvents()
		self.calculateCurField()

	@script(gestures=hMovementKeys, **speakOnDemand)
	def script_horizontalMovements(self, gesture):
		gesture.send()
		self.vertical = 0
		self.calculateCurField()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = ADDON_SUMMARY

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		NVDASettingsDialog.categoryClasses.append(DayOfWeekSettingsDialog)
		self.createMenu()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (
			obj.value
			and obj.role == controlTypes.Role.DROPLIST
			and isDatepickerDate(obj.value)
			and config.conf["dayOfWeek"]["enableAnnounces"]
			and obj.parent.parent.name == _("Get the day of the week")
		):
			clsList.insert(0, AnnounceFieldsLabels)

	def createMenu(self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.mainItem = self.toolsMenu.Append(
			wx.ID_ANY,
			_("Day of the &week..."),
			_("Search a day in the calendar"),
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onDateDialog, self.mainItem)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(DayOfWeekSettingsDialog)
		if wx.version().startswith("4"):
			self.toolsMenu.Remove(self.mainItem)
		else:
			self.toolsMenu.RemoveItem(self.mainItem)

	def onDateDialog(self, evt):
		gui.mainFrame.prePopup()
		d = DateDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		description=_("Allows you to find the day of the week corresponding to a chosen date."),
		**speakOnDemand,
	)
	def script_activateDayOfTheWeekDialog(self, gesture):
		wx.CallAfter(self.onDateDialog, gui.mainFrame)

	@script(
		description=_("Allows you to open the {0} add-on settings dialog.").format(ADDON_NAME),
		**speakOnDemand,
	)
	def script_activateDayOfTheWeekSettingsDialog(self, gesture):
		wx.CallAfter(gui.mainFrame.popupSettingsDialog, NVDASettingsDialog, DayOfWeekSettingsDialog)
        