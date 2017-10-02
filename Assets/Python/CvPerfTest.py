## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *

gc = CyGlobalContext()

def fillMap():
	"Entry point to fill a map"
	CvFillMap().fillMap()
	
def emptyMap():
	"Entry point to empty a map"
	CvFillMap().emptyMap()

#
#
#
class CvFillMap:
	"class which handles filling the map"
	def __init__(self):
		self.waterUnits=[]
		self.landUnits=[]

	def emptyMap(self):
		"clear players and cities from the map"
		for i in range(gc.getMAX_PLAYERS()):
			gc.getPlayer(i).killUnits()
			gc.getPlayer(i).killCities()
	
	def fillMap(self):
		"populate the map for performance testing"
	
		self.waterUnits=[]
		self.landUnits=[]
		for i in range(gc.getNumUnitInfos()):
			if (gc.getUnitInfo(i).getDomainType()==DomainTypes.DOMAIN_SEA):
				self.waterUnits.append(i)
			else:
				self.landUnits.append(i)
	
		seed = 1001
		
		rand = CyRandom()
		rand.init(seed)
	
		map = CyMap()
		for iX in range(map.getGridWidth()):
			for iY in range(map.getGridHeight()):
				self.fillPlot(iX, iY, rand)
			print "fillPlot", iX
			
	def fillPlot(self, iX, iY, rand):
		"roll the dice and put something on this plot"
		ignoreChance = 4	# 40% chance of doing nothing
		cityChance = 2		# 20% chance of a city
		maxUnitsPerPlot = 10	# stack 1-10 units on a plot
		
		waterPlot = CyMap().plot(iX, iY).isWater()
		if waterPlot:
			ignoreChance = 9	# more likely to ignore a waterplot
			
		r=rand.get(10, "PerfTest")
		
		# check if we should do nothing
		if r<ignoreChance:
			return	
	
		owner = CyMap().plot(iX, iY).getOwner()
		if (owner != -1):
			player = gc.getPlayer(owner)
		else:
			player = gc.getPlayer(GC.getBARBARIAN_PLAYER())
	
		# check if we should place a city 
		r=rand.get(10, "PerfTest")
		if r<cityChance:
			if player.canFound(iX, iY):
				player.initCity(iX, iY)
				# add city buildings TODO
				return
	
		# otherwise place units
		numUnits = rand.get(maxUnitsPerPlot+1, "PerfTest") + 1
	
		if waterPlot:
			r = rand.get(len(self.waterUnits), "PerfTest")
			unitType = self.waterUnits[r]
		else:
			r = rand.get(len(self.landUnits), "PerfTest")
			unitType = self.landUnits[r]
				
		#	print "units", iX, iY
		unitAI = UnitAITypes.UNITAI_UNKNOWN
		for i in range(numUnits):
			player.initUnit(unitType, iX, iY, unitAI, DirectionTypes.NO_DIRECTION)
		
		# check if we should put improvements down TODO
		
		# check if we should put roads down TODO
	
		
		