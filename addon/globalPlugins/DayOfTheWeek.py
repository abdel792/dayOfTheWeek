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
import keyboardHandler
import globalVars
import api
import os
import controlTypes
import wx
import gui
from gui.settingsDialogs import SettingsDialog
from NVDAObjects.IAccessible import IAccessible
import config

### Constants
ADDON_SUMMARY = addonHandler.Addon (os.path.join (os.path.dirname (__file__), '..').decode ('mbcs')).manifest['summary']

fieldLabels = (
	# Translators: The label of the days field.
	_("You can select a day with the vertical arrows"),
	# Translators: The label of the months field.
	_("You can select a month with the vertical arrows"),
	# Translators: The label of the years field.
	_("You can select a year with the vertical arrows")
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
	'reportLabels': 'boolean(default = True)'
	}
config.conf.spec['dayOfWeek'] = confSpec

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

	def makeSettings (self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper (self, sizer = settingsSizer)
		# Translators: The label of the checkbox to enable or disable the date field labels announcements.
		labelAnnounce = _("Enable announcements of the date field labels")
		self.reportDateFieldLabelsCheckBox = wx.CheckBox (parent = self, label = labelAnnounce)
		self.reportDateFieldLabelsCheckBox.SetValue (config.conf['dayOfWeek']['reportLabels'])
		settingsSizerHelper.addItem (self.reportDateFieldLabelsCheckBox)

	def postInit (self):
		self.reportDateFieldLabelsCheckBox.SetFocus ()

	def onOk (self, evt):
		config.conf['dayOfWeek']['reportLabels'] = self.reportDateFieldLabelsCheckBox.GetValue ()
		super (DayOfWeekSettingsDialog, self).onOk (evt)

class MyDayOfWeek (IAccessible):

	increment = 0

	def event_gainFocus (self):
		global curDateField
		speech.speakObject (self, reason = controlTypes.REASON_FOCUS)
		if curDateField == 0: curDateField += 1
		self.sayFieldLabel (curDateField)

	def sayFieldLabel (self, columnID):
		import ui
		fieldID = columnID - 1
		label = fieldLabels[fieldID]
		ui.message (label)

	def whatChanged (self, val1, val2):
		global curDateField
		val1 = val1.split ("/")
		val2 = val2.split ("/")
		if val1[0] != val2[0]:
			curDateField = 1
		if val1[1] != val2[1]:
			curDateField = 2
		if val1[2] != val2[2]:
			curDateField = 3
		self.sayFieldLabel (curDateField)

	def event_valueChange(self):
		if self.increment:
			return
		else:
			super(MyDayOfWeek, self).event_valueChange()

	def script_switchBetweenDateFields (self, gesture):
		val1 = self.value
		gesture.send ()
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
		if self.increment == -1:
			keyboardHandler.KeyboardInputGesture.fromName ("downArrow").send ()
			api.processPendingEvents ()
		elif self.increment == 1:
			keyboardHandler.KeyboardInputGesture.fromName ("upArrow").send ()
			api.processPendingEvents ()
		self.whatChanged (val1, val2)
		self.increment = 0

	__gestures = {
		"kb:leftArrow":"switchBetweenDateFields",
		"kb:rightArrow":"switchBetweenDateFields"
	}

class GlobalPlugin (globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self, *args, **kwargs):
		super (GlobalPlugin, self).__init__(*args, **kwargs)
		self.createSubMenu ()

	def chooseNVDAObjectOverlayClasses (self, obj, clsList):
		if obj.value and obj.role == controlTypes.ROLE_DROPLIST and len (obj.value) == 10 and "/" in obj.value and config.conf["dayOfWeek"]["reportLabels"]:
			clsList.insert (0, MyDayOfWeek)

	def createSubMenu (self):
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		dowMenu = wx.Menu ()
		self.mainItem = self.menu.AppendSubMenu (dowMenu,
		# Translators: Item in the preferences menu for the Addon dayOfTheWeek.
		_("&Day of the week..."),
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

