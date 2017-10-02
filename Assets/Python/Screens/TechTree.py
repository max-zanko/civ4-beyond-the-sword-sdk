## Sid Meier's Civilization 4
from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums
import math

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class TechTree:
	"Creates Tech Tree"
	def __init__ (self):
		self.dIsRequiredPrereqFor = {}
		self.dIsOptionalPrereqFor = {}

		self.dRequiredPrereqTechs = {}
		self.dOptionalPrereqTechs = {}

		for iLoopTech in range (gc.getNumTechInfos()):
			RequiredPrereqs = []
			OptionalPrereqs = []
			for k in range(gc.getNUM_OR_TECH_PREREQS()):
				eOrPrereq = gc.getTechInfo (iLoopTech).getPrereqOrTechs(k)
				if eOrPrereq != -1:
					OptionalPrereqs.append (eOrPrereq)
			for k in range(gc.getNUM_AND_TECH_PREREQS()):
				eAndPrereq = gc.getTechInfo (iLoopTech).getPrereqAndTechs(k)
				if eAndPrereq != -1:
					RequiredPrereqs.append (eAndPrereq)

			if len(OptionalPrereqs) == 1:
				RequiredPrereqs.extend (OptionalPrereqs)
				self.dOptionalPrereqTechs [iLoopTech] = []
			else:
				self.dOptionalPrereqTechs [iLoopTech] = OptionalPrereqs
			self.dRequiredPrereqTechs [iLoopTech] = RequiredPrereqs

		for iTech in range (gc.getNumTechInfos()):
			self.dRequiredPrereqFor = []
			self.dOptionalPrereqFor = []
			for iLoopTech in range(gc.getNumTechInfos()):
				if iTech in self.dRequiredPrereqTechs[iLoopTech]:
					self.dRequiredPrereqFor.append (iLoopTech)
				elif iTech in self.dOptionalPrereqTechs [iLoopTech]:
					self.dOptionalPrereqFor.append (iLoopTech)

			self.dIsRequiredPrereqFor[iTech] = self.dRequiredPrereqFor
			self.dIsOptionalPrereqFor[iTech] = self.dOptionalPrereqFor
#		CvUtil.pyPrint ("%s" % self.dIsRequiredPrereqFor)

	def RequiredLeadsTo (self, iTech):
		return self.dIsRequiredPrereqFor[iTech]

	def OptionalLeadsTo (self, iTech):
		return self.dIsOptionalPrereqFor[iTech]

	def RequiredPrereqs (self, iTech):
		return self.dRequiredPrereqTechs[iTech]

	def OptionalPrereqs (self, iTech):
		return self.dOptionalPrereqTechs[iTech]
