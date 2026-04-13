# Day of the week #

*	 लेखकहरू: अब्दुल र नोलिया रुइज्
*	 अनुबहन [stable version][1]
*	 डाउनलोड [विकास संस्करण][2]

यो उपकर्मीको सहयोगले आफुले चाहेको मितिको बार पत्ता लगाउन सकिने छ ।

It adds an item in the NVDA Tools menu named "Day of the week", to open a
dialog composed of 3 controls:

*	 A listbox to choose or type your date.
*	 An "OK" button to display a messageBox containing your day.
*	 पातो बन्द गर्नका लागि  बन्द भन्ने टाँकको प्रयोग गर । 

## टिप्पणी: ##
*	 You can close this dialog just by pressing Escape.
*	 You can assign a shortcut to open the dialog in "Input gestures" menu
   and, more precisely, in the "Tools" category.

## Changes for 2.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   dialog asking for a date;
*	 Added the GPL license to the addon;
*	 Days of the week have been translated, so that the add-on works properly
   in the different languages;
*	 Used the %w format for the dates rather than %a to avoid encoding errors.

## १.० मा गरिएका परिवर्तनहरू ##

*	 शुरूको संस्करण

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dw

[2]: https://addons.nvda-project.org/files/get.php?file=dw-dev
