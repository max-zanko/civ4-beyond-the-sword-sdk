## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class CvPediaUnitChart:
	"Civilopedia Screen for Unit Combat Groups"

	def __init__(self, main):
		self.iGroup = -1
		self.top = main
			
		self.X_UNITS = 50
		self.Y_UNITS = 95
		self.W_UNITS = 700
		self.H_UNITS = 570
		self.DX_UNITS = 150
		self.DY_UNITS = 40
		self.Y_TEXT_MARGIN = 6

	# Screen construction function
	def interfaceScreen(self, iGroup):	
			
		self.iGroup = iGroup
	
		self.top.deleteAllWidgets()						
							
		screen = self.top.getScreen()
		
		bNotActive = (not screen.isActive())
		if bNotActive:
			self.top.setPediaCommonWidgets()

		# Header...
		if (self.iGroup >= gc.getNumUnitCombatInfos()):
			szHeader = localText.getText("TXT_KEY_PEDIA_ALL_UNITS", ())
		else:
			szHeader = gc.getUnitCombatInfo(self.iGroup).getDescription()
		szHeader = u"<font=4b>" + szHeader.upper() + u"</font>"
		szHeaderId = self.top.getNextWidgetName()
		screen.setLabel(szHeaderId, "Background", szHeader, CvUtil.FONT_CENTER_JUSTIFY, self.top.X_SCREEN, self.top.Y_TITLE, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
		
		# Top
		screen.setText(self.top.getNextWidgetName(), "Background", self.top.MENU_TEXT, CvUtil.FONT_LEFT_JUSTIFY, self.top.X_MENU, self.top.Y_MENU, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_PEDIA_MAIN, CivilopediaPageTypes.CIVILOPEDIA_PAGE_UNIT_GROUP, -1)

		if self.top.iLastScreen	!= CvScreenEnums.PEDIA_UNIT_CHART or bNotActive:		
			self.placeLinks(true)
			self.top.iLastScreen = CvScreenEnums.PEDIA_UNIT_CHART
		else:
			self.placeLinks(false)
				
		self.placeUnitTable()
						
	def placeUnitTable(self):
		screen = self.top.getScreen()
		
		panelName = self.top.getNextWidgetName()
		screen.addPanel( panelName, "", "", true, true,
			self.X_UNITS, self.Y_UNITS, self.W_UNITS, self.H_UNITS, PanelStyles.PANEL_STYLE_BLUE50 )
		
		iMargin = 40
		panelName2 = self.top.getNextWidgetName()
		screen.addPanel( panelName2, "", "", true, true,
                                 self.X_UNITS + iMargin, self.Y_UNITS + iMargin, self.W_UNITS - (iMargin * 2), self.H_UNITS - (iMargin * 2), PanelStyles.PANEL_STYLE_BLUE50 )
		szTable = self.top.getNextWidgetName()
		screen.addTableControlGFC(szTable, 4,
			self.X_UNITS + iMargin, self.Y_UNITS + iMargin + 5, self.W_UNITS - (iMargin * 2), self.H_UNITS - (iMargin * 2) - 10, True, False, 32,32, TableStyles.TABLE_STYLE_EMPTY)
		screen.enableSort(szTable)
			
#		screen.attachTableControlGFC( panelName, szTable, 4, False, True, 32, 32, TableStyles.TABLE_STYLE_EMPTY );
			
		iTableWidth = self.W_UNITS - (iMargin * 2)
		iColWidth = int(iTableWidth * (7 / 19.0))
		screen.setTableColumnHeader(szTable, 0, "", iColWidth)
		iColWidth = int(iTableWidth * (4 / 19.0))
		screen.setTableColumnHeader(szTable, 1, u"%c" % CyGame().getSymbolID(FontSymbols.STRENGTH_CHAR), iColWidth)
		screen.setTableColumnHeader(szTable, 2, u"%c" % CyGame().getSymbolID(FontSymbols.MOVES_CHAR), iColWidth)
		screen.setTableColumnHeader(szTable, 3, u"%c" % gc.getYieldInfo(YieldTypes.YIELD_PRODUCTION).getChar(), iColWidth)
					
		# count units in this group
		nUnits = 0
		for j in range(gc.getNumUnitInfos()):
			if (self.iGroup == gc.getUnitInfo(j).getUnitCombatType() or self.iGroup == gc.getNumUnitCombatInfos()):
				nUnits += 1

		dy = self.DY_UNITS
		yTextMargin = self.Y_TEXT_MARGIN
		if (self.iGroup == gc.getNumUnitCombatInfos()):
			dy = self.DY_UNITS/2
			yTextMargin = 0

		# sort Units by strength
		i = 0
		unitsList=[(0,0,0,0,0)]*nUnits
		for j in range(gc.getNumUnitInfos()):
			if (self.iGroup == gc.getUnitInfo(j).getUnitCombatType() or self.iGroup == gc.getNumUnitCombatInfos()):
			
				if (gc.getUnitInfo(j).getDomainType() == DomainTypes.DOMAIN_AIR):
					iStrength = unicode(gc.getUnitInfo(j).getAirCombat())
					iMovement = unicode(gc.getUnitInfo(j).getAirRange())
				else:
					iStrength = unicode(gc.getUnitInfo(j).getCombat())
					iMovement = unicode(gc.getUnitInfo(j).getMoves())
					
				if (gc.getUnitInfo(j).getProductionCost() < 0):
					szCost = localText.getText("TXT_KEY_NON_APPLICABLE", ())
				else:
					szCost = unicode(gc.getUnitInfo(j).getProductionCost())# + u"%c" % gc.getYieldInfo(YieldTypes.YIELD_PRODUCTION).getChar()
					
				unitsList[i] = (iStrength, iMovement, szCost, gc.getUnitInfo(j).getDescription(), j)
				i += 1

		for i in range(nUnits):			
			iRow = screen.appendTableRow(szTable)
			screen.setTableText(szTable, 0, iRow, u"<font=3>" + unitsList[i][3] + u"</font>", "", WidgetTypes.WIDGET_PEDIA_JUMP_TO_UNIT, unitsList[i][4], 1, CvUtil.FONT_LEFT_JUSTIFY)						
			screen.setTableInt(szTable, 1, iRow, u"<font=3>" + unicode(unitsList[i][0]) + u"</font>", "", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY)
			screen.setTableInt(szTable, 2, iRow, u"<font=3>" + unicode(unitsList[i][1]) + u"</font>", "", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY)
			screen.setTableInt(szTable, 3, iRow, u"<font=3>" + unicode(unitsList[i][2]) + u"</font>", "", WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY)

	def placeLinks(self, bRedraw):

		screen = self.top.getScreen()

		if bRedraw:
			screen.clearListBoxGFC(self.top.LIST_ID)
		
		# sort groups alphabetically
		listSorted=[(0 ,0)] * gc.getNumUnitCombatInfos()
		for j in range(gc.getNumUnitCombatInfos()):
			listSorted[j] = (gc.getUnitCombatInfo(j).getDescription(), j)
		listSorted.sort()			

		iSelected = 0
		if bRedraw:		
			screen.appendListBoxString( self.top.LIST_ID, localText.getText("TXT_KEY_PEDIA_ALL_GROUPS", ()), WidgetTypes.WIDGET_PEDIA_JUMP_TO_UNIT_COMBAT, gc.getNumUnitCombatInfos(), 0, CvUtil.FONT_LEFT_JUSTIFY )
		if self.iGroup == gc.getNumUnitCombatInfos():
			iSelected = 0

		i = 1
		for iI in range(gc.getNumUnitCombatInfos()):
			if (not gc.getUnitCombatInfo(listSorted[iI][1]).isGraphicalOnly()):
				if bRedraw:
					screen.appendListBoxString( self.top.LIST_ID, listSorted[iI][0], WidgetTypes.WIDGET_PEDIA_JUMP_TO_UNIT_COMBAT, listSorted[iI][1], 0, CvUtil.FONT_LEFT_JUSTIFY )
				if listSorted[iI][1] == self.iGroup:
					iSelected = i
				i += 1			

		screen.setSelectedListBoxStringGFC(self.top.LIST_ID, iSelected)
		
	# Will handle the input for this screen...
	def handleInput (self, inputClass):
		return 0

