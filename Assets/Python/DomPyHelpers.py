## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
#import Info as PyInfo
import CvUtil
import PyHelpers

gc = CyGlobalContext()

class DomPyPlayer (PyHelpers.PyPlayer):
### Custom Includes
	def greatPeopleThreshold (self):
		return self.player.greatPeopleThreshold(false)

class DomPyCity (PyHelpers.PyCity):
### Custom Includes 

### 12monkeys - Modified Special Domestic Advisor - begin 

## 12monkeys - 1.61 - begin
#	def getVisibleDefenseModifier(self):
#		return self.city.getVisibleDefenseModifier()
## 12monkeys - 1.61 - end

	def getDefenseModifier(self, bIgnoreBuilding):
		return self.city.getDefenseModifier(bIgnoreBuilding)

	def getWarWearinessModifier(self):
		return self.city.getWarWearinessModifier()
		
	def getBuildingDefense(self):
		return self.city.getBuildingDefense()

	def canConscript(self):
		return self.city.canConscript()
		
	def getConscriptUnit(self):
		return self.city.getConscriptUnit()
		
	def getDefenseDamage(self):
		return self.city.getDefenseDamage()
		
	def getAirModifier(self):
		return self.city.getAirModifier()
		
	def getNaturalDefense(self):
		return self.city.getNaturalDefense()
		
	def getTotalDefense(self, bIgnoreBuilding):
		return self.city.getTotalDefense(bIgnoreBuilding)

	def getRealPopulation(self):
		return self.city.getRealPopulation()

	def calculateDistanceMaintenance(self):
		return self.city.calculateDistanceMaintenance()
		
	def calculateNumCitiesMaintenance(self):
		return self.city.calculateNumCitiesMaintenance()

	def getNoMilitaryPercentAnger(self):
		return self.city.getNoMilitaryPercentAnger()

	def getFreeExperience(self):
		return self.city.getFreeExperience()

	def isBombarded(self):
		return self.city.isBombarded()

	def isCoastal(self):
		return self.city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN())
	
	def isVisible(self, eTeam, bDebug):
		return self.city.isVisible(eTeam, bDebug)

	def getBaseYieldRate(self, eIndex):
		return self.city.getBaseYieldRate(eIndex)
	
### 12monkeys - Modified Special Domestic Advisor - end 


	def isGovernmentCenter(self):
		"bool - City is Government Center?"
		if self.city.isGovernmentCenter():
			return True
		return False

	def getMilitaryHappinessUnits(self):
		"int - Number of units in City Garrison"
		return self.city.getMilitaryHappinessUnits()

	def isOccupation(self):
		return self.city.isOccupation()

	def isPower(self):
		"bool - does the city have any power plant"
		return self.city.isPower()

	def isDisorder(self):
		return self.city.isDisorder()

	def reallyGold(self):
		return self.city.getCommerceRate( CommerceTypes.COMMERCE_GOLD )

	def getOrderQueueLength(self):
		return self.city.getOrderQueueLength()

##        def isWeLoveTheKingDay(self):
##                "bool - is the city in WLTKD"
##                return self.city.isWeLoveTheKingDay()

	def foodDifference(self, bBottom):
		return self.city.foodDifference (bBottom)

	def getFood (self):
		return self.city.getFood()

	def getFoodTurnsLeft(self):
		return self.city.getFoodTurnsLeft()

	def getTradeCity (self, iIndex):
		return self.city.getTradeCity (iIndex)

	def calculateTradeYield (self, eIndex, iTradeProfit):
		return self.city.calculateTradeYield (eIndex, iTradeProfit)

	def calculateTradeProfit (self, pCity):
		return self.city.calculateTradeProfit (pCity)

	def getOccupationTimer(self):
		"int - how many turns of occupation left"
		return self.city.getOccupationTimer()

	def getCurrentProductionDifference (self, bIgnoreFood, bOverflow):
		return self.city.getCurrentProductionDifference (bIgnoreFood, bOverflow)

	def isFoodProduction (self):
		return self.city.isFoodProduction()

	def getSpecialistCount (self, nSpecialist):
		return self.city.getSpecialistCount (nSpecialist)

	def isSpecialistValid (self, nSpecialist, iExtra):
		return self.city.isSpecialistValid (nSpecialist, iExtra)

	def getMaxSpecialistCount (self, nSpecialist):
		return self.city.getMaxSpecialistCount (nSpecialist)

	def getForceSpecialistCount (self, nSpecialist):
		return self.city.getForceSpecialistCount (nSpecialist)

	def totalFreeSpecialists (self):
		return self.city.totalFreeSpecialists()

	def isCitizensAutomated (self):
		return self.city.isCitizensAutomated()

	def isProductionAutomated (self):
		return self.city.isProductionAutomated()

	def AI_isEmphasize (self, nEmphasis):
		return self.city.AI_isEmphasize (nEmphasis)
