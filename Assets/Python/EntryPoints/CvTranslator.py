## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import CvUtil
import re

gc = CyGlobalContext()
file_Text = 0
localText = CyTranslator()


IconMap = { 
			"[ICON_BULLET]" : FontSymbols.BULLET_CHAR,
			"[ICON_HAPPY]" : FontSymbols.HAPPY_CHAR,
			"[ICON_UNHAPPY]" : FontSymbols.UNHAPPY_CHAR,
			"[ICON_HEALTHY]" : FontSymbols.HEALTHY_CHAR,
			"[ICON_UNHEALTHY]" : FontSymbols.UNHEALTHY_CHAR,
			"[ICON_STRENGTH]" : FontSymbols.STRENGTH_CHAR,
			"[ICON_MOVES]" : FontSymbols.MOVES_CHAR,
			"[ICON_RELIGION]" : FontSymbols.RELIGION_CHAR,
			"[ICON_STAR]" : FontSymbols.STAR_CHAR,
			"[ICON_SILVER_STAR]" : FontSymbols.SILVER_STAR_CHAR,
			"[ICON_TRADE]" : FontSymbols.TRADE_CHAR,
			"[ICON_DEFENSE]" : FontSymbols.DEFENSE_CHAR,
			"[ICON_GREATPEOPLE]" : FontSymbols.GREAT_PEOPLE_CHAR,
			"[ICON_BAD_GOLD]" : FontSymbols.BAD_GOLD_CHAR,
			"[ICON_BAD_FOOD]" : FontSymbols.BAD_FOOD_CHAR,
			"[ICON_EATENFOOD]" : FontSymbols.EATEN_FOOD_CHAR,
			"[ICON_GOLDENAGE]" : FontSymbols.GOLDEN_AGE_CHAR,
			"[ICON_ANGRYPOP]" : FontSymbols.ANGRY_POP_CHAR,
			"[ICON_OPENBORDERS]" : FontSymbols.OPEN_BORDERS_CHAR,
			"[ICON_DEFENSIVEPACT]" : FontSymbols.DEFENSIVE_PACT_CHAR,
			"[ICON_MAP]" : FontSymbols.MAP_CHAR,
			"[ICON_OCCUPATION]" : FontSymbols.OCCUPATION_CHAR,
			"[ICON_POWER]" : FontSymbols.POWER_CHAR,
		 }


def finishText(argsList):

	szString = argsList[0]
	
	# FONT TAGS
	#listMatches = re.findall("\\[ICON_.*?\\]", szString)	
	#for szMatch in listMatches:
	#	if IconMap.has_key(szMatch):
	#		szReplacement = u"%c" % CyGame().getSymbolID(IconMap[szMatch])
	#	elif (szMatch == "[ICON_GOLD]"):
	#		szReplacement = u"%c" % gc.getCommerceInfo(CommerceTypes.COMMERCE_GOLD).getChar()
	#	elif (szMatch == "[ICON_RESEARCH]"):
	#		szReplacement = u"%c" % gc.getCommerceInfo(CommerceTypes.COMMERCE_RESEARCH).getChar()
	#	elif (szMatch == "[ICON_CULTURE]"):
	#		szReplacement = u"%c" % gc.getCommerceInfo(CommerceTypes.COMMERCE_CULTURE).getChar()
	#	elif (szMatch == "[ICON_ESPIONAGE]"):
	#		szReplacement = u"%c" % gc.getCommerceInfo(CommerceTypes.COMMERCE_ESPIONAGE).getChar()
	#	elif (szMatch == "[ICON_FOOD]"):
	#		szReplacement = u"%c" % gc.getYieldInfo(YieldTypes.YIELD_FOOD).getChar()
	#	elif (szMatch == "[ICON_PRODUCTION]"):
	#		szReplacement = u"%c" % gc.getYieldInfo(YieldTypes.YIELD_PRODUCTION).getChar()
	#	elif (szMatch == "[ICON_COMMERCE]"):
	#		szReplacement = u"%c" % gc.getYieldInfo(YieldTypes.YIELD_COMMERCE).getChar()
	#	else:
	#		szReplacement = u""
	#		print ("can't find font symbol %s in font map" % szMatch)	

	#	if len(szReplacement) > 0:		
	#		szString = szString.replace(szMatch, szReplacement)

	# DIPLO 'OUR' TAGS
	#listMatches = re.findall("\\[OUR_.*?\\]", szString)	
	#for szMatch in listMatches:
	#	iSeparator = szMatch.find(':')
	#	iEnd = szMatch.find(']')
	#	iCase = 0
	#	if (iSeparator != -1 and iEnd > iSeparator + 1):
	#		szCase = szMatch[iSeparator+1:iEnd]
	#		if (szCase.isdigit()):
	#			iCase = max(0, int(szCase) - 1)
	#	player = gc.getPlayer(CyDiplomacy().getWhoTradingWith())
	#	if (szMatch.find("[OUR_NAME") != -1):
	#		szReplacement = player.getNameForm(iCase)
	#	elif (szMatch.find("[OUR_EMPIRE") != -1):
	#		szReplacement = player.getCivilizationDescription(iCase)
	#	elif (szMatch.find("[OUR_CIV_SHORT") != -1):
	#		szReplacement = player.getCivilizationShortDescription(iCase)
	#	elif (szMatch.find("[OUR_CIV_ADJ") != -1):
	#		szReplacement = player.getCivilizationAdjective(iCase)
	#	elif (szMatch.find("[OUR_STATE_RELIGION") != -1):
	#		szReplacement = player.getStateReligionName(iCase)
	#	elif (szMatch.find("[OUR_BEST_UNIT") != -1):
	#		szReplacement = player.getBestAttackUnitName(iCase)
	#	elif (szMatch.find("[OUR_WORST_ENEMY") != -1):
	#		szReplacement = player.getWorstEnemyName()
	#	else:
	#		print ("can't find diplomacy text %s" % szMatch)	
	#		szReplacement = u""
	#	if len(szReplacement) > 0:		
	#		szString = szString.replace(szMatch, szReplacement)

	# DIPLO 'CT' TAGS
	#listMatches = re.findall("\\[CT_.*?\\]", szString)	
	#for szMatch in listMatches:
	#	iSeparator = szMatch.find(':')
	#	iEnd = szMatch.find(']')
	#	iCase = 0
	#	if (iSeparator != -1 and iEnd > iSeparator + 1):
	#		szCase = szMatch[iSeparator+1:iEnd]
	#		if (szCase.isdigit()):
	#			iCase = max(0, int(szCase) - 1)
	#	player = gc.getPlayer(gc.getGame().getActivePlayer())
	#	if (szMatch.find("[CT_NAME") != -1):
	#		szReplacement = player.getNameForm(iCase)
	#	elif (szMatch.find("[CT_EMPIRE") != -1):
	#		szReplacement = player.getCivilizationDescription(iCase)
	#	elif (szMatch.find("[CT_CIV_SHORT") != -1):
	#		szReplacement = player.getCivilizationShortDescription(iCase)
	#	elif (szMatch.find("[CT_CIV_ADJ") != -1):
	#		szReplacement = player.getCivilizationAdjective(iCase)
	#	elif (szMatch.find("[CT_STATE_RELIGION") != -1):
	#		szReplacement = player.getStateReligionName(iCase)
	#	elif (szMatch.find("[CT_BEST_UNIT") != -1):
	#		szReplacement = player.getBestAttackUnitName(iCase)
	#	elif (szMatch.find("[CT_WORST_ENEMY") != -1):
	#		szReplacement = player.getWorstEnemyName()
	#	else:
	#		print ("can't find diplomacy text %s" % szMatch)	
	#		szReplacement = u""
	#	if len(szReplacement) > 0:		
	#		szString = szString.replace(szMatch, szReplacement)

	# COLOR TAGS
	#listMatches = re.findall("\\[COLOR_.*?\\]", szString) + re.findall("</color>", szString)
	#for szMatch in listMatches:	
	#	if (szMatch == "[COLOR_REVERT]" or szMatch == "</color>"):
	#		szReplacement = u"</color>"
	#	else:
	#		szColor = str(szMatch)
	#		szColor = szColor.replace('[', '')
	#		szColor = szColor.replace(']', '')
			
	#		iColor = gc.getInfoTypeForString(szColor)
	#		if (iColor >= 0):
	#			color = gc.getColorInfo(iColor).getColor()
	#			szReplacement = (u"<color=%d,%d,%d,%d>" % (int(color.r * 255), int(color.g * 255), int(color.b * 255), int(color.a * 255)))	# GFC style
	#		else:
	#			szReplacement = u""	# temporary proxy
						
	#	if len(szReplacement) > 0:		
	#		szString = szString.replace(szMatch, szReplacement)

	# LINK TAGS
	#listMatches = re.findall("\\[LINK.*?=.*?\\]", szString)	
	#for szMatch in listMatches:	
	#	iSeparator = szMatch.find('=')
	#	iEnd = szMatch.find(']')
	#	szLink = szMatch[iSeparator+1:iEnd]
	#	szReplacement = u"<link='" + szLink + "'>"
	#	szString = szString.replace(szMatch, szReplacement)

	#listMatches = re.findall("\\[\\\LINK\\]", szString)	
	#for szMatch in listMatches:	
	#	szReplacement = u"</link>"
	#	szString = szString.replace(szMatch, szReplacement)

	return szString

def printOutText(argsList):
	global file_Text
	key, text = argsList
	
	if key == "DONE" or text == "DONE" and file_Text != 0:
		file_Text.close()
		return
	
	if file_Text == 0:
		file_Text = open("Civ4 GAME Text.txt", 'w')
	
	if file_Text != 0:
		file_Text.write("\n%s\n\t%s" %(key, text))
	